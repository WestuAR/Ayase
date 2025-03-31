# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from config import VERSION, AUTOR, NOMBRE_APP

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.menuOpciones = QtWidgets.QMenu("Opciones", self.menubar)
        self.menuTema = self.menuOpciones.addMenu("Cambiar tema")
        self.accionClaro = QtWidgets.QAction("Claro", MainWindow)
        self.accionOscuro = QtWidgets.QAction("Oscuro", MainWindow)
        self.menuTema.addAction(self.accionClaro)
        self.menuTema.addAction(self.accionOscuro)
        self.menuAcerca = self.menuOpciones.addMenu("Acerca de")
        self.menuAcerca.addAction(f"{NOMBRE_APP} - Asistente Personal")
        self.menuAcerca.addAction(f"Versión: {VERSION}")
        self.menuAcerca.addAction(f"Autor: {AUTOR}")
        self.menuAcerca.addAction("Gracias por usar Ayase")
        self.menubar.addMenu(self.menuOpciones)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        # 🖼️ Título
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.labelTitulo, 0, 0, 1, 2)

        # 🔽 Splitter vertical (chat + input)
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(6)

        # 💬 Área del chat
        self.chatArea = QtWidgets.QTextEdit()
        self.chatArea.setReadOnly(True)
        self.chatArea.setMinimumHeight(30)
        self.splitter.addWidget(self.chatArea)

        # 📝 Input + Enviar en layout horizontal
        contenedorInput = QtWidgets.QWidget()
        contenedorInput.setMinimumHeight(30)
        hLayout = QtWidgets.QHBoxLayout(contenedorInput)
        hLayout.setContentsMargins(0, 0, 0, 0)

        self.inputMensaje = QtWidgets.QTextEdit()
        self.inputMensaje.setPlaceholderText("Escribí tu mensaje...")
        self.inputMensaje.setMinimumHeight(30)
        self.inputMensaje.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        hLayout.addWidget(self.inputMensaje)

        self.botonEnviar = QtWidgets.QPushButton("Enviar")
        self.botonEnviar.setMinimumHeight(30)
        self.botonEnviar.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        hLayout.addWidget(self.botonEnviar)

        self.splitter.addWidget(contenedorInput)

        # 🔒 ¡Evitar que se colapsen!
        self.splitter.setCollapsible(0, False)
        self.splitter.setCollapsible(1, False)

        self.splitter.setSizes([400, 100])  # proporción inicial

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 3)

        # 🔽 Selector de modelo
        self.comboModelo = QtWidgets.QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.comboModelo, 2, 0, 1, 1)

        # 🔙 Botón volver
        self.botonAtras = QtWidgets.QPushButton("← Volver", self.centralwidget)
        self.gridLayout.addWidget(self.botonAtras, 2, 2, 1, 1)

        # Distribución
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ayase - Asistente"))
        self.labelTitulo.setText(_translate("MainWindow", "Ayase - Asistente Personal"))
