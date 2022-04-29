from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(224, 241)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 100, 91, 61))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")

        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
#
        #self.plainTextEdit = QtWidgets.QPlainTextEdit(self.splitter)
        self.plainTextEdit = QtWidgets.QTextBrowser(self.splitter)

        self.plainTextEdit.setObjectName("plainTextEdit")

        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(20, 40, 181, 31))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")

#        self.textBrowser = QtWidgets.QTextBrowser(self.splitter_2)
        self.textBrowser = QtWidgets.QLineEdit(self.splitter_2)

        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setObjectName("label_3")

#        self.textBrowser_2 = QtWidgets.QTextBrowser(self.splitter_2)
        self.textBrowser_2 = QtWidgets.QLineEdit(self.splitter_2)

        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Суперпрограмма"))
        self.label.setText(_translate("MainWindow", "Сколько будет"))
        self.pushButton.setText(_translate("MainWindow", "Окей?"))
        self.label_2.setText(_translate("MainWindow", "Ответ:"))
        self.label_3.setText(_translate("MainWindow", "+"))
        self.label_4.setText(_translate("MainWindow", "?"))