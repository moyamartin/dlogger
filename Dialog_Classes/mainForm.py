# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QAction
from pyqtgraph import PlotWidget
from Threads_Classes import checkPortsThread, dataThread, generateLogThread
import maindesign
import errorForm
import ackForm
import aboutForm
import serial

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainForm(QtGui.QMainWindow, maindesign.Ui_MainWindow):
    serialPort = None
    actionPuertos = []

    dialogErrorForm = None
    dialogAckForm = None
    dialogAbout = None

    readThread = None
    writeFileThread = None

    # tabs variables
    tabs = []
    tabs_layouts = []
    plots = []
    tab_button = None

    # Datos a plotear
    datos_tiempo = []
    datos_frecuencia = []
    datos_capacidad = []
    datos_histo_cap = []

    # Buffer interno de 300 valores
    buffer_tiempo = []
    buffer_frecuencia = []
    buffer_capacidad = []
    buffer_histo_cap = []

    def __init__(self):
        # Super() es usado para referirse a clases padres sin nombrarla explícitamente
        super(self.__class__, self).__init__()

        # Setea el layout y los widgets definidos dentro del ui
        # Está definido automáticamente en maindesign.py
        self.setupUi(self)

        # Creamos un puerto serie vacío así más tarde en la conexión setea las variables
        # Y podemos pasarlo como parámetro al thread de lectura
        self.serialPort = serial.Serial()

        # Creamos un objeto del hilo de lectura de datos
        self.readThread = dataThread.DataThread(self.serialPort)
        self.connect(self.readThread, SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)'),
                     self.update_plot)
        self.connect(self.readThread, SIGNAL('finished()'), self.close_port)

        # Instanciamos el objeto de la clase CheckPortsThread()
        # Esta se encarga de detectar los puertos abiertos de los dispositivos conectados por USB
        self.setDevices = checkPortsThread.CheckPortsThread()
        self.connect(self.setDevices, SIGNAL('update_ports(PyQt_PyObject)'), self.update_combo)
        self.connect(self.setDevices, SIGNAL('finished()'), self.conectar_dispositivo)

        # Otorgamos función a los botones conectar y desconectar
        # Su función es bastante intuitiva
        self.pushConectar.clicked.connect(self.conectar_dispositivo)

        # Al iniciar la aplicación queremos que comienze a detectar los dispositivos automáticamente
        self.setDevices.start()

        self.writeFileThread = generateLogThread.GenerateLogThread()

        self.actionAbout.triggered.connect(self.open_about)
        self.actionAbrir_datos.triggered.connect(self.open_plot)

        self.tab_button = QtGui.QToolButton(self)
        self.tab_button.setText('+')
        font = self.tab_button.font()
        font.setBold(True)
        self.tab_button.setFont(font)
        self.tabWidget.setCornerWidget(self.tab_button)
        self.tab_button.clicked.connect(self.add_plot)

        self.tabWidget.tabBar().setTabButton(0, QtGui.QTabBar.RightSide, None)

        self.tabWidget.tabCloseRequested.connect(self.removePlot)

    def removePlot(self, index):
        self.tabWidget.removeTab(index)

    def add_plot(self):

        self.tabs.append(QtGui.QWidget())
        self.plots.append(PlotWidget(self.tabs[len(self.tabs) - 1]))
        self.plots[len(self.plots) - 1].setObjectName(_fromUtf8('plot_' + str(len(self.plots) + 1)))
        self.tabs_layouts.append(QtGui.QVBoxLayout(self.tabs[len(self.tabs) - 1]))

        self.tabs_layouts[len(self.tabs_layouts) - 1].addWidget(self.plots[len(self.plots) - 1])

        self.tabs[len(self.tabs) - 1].setLayout(self.tabs_layouts[len(self.tabs_layouts) - 1])
        self.tabWidget.insertTab(self.tabWidget.count(), self.tabs[len(self.tabs) - 1], _fromUtf8('Gráfica' +
                                                                                                  str(
                                                                                                      self.tabWidget.count() + 1)))
        self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

    def modify_plot(self):
        aux_frecuencia = self.datos_frecuencia
        aux_capacidad = self.datos_capacidad
        if self.checkBox_frecuencia.isChecked() is False:
            aux_frecuencia = []
        if self.checkBox_capacidad.isChecked() is False:
            aux_capacidad = []

        self.curve_capacidad.setData([], [])
        self.curve_frecuencia.setData([], [])
        self.update_plot(aux_capacidad, aux_frecuencia, self.datos_tiempo)

        del aux_frecuencia
        del aux_capacidad

    def open_plot(self):

        del self.datos_tiempo[:]
        del self.datos_frecuencia[:]
        del self.datos_capacidad[:]

        file_name = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo de datos', '/home')
        try:
            f = open(file_name, 'r')

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_tiempo.append(float(aux[i]))

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_frecuencia.append(float(aux[i]))

            aux = f.readline().split(',')
            for i in range(0, len(aux) - 1):
                self.datos_capacidad.append(float(aux[i]))

            f.close()

            self.curve_capacidad.setData([], [])
            self.curve_frecuencia.setData([], [])
            self.update_plot(self.datos_frecuencia, self.datos_capacidad, self.datos_tiempo)
            self.plot_1.setXRange(0, self.datos_tiempo[len(self.datos_tiempo) - 1])

            self.checkBox_frecuencia.setEnabled(True)
            self.checkBox_frecuencia.setChecked(True)
            self.checkBox_capacidad.setEnabled(True)
            self.checkBox_capacidad.setChecked(True)

        except IOError:
            pass

    def open_about(self):
        if self.dialogAbout is None:
            self.dialogAbout = aboutForm.AboutForm()
        self.dialogAbout.show()

    def close_port(self):
        self.datos_tiempo.extend(self.buffer_tiempo)
        self.datos_frecuencia.extend(self.buffer_frecuencia)
        self.datos_capacidad.extend(self.buffer_capacidad)

        self.writeFileThread.set_data(self.datos_frecuencia, self.datos_capacidad
                                      , self.datos_tiempo)
        self.writeFileThread.start()

        self.readThread.flush()
        self.serialPort.close()

        if len(self.datos_frecuencia) > 0:
            self.update_plot(self.datos_capacidad, self.datos_frecuencia, self.datos_tiempo)
            self.plot_1.setXRange(0, self.datos_tiempo[len(self.datos_tiempo) - 1])
        else:
            self.curve_capacidad.setData([], [])
            self.curve_frecuencia.setData([], [])

        self.plot_1.setMouseEnabled(True, True)

        self.comboPorts.setEnabled(True)
        self.pushConectar.setEnabled(True)
        self.setDevices.start()

        self.checkBox_frecuencia.setEnabled(True)
        self.checkBox_frecuencia.setChecked(True)
        self.checkBox_capacidad.setEnabled(True)
        self.checkBox_capacidad.setChecked(True)

    def end_readings(self):
        self.pushConectar.setText("Conectar")
        self.pushConectar.clicked.disconnect()
        self.pushConectar.clicked.connect(self.conectar_dispositivo)

        self.readThread.set_stop()
        self.readThread.quit()

    def kill_set_devices(self):
        # Queremos terminar la detección de los dispositivos porque ya se eligió a cual conectarse
        self.setDevices.set_stop()
        self.setDevices.quit()

    # conectar_dispositivo() es llamado al pulsar el botón conectar
    def conectar_dispositivo(self):

        del self.datos_tiempo[:]
        del self.datos_frecuencia[:]
        del self.datos_capacidad[:]

        self.plot_1.setYRange(0, 65000, 0.01)
        self.plot_1.setXRange(0, 3, 0.01)

        self.readThread.set_timer()

        self.curve_capacidad.setData([], [])
        self.curve_frecuencia.setData([], [])
        self.plot_1.setMouseEnabled(False, False)

        # PUERTO_DISPOSITIVO contiene el nombre del puerto serie referida al dispositivo
        # Se obtiene a través del comboBox donde se presentan los puertos disponibles
        # Windows: \\PORTX (1 - X - 255)
        # Unix: /tty[A-Z][a-z]
        PUERTO_DISPOSITIVO = str(self.comboPorts.itemText(self.comboPorts.currentIndex()))

        # PUERTO_BAUDRATE contiene el baudrate que seleccionamos dentro del comboBox del baudrate
        PUERTO_BAUDRATE = 19200

        # Se intenta conectar al dispositivo, como puede llegar a devolver una excepción se procede de la siguiente
        # manera
        # ERROR: presenta una ventana de error (errorForm.ErrorForm()
        # CORRECTO: presenta una ventana de autenticación (ackForm) y ejecuta el thread de lectura (readThread.Start())
        try:
            # Definimos constantes del puerto seria (puerto, baudrate, bytesize, paridad, bits de stop, timeout)
            self.serialPort = serial.Serial(PUERTO_DISPOSITIVO, PUERTO_BAUDRATE, serial.EIGHTBITS, serial.PARITY_NONE,
                                            serial.STOPBITS_ONE, 10, 10)
            # Muestra la ventana de autenticación
            if self.dialogAckForm is None:
                self.dialogAckForm = ackForm.AckForm()
            self.dialogAckForm.show()

            # Setea el puerto serie
            self.readThread.set_serial_port(self.serialPort)

            # Inicializa el hilo de lectura
            self.readThread.start()

            self.checkBox_frecuencia.setEnabled(False)
            self.checkBox_capacidad.setEnabled(False)

            self.comboPorts.setEnabled(False)

            self.checkBox_frecuencia.setChecked(True)
            self.checkBox_capacidad.setChecked(True)

            self.pushConectar.setText("Desconectar")
            self.pushConectar.clicked.disconnect()
            self.pushConectar.clicked.connect(self.end_readings)
        except (OSError, serial.SerialException):
            if self.dialogErrorForm is None:
                self.dialogErrorForm = errorForm.ErrorForm()

            # Re-inicializa el thread de detección
            # Muestra la ventana de error
            self.dialogErrorForm.show()
            self.setDevices.start()

    # updateCombo(deviceText): actualiza la lista de puertos disponibles
    # recibe como parámetro un String correspondiente a la dirección de los dispositivos
    def update_combo(self, device_text):
        if device_text == 'No hay dispositivos conectados':
            if self.comboPorts.itemText(0) != 'No hay dispositivos conectados':
                self.comboPorts.setItemText(0, device_text)
                self.remove_extra_items()
        else:
            if self.comboPorts.itemText(0) != device_text[0]:
                self.comboPorts.setItemText(0, device_text[0])
            else:
                if len(device_text) > 1:
                    for k in range(1, len(device_text)):
                        if self.comboPorts.findText(device_text[k]) == -1:
                            self.comboPorts.addItem(device_text[k])
                else:
                    self.remove_extra_items()

    # Remueve valores extras del comboPorts
    def remove_extra_items(self):
        if self.comboPorts.count() >= 1:
            for k in range(1, self.comboPorts.count()):
                self.comboPorts.removeItem(k)

    # Actualiza la gráfica
    def update_plot(self, cap, frec, tiempo, hist_y):  # , patron, signal):
        self.buffer_frecuencia = frec
        self.buffer_capacidad = cap
        self.buffer_tiempo = tiempo

        self.curve_histograma.setData(hist_y)

        if len(self.buffer_frecuencia) != 0:  # and len(self.buffer_temp) is len(self.buffer_tiempo):
            # self.fix_matrix(self.buffer_temp)
            # self.curve_temp.setData(x=self.buffer_tiempo, y=self.buffer_temp)
            self.curve_frecuencia.setData(x=self.buffer_tiempo, y=self.buffer_frecuencia, antialias=True)
        else:
            self.curve_frecuencia.setData([], [])

        if len(self.buffer_capacidad) != 0:
            # and len(self.buffer_pid) is len(self.buffer_tiempo):
            # self.fix_matrix(self.buffer_pid)
            # self.curve_pid.setData(x=self.buffer_tiempo, y=self.buffer_pid)
            self.curve_capacidad.setData(x=self.buffer_tiempo, y=self.buffer_capacidad, antialias=True)
        else:
            self.curve_capacidad.setData([], [])

        if len(self.buffer_tiempo) >= 15:
            self.plot_1.setXRange(self.buffer_tiempo[len(self.buffer_tiempo) - 1] - 3,
                                  self.buffer_tiempo[len(self.buffer_tiempo) - 1], 0.05)
