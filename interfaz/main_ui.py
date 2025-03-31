# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'

from PyQt5 import QtCore, QtGui, QtWidgets
from config import VERSION, AUTOR, NOMBRE_APP


class Ui_SeleccionConexion(object):
    def setupUi(self, SeleccionConexion):
        SeleccionConexion.setObjectName("SeleccionConexion")
        SeleccionConexion.resize(400, 260)
        self.verticalLayout = QtWidgets.QVBoxLayout(SeleccionConexion)
        self.labelTitulo = QtWidgets.QLabel(SeleccionConexion)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.verticalLayout.addWidget(self.labelTitulo)
        self.radioApiKey = QtWidgets.QRadioButton(SeleccionConexion)
        self.radioApiKey.setObjectName("radioApiKey")
        self.verticalLayout.addWidget(self.radioApiKey)
        self.inputApiKey = QtWidgets.QLineEdit(SeleccionConexion)
        self.inputApiKey.setObjectName("inputApiKey")
        self.verticalLayout.addWidget(self.inputApiKey)
        self.radioChatGPTWeb = QtWidgets.QRadioButton(SeleccionConexion)
        self.radioChatGPTWeb.setObjectName("radioChatGPTWeb")
        self.verticalLayout.addWidget(self.radioChatGPTWeb)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.botonContinuar = QtWidgets.QPushButton(SeleccionConexion)
        self.botonContinuar.setObjectName("botonContinuar")
        self.horizontalLayout.addWidget(self.botonContinuar)
        self.botonTema = QtWidgets.QPushButton(SeleccionConexion)
        self.botonTema.setObjectName("botonTema")
        self.horizontalLayout.addWidget(self.botonTema)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.retranslateUi(SeleccionConexion)
        QtCore.QMetaObject.connectSlotsByName(SeleccionConexion)

    def retranslateUi(self, SeleccionConexion):
        _translate = QtCore.QCoreApplication.translate
        SeleccionConexion.setWindowTitle(_translate("SeleccionConexion", "Ayase - Selección de conexión"))
        self.labelTitulo.setText(_translate("SeleccionConexion", "¿Cómo querés conectar a Ayase?"))
        self.radioApiKey.setText(_translate("SeleccionConexion", "Usar API Key de OpenAI"))
        self.inputApiKey.setPlaceholderText(_translate("SeleccionConexion", "Ingresá tu API Key aquí"))
        self.radioChatGPTWeb.setText(_translate("SeleccionConexion", "Usar ChatGPT Web (Plus o Gratis)"))
        self.botonContinuar.setText(_translate("SeleccionConexion", "Continuar"))
        self.botonTema.setText(_translate("SeleccionConexion", "🌙"))
