

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_Form_12(object):
    def setupUi(self, Form_12):
        Form_12.setObjectName("Form_12")
        Form_12.resize(961, 1028)
        self.label_1 = QtWidgets.QLabel(Form_12)
        self.label_1.setGeometry(QtCore.QRect(-250, 0, 851, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form_12)
        self.label_2.setGeometry(QtCore.QRect(540, 130, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_12)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form_12)
        self.label_4.setGeometry(QtCore.QRect(560, 540, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form_12)
        self.label_5.setGeometry(QtCore.QRect(40, 540, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_5.setObjectName("label_5")
        self.tableWidget_9 = QtWidgets.QTableWidget(Form_12)
        self.tableWidget_9.setGeometry(QtCore.QRect(510, 200, 411, 321))
        self.tableWidget_9.setRowCount(8)
        self.tableWidget_9.setColumnCount(7)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_10 = QtWidgets.QTableWidget(Form_12)
        self.tableWidget_10.setGeometry(QtCore.QRect(20, 200, 411, 321))
        self.tableWidget_10.setRowCount(8)
        self.tableWidget_10.setColumnCount(7)
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_11 = QtWidgets.QTableWidget(Form_12)
        self.tableWidget_11.setGeometry(QtCore.QRect(500, 620, 451, 321))
        self.tableWidget_11.setRowCount(8)
        self.tableWidget_11.setColumnCount(7)
        self.tableWidget_11.setObjectName("tableWidget_11")
        self.tableWidget_12 = QtWidgets.QTableWidget(Form_12)
        self.tableWidget_12.setGeometry(QtCore.QRect(20, 620, 411, 321))
        self.tableWidget_12.setRowCount(8)
        self.tableWidget_12.setColumnCount(7)
        self.tableWidget_12.setObjectName("tableWidget_12")
        self.pushButton_40 = QtWidgets.QPushButton(Form_12)
        self.pushButton_40.setGeometry(QtCore.QRect(740, 530, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(Form_12)
        self.pushButton_41.setGeometry(QtCore.QRect(250, 540, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_43 = QtWidgets.QPushButton(Form_12)
        self.pushButton_43.setGeometry(QtCore.QRect(250, 950, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_42 = QtWidgets.QPushButton(Form_12)
        self.pushButton_42.setGeometry(QtCore.QRect(770, 950, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_40.clicked.connect(self.gettingCs)
        self.pushButton_42.clicked.connect(self.gettingIt)
        self.pushButton_41.clicked.connect(self.gettingSe)
        self.pushButton_43.clicked.connect(self.gettingIs)
        self.retranslateUi(Form_12)
        QtCore.QMetaObject.connectSlotsByName(Form_12)

    def retranslateUi(self, Form_12):
        _translate = QtCore.QCoreApplication.translate
        Form_12.setWindowTitle(_translate("Form_12", "Form"))
        self.label_1.setText(_translate("Form_12", "عرض النتائج"))
        self.label_2.setText(_translate("Form_12", "CS"))
        self.label_3.setText(_translate("Form_12", "SE"))
        self.label_4.setText(_translate("Form_12", "IT"))
        self.label_5.setText(_translate("Form_12", "IS"))
        self.pushButton_40.setText(_translate("Form_12", "عرض "))
        self.pushButton_41.setText(_translate("Form_12", "عرض "))
        self.pushButton_43.setText(_translate("Form_12", "عرض "))
        self.pushButton_42.setText(_translate("Form_12", "عرض "))
    def gettingCs(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='الرغبة الثالثة')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM cs ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget_9.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget_9.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget_9.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def gettingIs(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='الرغبة الثالثة')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM iss ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget_12.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget_12.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget_12.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def gettingIt(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='الرغبة الثالثة')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM it ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget_11.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget_11.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget_11.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def gettingSe(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='الرغبة الثالثة')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM se ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget_10.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget_10.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget_10.setItem(row_number, column_number, QTableWidgetItem(str(data)))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_12 = QtWidgets.QWidget()
    ui = Ui_Form_12()
    ui.setupUi(Form_12)
    Form_12.show()
    sys.exit(app.exec_())
