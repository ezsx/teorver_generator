
import sys
# Импортируем наш интерфейс из файла
import design
from PyQt5 import QtCore, QtGui, QtWidgets

import main_logic


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = design.Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.myFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def myFunction(self):
        self.ui.plainTextEdit.setText(
            #str(int(self.ui.textBrowser.text())+int(self.ui.textBrowser_2.text())))
            main_logic.F())
        #pass

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())