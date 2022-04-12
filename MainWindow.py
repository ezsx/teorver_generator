#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

import main_logic
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QPalette, QColor



class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def dark(self):
        dark_palette = QtGui.QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        return dark_palette

    def initUI(self):

        #добавляем 2 кнопки
        btn1 = QPushButton("generator", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
        #конектим функции к кнопкам
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        #ставим темную тему
        self.setPalette(self.dark())
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text()+main_logic())

# инициализация
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())