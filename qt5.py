from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QTableWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Train_window(QWidget):

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

        self.pushButton.clicked.connect(self.gen_table)

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

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Train data')
        self.show()

    def gen_table(self):
        self.hide()
        col = int(self.lineEdit_1.text()) + 1
        row = int(self.lineEdit.text()) + 1
        print('row:{}, col:{}'.format(row, col))
        train_data = Train_data(row, col)
        train_data.show()

class Train_data(QWidget):

    def __init__(self, row, col):
        super().__init__()

        self.initUI(row, col)

    def initUI(self, row, col):      

        self.table = QTableWidget()
        self.table.setRowCount(row)
        self.table.setColumnCount(col)

        # hbox = QHBoxLayout()
        # hbox.addWidget(self.pushButton_2)
        # hbox.addWidget(self.pushButton_3)

        # h_line = QHBoxLayout()
        # h_line.addWidget(self.lineEdit)
        # h_line.addWidget(self.lineEdit_2)

        # vbox = QVBoxLayout()
        # vbox.addLayout(hbox)
        # vbox.addLayout(h_line)
        # vbox.addWidget(self.pushButton)

        # self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Train data')
        # self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Train_window()
    sys.exit(app.exec_())