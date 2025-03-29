from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtWidgets
from interfaz.chat_ui import Ui_MainWindow
from interfaz.tema import aplicar_tema
from openai import OpenAI, OpenAIError

class AyaseApp(QMainWindow):
    def __init__(self, api_key=None, tema_claro=True, volver=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tema_claro = tema_claro
        self.api_key = api_key
        self.volver_a = volver
        self.mensajes = []
        self.ui.inputMensaje.keyPressEvent = self.keyPressEventPersonalizado


        aplicar_tema(self, self.tema_claro, self.ui.botonTema)

        # Configurar selector de modelo
        self.ui.comboModelo.addItems(["gpt-3.5-turbo", "gpt-4"])
        self.modelo_actual = "gpt-3.5-turbo"
        self.ui.comboModelo.currentTextChanged.connect(self.cambiar_modelo)

        # Conectar botones
        self.ui.botonEnviar.clicked.connect(self.enviar_mensaje)
        self.ui.botonAtras.clicked.connect(self.volver)
        self.ui.botonTema.clicked.connect(self.cambiar_tema)

        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None

    def keyPressEventPersonalizado(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            if event.modifiers() == QtCore.Qt.ShiftModifier:
                self.ui.inputMensaje.insertPlainText("\n")
            else:
                self.enviar_mensaje()
        else:
            QtWidgets.QTextEdit.keyPressEvent(self.ui.inputMensaje, event)


    def cambiar_modelo(self, modelo):
        self.modelo_actual = modelo

    def enviar_mensaje(self):
        mensaje = self.ui.inputMensaje.toPlainText().strip()
        if not mensaje:
            return

        self.ui.chatArea.append(f"Tú: {mensaje}")
        self.ui.inputMensaje.clear()

        if not self.client:
            self.ui.chatArea.append("Ayase: [Error: No hay conexión a la API]")
            return

        self.mensajes.append({"role": "user", "content": mensaje})

        try:
            respuesta = self.client.chat.completions.create(
                model=self.modelo_actual,
                messages=self.mensajes
            )
            contenido = respuesta.choices[0].message.content.strip()
            self.ui.chatArea.append(f"Ayase: {contenido}")
            self.mensajes.append({"role": "assistant", "content": contenido})
        except OpenAIError as e:
            self.ui.chatArea.append(f"Ayase: [Error: {str(e)}]")
            print(f"[DEBUG] Error OpenAI: {e}")

    def cambiar_tema(self):
        self.tema_claro = not self.tema_claro
        aplicar_tema(self, self.tema_claro, self.ui.botonTema)

    def volver(self):
        if self.volver_a:
            self.volver_a.show()
        self.close()
