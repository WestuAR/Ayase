import sys
import os
import platform
from PyQt5.QtWidgets import QApplication, QWidget
from interfaz.main_ui import Ui_SeleccionConexion
from interfaz.tema import cargar_tema, guardar_tema, aplicar_tema
from ventanas.chat import AyaseApp
from cryptography.fernet import Fernet

class VentanaSeleccion(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SeleccionConexion()
        self.ui.setupUi(self)

        self.modo = None
        self.api_key = None
        self.tema_claro = cargar_tema()

        self.ui.inputApiKey.setEchoMode(self.ui.inputApiKey.Password)
        self.ui.inputApiKey.setText(self.cargar_api_key_segura())
        self.ui.inputApiKey.mousePressEvent = self.limpiar_campo_api

        self.actualizar_visibilidad_api()
        aplicar_tema(self, self.tema_claro, self.ui.botonTema)

        # Conexiones
        self.ui.radioApiKey.toggled.connect(self.actualizar_visibilidad_api)
        self.ui.radioApiKey.toggled.connect(self.verificar_opcion_seleccionada)
        self.ui.radioChatGPTWeb.toggled.connect(self.verificar_opcion_seleccionada)
        self.ui.botonContinuar.clicked.connect(self.continuar)
        self.ui.botonTema.clicked.connect(self.cambiar_tema)

        # Iniciar con botón deshabilitado
        self.ui.botonContinuar.setEnabled(False)

    def showEvent(self, event):
        super().showEvent(event)
        self.ui.inputApiKey.mousePressEvent = self.limpiar_campo_api

    def actualizar_visibilidad_api(self):
        self.ui.inputApiKey.setVisible(self.ui.radioApiKey.isChecked())

    def verificar_opcion_seleccionada(self):
        if self.ui.radioApiKey.isChecked() or self.ui.radioChatGPTWeb.isChecked():
            self.ui.botonContinuar.setEnabled(True)
        else:
            self.ui.botonContinuar.setEnabled(False)

    def cambiar_tema(self):
        self.tema_claro = not self.tema_claro
        aplicar_tema(self, self.tema_claro, self.ui.botonTema)
        guardar_tema(self.tema_claro)

    def continuar(self):
        if self.ui.radioApiKey.isChecked():
            self.modo = "api"
            self.api_key = self.ui.inputApiKey.text().strip()
            self.guardar_api_key_segura(self.api_key)
        else:
            self.modo = "web"

        self.chat = AyaseApp(
            api_key=self.api_key if self.modo == "api" else None,
            tema_claro=self.tema_claro,
            volver=self
        )
        self.chat.show()
        self.hide()

    def limpiar_campo_api(self, event):
        self.ui.inputApiKey.clear()
        self.ui.inputApiKey.mousePressEvent = lambda e: QWidget.mousePressEvent(self.ui.inputApiKey, e)

    def ocultar_archivo(self, nombre_archivo):
        if platform.system() == "Windows":
            os.system(f'attrib +h "{nombre_archivo}"')

    def generar_clave(self):
        if not os.path.exists("clave.key"):
            with open("clave.key", "wb") as f:
                f.write(Fernet.generate_key())
            self.ocultar_archivo("clave.key")

    def cargar_clave(self):
        with open("clave.key", "rb") as f:
            return f.read()

    def guardar_api_key_segura(self, api_key):
        self.generar_clave()
        clave = self.cargar_clave()
        f = Fernet(clave)
        token = f.encrypt(api_key.encode())

        if os.path.exists(".apikey.txt"):
            os.chmod(".apikey.txt", 0o666)
            os.remove(".apikey.txt")

        with open(".apikey.txt", "wb") as archivo:
            archivo.write(token)

        self.ocultar_archivo(".apikey.txt")

    def cargar_api_key_segura(self):
        try:
            clave = self.cargar_clave()
            f = Fernet(clave)
            with open(".apikey.txt", "rb") as archivo:
                token = archivo.read()
            return f.decrypt(token).decode()
        except:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaSeleccion()
    ventana.show()
    sys.exit(app.exec_())
