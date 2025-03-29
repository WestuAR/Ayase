import os

def cargar_tema():
    if not os.path.exists("config.txt"):
        return True  # Tema claro por defecto
    with open("config.txt", "r") as f:
        for linea in f:
            if linea.strip().startswith("tema="):
                return linea.strip().split("=")[1] == "claro"
    return True

def guardar_tema(claro=True):
    with open("config.txt", "w") as f:
        f.write("tema=claro\n" if claro else "tema=oscuro\n")

def aplicar_tema(ventana, claro=True, boton=None):
    if claro:
        ventana.setStyleSheet("""
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
        if boton:
            boton.setText("🌙")
    else:
        ventana.setStyleSheet("""
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
        if boton:
            boton.setText("☀️")
