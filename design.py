import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton
from PyQt5.QtCore import Qt

import write_docx
def generate_doc():
    pass

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        button = QPushButton("OK", self)

        self.resize(800, 600)
        button.clicked.connect(generate_doc())

    def onOKClicked(self):
        dialog = QDialog()
        dialog.setWindowTitle("Dialog Demo")
        dialog.resize(300, 200)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())