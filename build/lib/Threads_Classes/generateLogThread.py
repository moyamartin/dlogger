# -*- coding: utf-8 -*-

from PyQt4.QtCore import QThread, SIGNAL
import time


# Generates data file after connection or if the internal buffer is big enough
class GenerateLogThread(QThread):
    actualTime = None
    f = None
    data_temp = None
    data_error = None
    data_pid = None
    data_ref = None
    data_time = None

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def set_data(self, capacidad, frecuencia, tiempo):
        self.data_frecuencia = frecuencia
        self.data_capacidad = capacidad
        self.data_time = tiempo

    def run(self):
        self.actualTime = time.strftime("%d-%m-%y-%H-%M-%S")
        f = open('dataplot - ' + self.actualTime + '.data', 'w')

        for i in range(0, len(self.data_time)):
            f.write(str(self.data_time[i]) + ',')

        f.write('\n')
        for i in range(0, len(self.data_frecuencia)):
            f.write(str(self.data_frecuencia[i]) + ',')

        f.write('\n')
        for i in range(0, len(self.data_capacidad)):
            f.write(str(self.data_capacidad[i]) + ',')

        f.close()
