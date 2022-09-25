import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
import sqlite3

class ventanappal(QMainWindow):
    def __init__(self):
        super(ventanappal, self).__init__()
        loadUi('Interfaz.ui',self)
