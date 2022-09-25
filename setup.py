import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from Interfaz1 import Ui_Principal

class gestor(QDialog):

    def __init__(self): #Inicializador
        super().__init__()
        self.inicioGUI()

    def inicioGUI(self):
        self.ui = Ui_Principal()
        self.ui.setupUi(self)


        self.ui.btn_inicio.clicked.connect(self.pg_modificar)
        self.ui.btnreservar.clicked.connect(self.reservar)
        self.ui.btn_dispon.clicked.connect(self.disponibilidad)

        self.show()

    #def disponibilidad(self):


    #def reservar(self):

def main():                             #Entrada a la aplicación
    app = QtWidgets.QApplication(sys.argv)        #Se crea una aplicación QT
    vent = Ui_Principal()
    ventana = QtWidgets.QMainWindow()
    vent.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":              #Evita que se ejecuten los comandos, solo las funciones definidas
    main()