from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import sys
import numpy as np

class Train_window(QWidget):
    # sig = pyqtSignal()

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

        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        
        self.pushButton.setText("确认")
        self.pushButton_1.setText("类别数")
        self.pushButton_2.setText("训练样本数")
        self.pushButton_3.setText("维度")
        self.lineEdit.setText("10")
        self.lineEdit_1.setText("2")
        self.lineEdit_2.setText("2")

        self.pushButton_7.setText("确认")
        self.pushButton_4.setText("测试样本数")
        self.pushButton_5.setText("维度")
        self.pushButton_6.setText("类别数")
        self.lineEdit_4.setText("10")
        self.lineEdit_5.setText("2")
        self.lineEdit_6.setText("2")

        hbox = QHBoxLayout()
        hbox.addWidget(self.pushButton_2)
        hbox.addWidget(self.pushButton_3)
        hbox.addWidget(self.pushButton_1)

        h_line = QHBoxLayout()
        h_line.addWidget(self.lineEdit)
        h_line.addWidget(self.lineEdit_2)
        h_line.addWidget(self.lineEdit_1)

        h_1_box = QHBoxLayout()
        h_1_box.addWidget(self.pushButton_4)
        h_1_box.addWidget(self.pushButton_5)
        h_1_box.addWidget(self.pushButton_6)

        h_line_test = QHBoxLayout()
        h_line_test.addWidget(self.lineEdit_4)
        h_line_test.addWidget(self.lineEdit_5)
        h_line_test.addWidget(self.lineEdit_6)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h_line)
        vbox.addWidget(self.pushButton)
        vbox.addLayout(h_1_box)
        vbox.addLayout(h_line_test)
        vbox.addWidget(self.pushButton_7)

        self.pushButton.clicked.connect(self.gen_table)
        self.pushButton_7.clicked.connect(self.gen_table)
        # self.sig.connect(self.gen_table)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Train data')
        self.show()

    # def slot_btn(self):
    #     self.sig.emit()

    def gen_table(self):
        
        col = int(self.lineEdit_2.text()) + 1
        row = int(self.lineEdit.text())
        label = int(self.lineEdit_1.text())
        print('row:{}, col:{}'.format(row, col))
        self.train_data = Train_data(row, col, label)

        self.train_data.show()

class Train_data(QWidget):

    def __init__(self, row, col, label):
        super().__init__()
        
        self.row = row
        self.col = col
        self.label = label
        self.initUI(row, col, label)

    def initUI(self, row, col, label):      

        self.table = QTableWidget(self)
        self.button = QPushButton(self)

        self.table.setRowCount(row)
        self.table.setColumnCount(col)
        self.button.setText("确认")
        self.button.clicked.connect(self.save_text)

        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

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
        
        for i in range(row):
            for j in range(col):
                if j != col - 1:
                    rand_num = str(np.random.rand())[:5]
                    self.table.setItem(i,j, QTableWidgetItem(rand_num))
                else:
                    label_str = str(np.random.randint(label))
                    self.table.setItem(i,j, QTableWidgetItem(label_str))

        self.setLayout(vbox)
        self.setGeometry(800, 300, 1000, 500)
        self.setWindowTitle('Train data')
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.show()

    def save_text(self):
        arr = np.empty((self.row, self.col))
        for i in range(self.row):
            for j in range(self.col):
                val = self.table.item(i, j)
                arr[i, j] = float(val.text())

        print(arr)
        np.savetxt("traindata.csv", arr, delimiter=",", fmt="%.4f,%.4f,%d")
        self.dialog = Dialog()
        self.dialog.show()

class Dialog(QDialog):

    def __init__(self):
        super().__init__()

        self.resize(100, 100)
        self.label = QtWidgets.QLabel(self)
        self.label.setText('保存成功')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label)
        hbox.addStretch(1)

        # vbox = QVBoxLayout()
        # vbox.addLayout(hbox)
        self.setLayout(hbox)
        self.setWindowTitle('Data')
        self.setWindowModality(QtCore.Qt.ApplicationModal)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Train_window()
    sys.exit(app.exec_())