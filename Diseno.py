#Importación de librerías necesarias
import sys
from PyQt5 import QtCore, QtGui, QtWidgets                          #PyQT5 para el diseño de la interfaz
from PyQt5.uic import loadUi                                        #Para cargar la interfaz
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow,
                             QCalendarWidget, QPushButton,
                             QTableWidget,QTableWidgetItem)
import sqlite3 as sql                                               #Sqlite3 para la base de datos
from bdatos import BaseDatos                                        #Importamos la clase para administrar la base de datos

class ventanappal(QMainWindow):
    def __init__(self):
        super(ventanappal, self).__init__()
        loadUi('Interfaz.ui',self)

        self.btn_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_inicio))
        self.btn_tarifas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_tarifas))
        self.btn_modificar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_modificar))
        self.btn_admin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_admin))
        self.btn_salir.clicked.connect(lambda: self.close())

        self.BBDD = BaseDatos()

        #self.btn_dispon_ini.clicked.connect(self.consultabd)
        self.btn_enviar_ini.clicked.connect(self.reservaeventos)
        self.btn_refresh_leven.clicked.connect(self.consultaevento)
        #self.btn_cancelar_ini_clicked.connect(self.close)

    def consultaevento(self):
        datos = self.BBDD.consultabd()
        i = len(datos)
        print(datos)
        self.tableW.setRowCount(i)
        print(i)
        tablerow = 1
        print(datos[0])
        self.tableW.setItem(tablerow, 0, row[0])
        for row in datos:
            print(row[0])
            self.tableW.setItem(tablerow, 0, row[0])
            self.tableW.setItem(tablerow, 1, row[1])
            self.tableW.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableW.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableW.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableW.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableW.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableW.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            tablerow+=1

    def reservaeventos(self):
        ID1 = self.LE_ID_ini.int()
        Nombre1 = self.LE_Nombre_ini().text()
        Apellido1 = self.LE_Apellidos_ini().text()
        Celular1 = self.LE_Cel_ini().text()
        Correo1 = self.LE_Correo_ini().text()
        Salon1 = self.cBsalon_ini.text()
        fechai = self.clicked.connect(self.calendarW_ini.selectedDate())
        print(self.calendarW_ini.selectedDate)
        fechait = str(fechai)
        self.LE_finicial_ini.setText(fechait)
        Fecha_inicial1 = self.LE_finicial_ini().text()
        Fecha_final1 = self.LE_Ffinal_ini().text()
        if ID1 != '' and Nombre1 != '' and Apellido1 != '' and Celular1 != '' and Salon1 != '' and Fecha_inicial1 != '' and Fecha_final1 != '':
            self.BBDD.reservabd(ID1,Nombre1,Apellido1,Celular1,Correo1,Salon1,Fecha_inicial1,Fecha_final1)
            self.lbl_confirm_ini.setText('Registro exitoso')
            self.LE_ID_ini.clear()
            self.LE_Nombre_ini().clear()
            self.LE_Apellidos_ini().clear()
            self.LE_Cel_ini().clear()
            self.LE_Correo_ini.clear()
            self.LE_finicial_ini.clear()
            self.LE_ffinal_ini.clear()
        else:
            self.lbl_confirm_ini.setText('Por favor llene todos los campos')


if __name__ == "__main__":              #Evita que se ejecuten los comandos, solo las funciones definidas
    app = QApplication(sys.argv)
    mi_app = ventanappal()
    mi_app.show()
    sys.exit(app.exec_())