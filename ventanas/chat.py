from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication
from PyQt5 import QtCore, QtWidgets
from interfaz.chat_ui import Ui_MainWindow
from interfaz.tema import aplicar_tema
from openai import OpenAI
import os

def interpretar_error_openai(error):
    try:
        status = error.response.status_code
        detalle = error.response.json()
        mensaje = detalle.get("error", {}).get("message", "")
        tipo = detalle.get("error", {}).get("type", "")
        codigo = detalle.get("error", {}).get("code", "")
    except Exception:
        return "Ayase: Se produjo un error inesperado al intentar comunicarme con OpenAI."

    if status == 401:
        return "Ayase: Tu API Key parece ser inválida. Verificá que esté bien escrita, cielo 😅"
    elif status == 403:
        return "Ayase: Tu cuenta no tiene permiso para acceder a esta función. Revisá tu cuenta o región 😔"
    elif status == 429:
        if codigo == "billing_not_active":
            return "Ayase: Tu cuenta no tiene un plan activo. Revisá tu facturación en OpenAI 💸"
        elif tipo == "rate_limit_exceeded":
            return "Ayase: Estás enviando muchas solicitudes muy rápido. Tomate un respiro 😉"
        else:
            return "Ayase: No puedo procesar tu solicitud ahora. Probá dentro de un rato."
    elif status == 400:
        return "Ayase: Algo salió mal con el formato del mensaje. Podés intentar corregirlo ✍️"
    elif status in [500, 502, 503, 504]:
        return "Ayase: Los servidores de OpenAI están teniendo un mal día. Volvé más tarde 💔"

    return f"Ayase: Error inesperado ({status}): {mensaje}"

class AyaseApp(QMainWindow):
    def __init__(self, api_key=None, tema_claro=True, volver=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tema_claro = tema_claro
        self.api_key = api_key
        self.volver = volver

        aplicar_tema(self, self.tema_claro)

        self.ui.botonAtras.clicked.connect(self.volver_atras)
        self.ui.botonEnviar.clicked.connect(self.enviar_mensaje)

        self.ui.accionClaro.triggered.connect(self.tema_claro_manual)
        self.ui.accionOscuro.triggered.connect(self.tema_oscuro_manual)

        self.ui.inputMensaje.installEventFilter(self)

        # Modelos disponibles
        self.ui.comboModelo.addItems(["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"])
        self.ui.comboModelo.setCurrentIndex(0)

    def tema_claro_manual(self):
        self.tema_claro = True
        aplicar_tema(self, self.tema_claro)

    def tema_oscuro_manual(self):
        self.tema_claro = False
        aplicar_tema(self, self.tema_claro)

    def volver_atras(self):
        if self.volver:
            self.volver.show()
        self.close()

    def enviar_mensaje(self):
        mensaje = self.ui.inputMensaje.toPlainText().strip()
        if not mensaje:
            return

        self.ui.chatArea.append(f"Tú: {mensaje}")
        self.ui.inputMensaje.clear()

        if not self.api_key:
            self.ui.chatArea.append("Ayase: [Error: No hay conexión a la API]")
            return

        modelo = self.ui.comboModelo.currentText()

        try:
            cliente = OpenAI(api_key=self.api_key)
            respuesta = cliente.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": mensaje}],
                temperature=0.7,
            )
            contenido = respuesta.choices[0].message.content
            self.ui.chatArea.append(f"Ayase: {contenido}")

        except Exception as error:
            try:
                import openai
                if isinstance(error, openai.OpenAIError):
                    mensaje_error = interpretar_error_openai(error)
                else:
                    mensaje_error = f"Ayase: [Error desconocido] {str(error)}"
            except:
                mensaje_error = f"Ayase: [Error inesperado] {str(error)}"

            self.ui.chatArea.append(mensaje_error)

    def eventFilter(self, source, event):
        if source == self.ui.inputMensaje and event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                if event.modifiers() == QtCore.Qt.ShiftModifier:
                    return False  # Permitir salto de línea
                else:
                    self.enviar_mensaje()
                    return True  # Evita que se agregue salto de línea
        return super().eventFilter(source, event)
