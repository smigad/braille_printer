######################################################  Braille Printer v2.0 ######################################################
__author__ = "elias"

import sys
from brailleprinter import Ui_MainWindow
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore, Qt
import time
from preview import *
import ntpath
import serial
import subprocess
import os

class App(QtGui.QMainWindow, Ui_MainWindow):

	# To Make it avaliable for the cancel button action and file open Action
	__directoryPath = ''
	__FileType = 'Text Files (*.txt)'
	__DefaultPath = "/home"

	def __init__(self, parent=None):

		super(App, self).__init__(parent)

		self.UI = Ui_MainWindow()
		self.UI.setupUi(self)

		#Button
		self.UI.Status.setStyleSheet("QLabel { color: red; }")
		self.UI.OpenButton.clicked.connect(lambda : self.OpenButton_Action(self.UI.OpenButton))
		self.UI.PreviewButton.clicked.connect(lambda : self.PreviewButton_Action(self.UI.PrintButton))
		self.UI.PrintButton.clicked.connect(lambda : self.PrintButton_Action(self.UI.PrintButton))
		self.UI.CancelButton.clicked.connect(lambda : self.CancelButton_Action(self.UI.CancelButton))
        # if os.listdir('/dev/').count('ttyACM0') != 0:
        #     self.UI.Status.setText("Connected")
        #     self.UI.Status.setStyleSheet("QLabel { color: green; }")
        # else:
        #     self.UI.Status.setText("Disconnected")
        #     self.UI.Status.setStyleSheet("QLabel { color: red; }")


	# used to Display Message Boxss
	def DisplayMessage(self, kind):
		if kind == 'PrintSuccess':
			QMessageBox.information(self, 'Print', "Print Successful!", QMessageBox.Ok)

		elif kind == 'Cancel':
			return QMessageBox.question(self, 'Cancel', "Are You Sure You Want to Cancel?", QMessageBox.Yes | QMessageBox.No)

		elif kind == 'Print':
			return QMessageBox.question(self, 'Print', "Are You Sure You Want to Print {} ?".format(ntpath.basename(str(self.__directoryPath))), QMessageBox.Yes | QMessageBox.No)

    # Open Button Action
	def OpenButton_Action(self, OpenBtn):
		self.__directoryPath = QFileDialog.getOpenFileName(self, "Open File", self.__DefaultPath, self.__FileType)
		print "From File Opener: " + self.__directoryPath
		try:
			File = open(self.__directoryPath, 'r')
		except IOError as e:
			error = "Could Not Open File: " + str(e)
			print error
		else:
			with File:
				text = File.read()
				self.UI.TextArea.setText(text)

	def updateStatusLabel(self, changeTo):
		if changeTo == 'connect':
			self.UI.Status.setText("Connected")
			self.UI.Status.setStyleSheet("QLabel { color: green; }")
		else:
			self.UI.Status.setText("Disconnected")
			self.UI.Status.setStyleSheet("QLabel { color: red; }")

	# Preview Button Action
	def PreviewButton_Action(self, PreviewBtn):
		if self.UI.TextArea.toPlainText() == "" or self.__directoryPath == "":
			print "Nothing to show!"
		else:
			print "Preview Button Clicked!"
			self.updateStatusLabel('connect')
			test(self.__directoryPath)

    # Print Button Action
	def PrintButton_Action(self, PrintBtn):
		if self.UI.TextArea.toPlainText() == "" or self.__directoryPath == "":
			print "File Not Selected!"
		else:
			choice = self.DisplayMessage('Print')
			if choice == QMessageBox.Yes:
				print "Printing......."
                subprocess.call(['/home/dagiopia/Documents/Braille Printer/git_repo/Software/Main/braille_celler', self.__directoryPath])
                self.s_port = serial.Serial('/dev/ttyACM0')
                f = open('output__file')
                str = f.readlines()[0]
                self.s_port.write(str)
                #print output

    # Cancel Button Action
	def CancelButton_Action(self, CancelBtn):
		if self.UI.TextArea.toPlainText() == "" or self.__directoryPath == "":
			print "Cancel Button Clicked!"
		else:
			choice = self.DisplayMessage('Cancel')
			if choice == QMessageBox.Yes:
				self.UI.TextArea.setText("")
				self.__directoryPath = ""
				print "Cancel Successfully!" + self.__directoryPath
			else:
				print "Doing Nothing with the Cancel Button!"

def main():
   app = QApplication(sys.argv)
   ex = App()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':main()
