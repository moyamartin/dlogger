# -*- coding: utf-8 -*-

<<<<<<< HEAD
# Form implementation generated from reading ui file 'mainwindow.ui'
=======
# Form implementation generated from reading ui file 'mainwindow_1.ui'
>>>>>>> origin/master
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
<<<<<<< HEAD
        MainWindow.resize(766, 470)
        MainWindow.setMinimumSize(QtCore.QSize(740, 470))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
=======
        MainWindow.resize(782, 510)
        MainWindow.setMinimumSize(QtCore.QSize(740, 470))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
>>>>>>> origin/master
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(67, 17))
        self.label.setMaximumSize(QtCore.QSize(67, 17))
        self.label.setSizeIncrement(QtCore.QSize(67, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboPorts = QtGui.QComboBox(self.centralwidget)
        self.comboPorts.setMinimumSize(QtCore.QSize(250, 25))
        self.comboPorts.setMaximumSize(QtCore.QSize(250, 25))
        self.comboPorts.setObjectName(_fromUtf8("comboPorts"))
        self.comboPorts.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboPorts)
        self.pushConectar = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushConectar.sizePolicy().hasHeightForWidth())
        self.pushConectar.setSizePolicy(sizePolicy)
        self.pushConectar.setMinimumSize(QtCore.QSize(100, 25))
        self.pushConectar.setMaximumSize(QtCore.QSize(100, 25))
        self.pushConectar.setSizeIncrement(QtCore.QSize(80, 0))
        self.pushConectar.setObjectName(_fromUtf8("pushConectar"))
        self.horizontalLayout.addWidget(self.pushConectar)
        spacerItem = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
