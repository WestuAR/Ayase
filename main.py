import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from ayase_ui import Ui_MainWindow


class AyaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Leer tema guardado
        self.tema_claro = self.leer_configuracion()
        
        # Aplicar tema inicial
        if self.tema_claro:
            self.aplicar_tema_claro()
            self.ui.botonTema.setText("🌙")
        else:
            self.aplicar_tema_oscuro()
            self.ui.botonTema.setText("☀️")

        # Conectar botones
        self.ui.botonTema.clicked.connect(self.cambiar_tema)
        self.ui.botonEnviar.clicked.connect(self.enviar_mensaje)

    def leer_configuracion(self):
        if not os.path.exists("config.txt"):
            return True  # Si no hay config, modo claro por defecto
        with open("config.txt", "r") as f:
            return f.read().strip() == "claro"

    def guardar_configuracion(self):
        with open("config.txt", "w") as f:
            f.write("claro" if self.tema_claro else "oscuro")

    def cambiar_tema(self):
        if self.tema_claro:
            self.aplicar_tema_oscuro()
            self.ui.botonTema.setText("☀️")
        else:
            self.aplicar_tema_claro()
            self.ui.botonTema.setText("🌙")
        self.tema_claro = not self.tema_claro
        self.guardar_configuracion()

    def aplicar_tema_claro(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                color: #000000;
                font-family: 'Helvetica Neue';
            }
            QTextEdit, QLineEdit {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton {
                background-color: #e0e0e0;
                border: none;
                border-radius: 8px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """)

    def aplicar_tema_oscuro(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #d4d4d4;
                font-family: 'Helvetica Neue';
            }
            QTextEdit, QLineEdit {
                background-color: #2e2e2e;
                border: 1px solid #555;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton {
                background-color: #3c3c3c;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
        """)

    def enviar_mensaje(self):
        texto = self.ui.inputMensaje.text()
        if texto.strip() == "":
            return
        self.ui.chatArea.append(f"Tú: {texto}")
        self.ui.chatArea.append("Ayase: (respuesta futura de la IA)\n")
        self.ui.inputMensaje.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AyaseApp()
    ventana.setWindowTitle("Ayase")
    ventana.show()
    sys.exit(app.exec_())