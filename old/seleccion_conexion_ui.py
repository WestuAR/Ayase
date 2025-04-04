# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seleccion_conexion.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SeleccionConexion(object):
    def setupUi(self, SeleccionConexion):
        SeleccionConexion.setObjectName("SeleccionConexion")
        SeleccionConexion.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(SeleccionConexion)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitulo = QtWidgets.QLabel(SeleccionConexion)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.gridLayout.addWidget(self.labelTitulo, 0, 0, 1, 2)
        self.radioApiKey = QtWidgets.QRadioButton(SeleccionConexion)
        self.radioApiKey.setChecked(True)
        self.radioApiKey.setObjectName("radioApiKey")
        self.gridLayout.addWidget(self.radioApiKey, 1, 0, 1, 2)
        self.radioChatGPTWeb = QtWidgets.QRadioButton(SeleccionConexion)
        self.radioChatGPTWeb.setObjectName("radioChatGPTWeb")
        self.gridLayout.addWidget(self.radioChatGPTWeb, 2, 0, 1, 2)
        self.inputApiKey = QtWidgets.QLineEdit(SeleccionConexion)
        self.inputApiKey.setVisible(True)
        self.inputApiKey.setObjectName("inputApiKey")
        self.gridLayout.addWidget(self.inputApiKey, 3, 0, 1, 2)
        self.botonTema = QtWidgets.QPushButton(SeleccionConexion)
        self.botonTema.setObjectName("botonTema")
        self.gridLayout.addWidget(self.botonTema, 4, 0, 1, 1)
        self.botonContinuar = QtWidgets.QPushButton(SeleccionConexion)
        self.botonContinuar.setObjectName("botonContinuar")
        self.gridLayout.addWidget(self.botonContinuar, 4, 1, 1, 1)

        self.retranslateUi(SeleccionConexion)
        QtCore.QMetaObject.connectSlotsByName(SeleccionConexion)

    def retranslateUi(self, SeleccionConexion):
        _translate = QtCore.QCoreApplication.translate
        SeleccionConexion.setWindowTitle(_translate("SeleccionConexion", "Conectar Ayase"))
        self.labelTitulo.setText(_translate("SeleccionConexion", "¿Cómo querés conectar a Ayase?"))
        self.radioApiKey.setText(_translate("SeleccionConexion", "Usar API Key de OpenAI"))
        self.radioChatGPTWeb.setText(_translate("SeleccionConexion", "Usar ChatGPT Web (Plus o gratis)"))
        self.inputApiKey.setPlaceholderText(_translate("SeleccionConexion", "Pegá tu API Key acá"))
        self.botonTema.setText(_translate("SeleccionConexion", "🌙"))
        self.botonTema.setToolTip(_translate("SeleccionConexion", "Cambiar tema"))
        self.botonContinuar.setText(_translate("SeleccionConexion", "Continuar"))
