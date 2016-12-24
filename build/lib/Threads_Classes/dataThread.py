# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import serial


class DataThread(QThread):
    frecuencia = []
    capacidad  = []
    tiempo = []
    data_y_hist = []

    for j in range(20460):
        data_y_hist.append(0)

    serial_port = serial.Serial()

    start_time = 0
    actual_time = 0
    actual_time_e = 0
    actual_time_pid = 0
    actual_time_ref = 0

    non_stop = True

    aux_1 = []
    aux_2 = []

    aux_frec = []
    aux_cap = []

    flag_data = False
    flag_updating = False
    flag_ready = False

    i = 0
    aux_cadena = []

    def __init__(self, serial_port):
        QThread.__init__(self)
        self.serial_port = serial_port

    def __del__(self):
        self.wait()

    def set_serial_port(self, serial_p):
        self.serial_port = serial_p

    def set_timer(self):
        self.start_time = 0
        self.actual_time = 0

    def flush(self):
        del self.frecuencia[:]
        del self.capacidad[:]
        del self.tiempo[:]


    def set_stop(self):
        self.non_stop = False

    # Override de la funcion run
    def run(self):
        self.non_stop = True
        while self.non_stop:
            if self.non_stop:
                try:
                    self.aux = self.serial_port.read()
                    if self.flag_data:
                        self.aux_cadena.append(self.aux)
                        self.i += 1

                        if self.i == 4:
                            self.i = 0

                            try:
                                self.flag_data = False
                                self.capacidad.append(float(self.to_integer(self.aux_cadena, 0)))
                                self.frecuencia.append(float(self.to_integer(self.aux_cadena, 2)))
                                self.data_y_hist[int(self.to_integer(self.aux_cadena, 0))] = self.data_y_hist[int(self.to_integer(self.aux_cadena, 0))] + 1
                                self.tiempo.append(self.actual_time)
                                self.actual_time += 0.2
                                self.flag_ready = True

                                del self.aux_cadena[:]
                                if self.flag_ready:

                                    self.emit(SIGNAL('update_plot(PyQt_PyObject, PyQt_PyObject, PyQt_PyObject, PyQt_PyObject)')
                                              , self.capacidad, self.frecuencia, self.tiempo, self.data_y_hist)
                                    self.msleep(10)
                                    self.flag_ready = False

                            except ValueError:
                                pass
                    elif self.aux is 'A':
                        self.flag_data = True
                        print self.aux
                except(OSError, serial.SerialException):
                    pass

            else:
                self.serial_port.close()


    def to_integer(self, cadena, i):
        to_bits = (ord(cadena[i]) << 8) | ord(cadena[i + 1])
        return to_bits
