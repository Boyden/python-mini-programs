from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import sys

class Train_window(QWidget):
    sig = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):      

        self.pushButton = QtWidgets.QPushButton(self)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        
        self.pushButton.setText("确认")
        self.pushButton_1.setText("类别数")
        self.pushButton_2.setText("样本数")
        self.pushButton_3.setText("维度")
        self.lineEdit.setText("10")
        self.lineEdit_1.setText("2")
        self.lineEdit_2.setText("2")



        hbox = QHBoxLayout()
        hbox.addWidget(self.pushButton_2)
        hbox.addWidget(self.pushButton_3)
        hbox.addWidget(self.pushButton_1)

        h_line = QHBoxLayout()
        h_line.addWidget(self.lineEdit)
        h_line.addWidget(self.lineEdit_2)
        h_line.addWidget(self.lineEdit_1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h_line)
        vbox.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.slot_btn)
        self.sig.connect(self.gen_table)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Train data')
        self.show()

    def slot_btn(self):
        self.sig.emit()

    def gen_table(self):
        
        col = int(self.lineEdit_2.text()) + 1
        row = int(self.lineEdit.text())
        print('row:{}, col:{}'.format(row, col))
        self.train_data = Train_data(row, col)
        self.train_data.show()

class Train_data(QWidget):

    def __init__(self, row, col):
        super().__init__()

        self.initUI(row, col)

    def initUI(self, row, col):      

        self.table = QTableWidget(self)
        self.button = QPushButton(self)

        self.table.setRowCount(row)
        self.table.setColumnCount(col)
        self.button.setText("确认")
        self.button.clicked.connect(self.save_text)

        font = QFont('', 15)
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)
        
        headers = [str(i+1) for i in range(col-1)]
        headers.append("label")
        self.table.setHorizontalHeaderLabels(headers)
        hbox = QHBoxLayout()
        hbox.addWidget(self.table)
        hbox.addWidget(self.button)

        # h_line = QHBoxLayout()
        # h_line.addWidget(self.lineEdit)
        # h_line.addWidget(self.lineEdit_2)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        # vbox.addLayout(h_line)
        # vbox.addWidget(self.pushButton)

        self.setLayout(vbox)
        self.setGeometry(800, 300, 1000, 500)
        self.setWindowTitle('Train data')
        # self.show()

    def save_text(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Train_window()
    sys.exit(app.exec_())