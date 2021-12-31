import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic import loadUi
from main import Ui_Form_1

class login(QDialog):
	def __init__(self):
		super(login,self).__init__()
		loadUi("login.ui",self)
		self.loginbutton.clicked.connect(self.openWindow1)
		self.password.setEchoMode(QtWidgets.QLineEdit.Password)
		self.username.setPlaceholderText("              Username")
		self.password.setPlaceholderText("              Password")
	def openWindow1(self):
		userName=self.username.text()
		passWord=self.password.text()
		if userName=="admin" and passWord=="admin":
			self.window = QtWidgets.QWidget()
			self.ui = Ui_Form_1()
			self.ui.setupUi(self.window)
			self.window.show()
			widget.close()
		else:
			msg = QMessageBox()
			msg.setText("Wrong name or password")
			msg.setIcon(QMessageBox.Critical)
			msg.setWindowTitle("Error")
			msg.exec_()


app=QApplication(sys.argv)
mainWindow=login()
widget=QtWidgets.QStackedWidget()
widget.setFixedWidth(900)
widget.setFixedHeight(1200)
widget.setWindowTitle("Login")
widget.addWidget(mainWindow)
widget.show()
app.exec_()