<<<<<<< HEAD
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsView = PlotWidget(self.tab)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 766, 20))
=======
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(60, 23))
        self.label_3.setSizeIncrement(QtCore.QSize(60, 23))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.checkBox_frecuencia = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_frecuencia.setEnabled(False)
        self.checkBox_frecuencia.setMinimumSize(QtCore.QSize(100, 23))
        self.checkBox_frecuencia.setMaximumSize(QtCore.QSize(100, 23))
        self.checkBox_frecuencia.setObjectName(_fromUtf8("checkBox_frecuencia"))
        self.horizontalLayout_2.addWidget(self.checkBox_frecuencia)
        self.checkBox_capacidad = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_capacidad.setEnabled(False)
        self.checkBox_capacidad.setMinimumSize(QtCore.QSize(100, 23))
        self.checkBox_capacidad.setMaximumSize(QtCore.QSize(100, 23))
        self.checkBox_capacidad.setObjectName(_fromUtf8("checkBox_capacidad"))
        self.horizontalLayout_2.addWidget(self.checkBox_capacidad)
        spacerItem1 = QtGui.QSpacerItem(468, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.plot_1 = PlotWidget(self.tab)
        self.plot_1.setMinimumSize(QtCore.QSize(720, 360))
        self.plot_1.setObjectName(_fromUtf8("plot_1"))
        self.horizontalLayout_3.addWidget(self.plot_1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.plot_2 = PlotWidget(self.tab_2)
        self.plot_2.setMinimumSize(QtCore.QSize(720, 360))
        self.plot_2.setObjectName(_fromUtf8("plot_2"))
        self.horizontalLayout_4.addWidget(self.plot_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 782, 20))
>>>>>>> origin/master
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArchivo = QtGui.QMenu(self.menuBar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuAyuda = QtGui.QMenu(self.menuBar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
<<<<<<< HEAD
        self.menuConfiguraci_n = QtGui.QMenu(self.menuBar)
        self.menuConfiguraci_n.setObjectName(_fromUtf8("menuConfiguraci_n"))
=======
>>>>>>> origin/master
        MainWindow.setMenuBar(self.menuBar)
        self.actionConfiguraci_n = QtGui.QAction(MainWindow)
        self.actionConfiguraci_n.setObjectName(_fromUtf8("actionConfiguraci_n"))
        self.actionNinguno = QtGui.QAction(MainWindow)
        self.actionNinguno.setCheckable(False)
        self.actionNinguno.setEnabled(True)
        self.actionNinguno.setObjectName(_fromUtf8("actionNinguno"))
        self.actionSearchPorts = QtGui.QAction(MainWindow)
        self.actionSearchPorts.setCheckable(False)
        self.actionSearchPorts.setObjectName(_fromUtf8("actionSearchPorts"))
        self.actionConectar_dispositivo = QtGui.QAction(MainWindow)
        self.actionConectar_dispositivo.setObjectName(_fromUtf8("actionConectar_dispositivo"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionContenido = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Assets/Help_mark_query_question_support-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContenido.setIcon(icon)
        self.actionContenido.setObjectName(_fromUtf8("actionContenido"))
        self.actionSalir = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Assets/cross_close_quit-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon1)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionNueva_ventana = QtGui.QAction(MainWindow)
        self.actionNueva_ventana.setObjectName(_fromUtf8("actionNueva_ventana"))
        self.actionAbrir_datos = QtGui.QAction(MainWindow)
        self.actionAbrir_datos.setObjectName(_fromUtf8("actionAbrir_datos"))
<<<<<<< HEAD
        self.actionGr_fica_1 = QtGui.QAction(MainWindow)
        self.actionGr_fica_1.setObjectName(_fromUtf8("actionGr_fica_1"))
        self.actionPuertos = QtGui.QAction(MainWindow)
        self.actionPuertos.setObjectName(_fromUtf8("actionPuertos"))
        self.actionGr_ficas_2 = QtGui.QAction(MainWindow)
        self.actionGr_ficas_2.setObjectName(_fromUtf8("actionGr_ficas_2"))
        self.menuArchivo.addAction(self.actionAbrir_datos)
        self.menuAyuda.addAction(self.actionAbout)
        self.menuConfiguraci_n.addAction(self.actionGr_ficas_2)
        self.menuConfiguraci_n.addAction(self.actionPuertos)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuConfiguraci_n.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
=======
        self.menuArchivo.addAction(self.actionAbrir_datos)
        self.menuAyuda.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
>>>>>>> origin/master
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ADN - Plot", None))
        self.label.setText(_translate("MainWindow", "Puerto:", None))
        self.comboPorts.setItemText(0, _translate("MainWindow", "No hay dispositivos conectados", None))
        self.pushConectar.setText(_translate("MainWindow", "Conectar", None))
<<<<<<< HEAD
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gráfica 1", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.menuConfiguraci_n.setTitle(_translate("MainWindow", "Configuración", None))
=======
        self.label_3.setText(_translate("MainWindow", "Mostrar:", None))
        self.checkBox_frecuencia.setText(_translate("MainWindow", "Frecuencia", None))
        self.checkBox_capacidad.setText(_translate("MainWindow", "Capacidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Evolución Temporal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Histograma", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
>>>>>>> origin/master
        self.actionConfiguraci_n.setText(_translate("MainWindow", "Configuracion", None))
        self.actionNinguno.setText(_translate("MainWindow", "Ninguno", None))
        self.actionSearchPorts.setText(_translate("MainWindow", "Buscar puertos", None))
        self.actionConectar_dispositivo.setText(_translate("MainWindow", "Conectar dispositivo", None))
        self.actionAbout.setText(_translate("MainWindow", "Acerca de ADN-Plot", None))
        self.actionContenido.setText(_translate("MainWindow", "Contenido", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionNueva_ventana.setText(_translate("MainWindow", "Nueva ventana", None))
        self.actionAbrir_datos.setText(_translate("MainWindow", "Abrir datos", None))
<<<<<<< HEAD
        self.actionGr_fica_1.setText(_translate("MainWindow", "Gráfica 1", None))
        self.actionPuertos.setText(_translate("MainWindow", "Puertos", None))
        self.actionGr_ficas_2.setText(_translate("MainWindow", "Gráficas", None))
=======
>>>>>>> origin/master

from pyqtgraph import PlotWidget
