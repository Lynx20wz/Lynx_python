from PyQt6 import QtWidgets #Позволяет создавать виджеты
from PyQt6.QtWidgets import QApplication, QMainWindow #QApplication - приложение, QMainWindow - окно
#ожно приложение, но много окон в нём

import sys

def app():
    app = QApplication(sys.argv) #соаздание приложения в целом
    window = QMainWindow() #создание окна

    window.setWindowTitle('Focus manager') #Название сверху
    window.setGeometry(700,400,400,200) #отступ сверху, отступ снизу, и размеры: ширина, высота
    window.show() #показывание окна
    sys.exit(app.exec())

if __name__ == '__main__':
    app()