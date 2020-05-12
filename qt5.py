from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):      

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(290, 300, 100, 50))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(230, 240, 100, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 170, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 170, 100, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 240, 100, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton.setText("确认")
        self.pushButton_2.setText("样本数")
        self.pushButton_3.setText("维度")

        hbox = QHBoxLayout()
        hbox.addWidget(self.pushButton_2)
        hbox.addWidget(self.pushButton_3)

        h_line = QHBoxLayout()
        h_line.addWidget(self.lineEdit)
        h_line.addWidget(self.lineEdit_2)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h_line)
        vbox.addWidget(self.pushButton)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('QCheckBox')
        self.show()
   

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())