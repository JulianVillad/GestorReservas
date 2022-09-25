#Importación de librerías necesarias
import sys
from PyQt5 import QtCore, QtGui, QtWidgets                          #PyQT5 para el diseño de la interfaz
from PyQt5.uic import loadUi                                        #Para cargar la interfaz
from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow,
                             QCalendarWidget, QPushButton,
                             QTableWidget,QTableWidgetItem)
import sqlite3 as sql                                               #Sqlite3 para la base de datos
from bdatos import BaseDatos                                        #Importamos la clase para administrar la base de datos

class ventanappal(QMainWindow):                                     #Programa de reservas
    def __init__(self):
        super(ventanappal, self).__init__()
        loadUi('Interfaz.ui',self)

        #Botones de navegación (Barra superior):
        self.btn_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_inicio))
        self.btn_tarifas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_tarifas))
        self.btn_modificar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_modificar))
        self.btn_admin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_admin))
        self.btn_salir.clicked.connect(lambda: self.close())

        self.BBDD = BaseDatos()                                     #Llamo la función creada en bdatos.py
        
        self.btn_consultar_mod.clicked.connect(self.buscarevento)       #Botón buscar evento
        self.btn_enviar_ini.clicked.connect(self.reservaeventos)        #Botón reservar
        self.btn_refresh_leven.clicked.connect(self.consultaevento)     #Botón actualizar
        self.btn_cancelar_mod.clicked.connect(self.cancelarevento)      #Botón cancelar evento
        self.btn_modificar_mod.clicked.connect(self.modificarevento)    #Botón modificar evento
        self.btn_ordenar_leven.clicked.connect(self.ordenartabla)       #Botón ordenar por fecha
        self.btn_dispon_ini.clicked.connect(self.consdis)               #Botón consultar disponibilidad

    def consultaevento(self):                                       #Consulta de eventos
        datos = self.BBDD.consultabd()
        i = len(datos)
        #print(datos)
        self.tableW.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row[0])
            self.tableW.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableW.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableW.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableW.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableW.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableW.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableW.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableW.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            tablerow+=1

    def reservaeventos(self):                                       #Registrar un evento
        ID1 = self.LE_ID_ini.text()
        Nombre1 = self.LE_Nombre_ini.text().upper()
        Apellido1 = self.LE_Apellidos_ini.text().upper()
        Celular1 = self.LE_Cel_ini.text()
        Correo1 = self.LE_Correo_ini.text().upper()
        Salon1 = self.cBsalon_ini.currentText()
        Fecha_inicial1 = self.LE_finicial_ini.text()
        Fecha_final1 = self.LE_ffinal_ini.text()
        if ID1 != '' and Nombre1 != '' and Apellido1 != '' and Celular1 != '' and Salon1 != '' and Fecha_inicial1 != '' and Fecha_final1 != '':
            self.BBDD.reservabd(ID1,Nombre1,Apellido1,Celular1,Correo1,Salon1,Fecha_inicial1,Fecha_final1)
            self.lbl_confirm_ini.setText('Registro exitoso')
            self.LE_ID_ini.clear()
            self.LE_Nombre_ini.clear()
            self.LE_Apellidos_ini.clear()
            self.LE_Cel_ini.clear()
            self.LE_Correo_ini.clear()
            self.LE_finicial_ini.clear()
            self.LE_ffinal_ini.clear()
        else:
            self.lbl_confirm_ini.setText('Por favor llene todos los campos')

    def buscarevento(self):                                         #Consultar un evento
        Fcan = str(self.LE_finicial_mod.text())
        Scan = str(self.cB_salon_mod.currentText())
        evento = self.BBDD.buscarevento(Fcan, Scan)
        #print(evento)
        if len(evento) == 0:
            self.lbl_alerta_mod.setText('No existen eventos para esas fechas')
            self.LE_ID_mod.setText('')
            self.LE_ffinal_mod.setText('')
            self.LE_nombre_mod.setText('')
            self.LE_apellido_mod.setText('')
            self.LE_cel_mod.setText('')
            self.LE_correo_mod.setText('')
        else:
            self.LE_ID_mod.setText(evento[0][0])
            self.LE_ffinal_mod.setText(evento[0][7])
            self.LE_nombre_mod.setText(evento[0][1])
            self.LE_apellido_mod.setText(evento[0][2])
            self.LE_cel_mod.setText(evento[0][3])
            self.LE_correo_mod.setText(evento[0][4])
    
    def cancelarevento(self):                                       #Cancelar un evento
        Fcan = str(self.LE_finicial_mod.text())
        Scan = str(self.cB_salon_mod.currentText())
        evento = self.BBDD.buscarevento(Fcan, Scan)
        #print(evento)
        if len(evento) != 0:
            self.BBDD.cancelarev(Fcan, Scan)
        
    def modificarevento(self):                                      #Modificar un evento
        Fcan = str(self.LE_finicial_mod.text())
        Scan = str(self.cB_salon_mod.currentText())
        evento = self.BBDD.buscarevento(Fcan, Scan)
        #print(evento)
        if len(evento) != 0:
            IDmod = self.LE_ID_mod.text()
            nwnombre = self.LE_nombre_mod.text()
            nwapellido = self.LE_apellido_mod.text()
            nwcel = self.LE_cel_mod.text()
            nwcorreo = self.LE_correo_mod.text()
            nwsalon = self.cB_salon_mod.currentText()
            nwfinicial = self.LE_finicial_mod.text()
            nwffinal = self.LE_ffinal_mod.text()
            self.BBDD.modificarevento(nwnombre, nwapellido, nwcel, nwcorreo, nwsalon, nwfinicial, nwffinal,IDmod)
    
    def ordenartabla(self):
        self.BBDD.orden()
        
    def consdis(self):
        datos = self.BBDD.consultabd()
        Fini = str(self.LE_finicial_ini.text())
        Ffin = str(self.LE_finicial_ini.text())
        Sln = str(self.cBsalon_ini.currentText())
        i = 0
        for row in datos:
            if Fini == datos[i][6] and Sln == datos[i][5]:
                self.lbl_confirm_ini.setText('NO DISPONIBLE')
            else:
                self.lbl_confirm_ini.setText('DISPONIBLE')
        
        
        
if __name__ == "__main__":              #Evita que se ejecuten los comandos, solo las funciones definidas
    app = QApplication(sys.argv)
    mi_app = ventanappal()
    mi_app.show()
    sys.exit(app.exec_())