# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Form_11(object):
    def setupUi(self, Form_11):
        Form_11.setObjectName("Form_11")
        Form_11.resize(961, 1028)
        self.label_1 = QtWidgets.QLabel(Form_11)
        self.label_1.setGeometry(QtCore.QRect(-250, 0, 851, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form_11)
        self.label_2.setGeometry(QtCore.QRect(540, 130, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_11)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form_11)
        self.label_4.setGeometry(QtCore.QRect(560, 540, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form_11)
        self.label_5.setGeometry(QtCore.QRect(40, 540, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("Color: rgba(0, 83, 139, 1)\n"
"")
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(Form_11)
        self.tableWidget.setGeometry(QtCore.QRect(510, 200, 411, 321))
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget_2 = QtWidgets.QTableWidget(Form_11)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 200, 411, 321))
        self.tableWidget_2.setRowCount(8)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(Form_11)
        self.tableWidget_3.setGeometry(QtCore.QRect(500, 620, 451, 321))
        self.tableWidget_3.setRowCount(8)
        self.tableWidget_3.setColumnCount(7)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(Form_11)
        self.tableWidget_4.setGeometry(QtCore.QRect(20, 620, 411, 321))
        self.tableWidget_4.setRowCount(8)
        self.tableWidget_4.setColumnCount(7)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.pushButton_36 = QtWidgets.QPushButton(Form_11)
        self.pushButton_36.setGeometry(QtCore.QRect(740, 530, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(Form_11)
        self.pushButton_37.setGeometry(QtCore.QRect(250, 540, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_39 = QtWidgets.QPushButton(Form_11)
        self.pushButton_39.setGeometry(QtCore.QRect(250, 950, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_38 = QtWidgets.QPushButton(Form_11)
        self.pushButton_38.setGeometry(QtCore.QRect(770, 950, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setObjectName("pushButton_38")

        self.retranslateUi(Form_11)
        QtCore.QMetaObject.connectSlotsByName(Form_11)
        self.pushButton_36.clicked.connect(self.gettingCs)
        self.pushButton_38.clicked.connect(self.gettingIt)
        self.pushButton_37.clicked.connect(self.gettingSe)
        self.pushButton_39.clicked.connect(self.gettingIs)

    def retranslateUi(self, Form_11):
        _translate = QtCore.QCoreApplication.translate
        Form_11.setWindowTitle(_translate("Form_11", "Form"))
        self.label_1.setText(_translate("Form_11", "?????? ??????????????"))
        self.label_2.setText(_translate("Form_11", "CS"))
        self.label_3.setText(_translate("Form_11", "SE"))
        self.label_4.setText(_translate("Form_11", "IT"))
        self.label_5.setText(_translate("Form_11", "IS"))
        self.pushButton_36.setText(_translate("Form_11", "?????? "))
        self.pushButton_37.setText(_translate("Form_11", "?????? "))
        self.pushButton_39.setText(_translate("Form_11", "?????? "))
        self.pushButton_38.setText(_translate("Form_11", "?????? "))
    def gettingCs(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='???????????? ??????????????')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM cs ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def gettingIs(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='???????????? ??????????????')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM iss ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget_4.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget_4.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget_4.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def gettingIt(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='???????????? ??????????????')    
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM it ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget_3.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget_3.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget_3.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def gettingSe(self):
                mydb=mc.connect(
                                host='localhost',
                                user='root',
                                password='',
                                database='???????????? ??????????????')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM se ORDER BY GPA DESC LIMIT 4")
                result = cursor.fetchall()
                self.tableWidget_2.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget_2.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_11 = QtWidgets.QWidget()
    ui = Ui_Form_11()
    ui.setupUi(Form_11)
    Form_11.show()
    sys.exit(app.exec_())
