######################################################  Braille Printer v1.0 ######################################################
__author__ = "elias"

import sys
from BraillePrinterUI import Ui_BraillePrinter
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore, Qt
import serial
import time

class App(QtGui.QMainWindow, Ui_BraillePrinter):
    
    # To Make it avaliable for the cancel button action and file open Action
    __directoryPath = ''
    __FullScreen = False
    __FileType = 'Text Files (*.txt)'
    __DefaultPath = "/home"

    def __init__(self, parent=None):

        super(App, self).__init__(parent)

        #self.SerialData = serial.Serial("COM3", 9600, timeout=0)

        self.UI = Ui_BraillePrinter()
        self.UI.setupUi(self)

        #Print And Cancel Button
        self.UI.Cancel.clicked.connect(lambda : self.Cancel_btn(self.UI.Cancel))
        self.UI.Print.clicked.connect(lambda : self.Print_btn(self.UI.Print))

        #File Menu Bar
        self.UI.actionOpen_File.triggered.connect(lambda : self.Menu(self.UI.actionOpen_File))
        self.UI.actionPrint_File.triggered.connect(lambda : self.Menu(self.UI.actionPrint_File))
        self.UI.actionExit.triggered.connect(lambda : self.Menu(self.UI.actionExit))

        #File Window Bar
        self.UI.actionChange_Color.triggered.connect(lambda : self.Menu(self.UI.actionChange_Color))
        self.UI.actionChange_Font.triggered.connect(lambda : self.Menu(self.UI.actionChange_Font))
        self.UI.actionChange_Text_Color.triggered.connect(lambda : self.Menu(self.UI.actionChange_Text_Color))
        self.UI.actionFull_Screen.triggered.connect(lambda : self.Menu(self.UI.actionFull_Screen))


        #File Help Bar
        self.UI.actionHelp.triggered.connect(lambda : self.Menu(self.UI.actionHelp))
        self.UI.actionAbout.triggered.connect(lambda : self.Menu(self.UI.actionAbout))

    # used to Display Message Boxss
    def DisplayMessage(self, kind):
      if kind == 'Exit':
        return QMessageBox.question(self, 'Exit', 
                                          "Are you sure you want to Exit?",
                                          QMessageBox.Yes | QMessageBox.No )

      elif kind == 'Help':
        QMessageBox.information(self, 'Help', 
                                      "Help Page about the Braille Printer!",
                                      QMessageBox.Ok )

      elif kind == 'About':
        QMessageBox.information(self, 'About Braille Printer V1.0', 
                                      "Version 1.0", 
                                      QMessageBox.Ok )

      elif kind == 'PrintSuccess':
        QMessageBox.information(self, 'Print', 
                                      "Print Successful!", 
                                      QMessageBox.Ok )

      elif kind == 'Cancel':
        return QMessageBox.question(self, 'Cancel', 
                                          "Are You Sure You Want to Cancel?",
                                          QMessageBox.Yes | QMessageBox.No)

      elif kind == 'Print':
        return QMessageBox.question(self, 'Print', 
                                          "Are You Sure You Want to Print {} ?".format(str(self.__directoryPath)),
                                          QMessageBox.Yes | QMessageBox.No)

    # Cancel Button Action 
    def Cancel_btn(self, CancelBtn):
      if self.UI.TextEditer.toPlainText() == "" or self.__directoryPath == "":
        #self.SerialData.write('0')
        print "Cancel Button Clicked!"
        pass
      else:
        choice = self.DisplayMessage('Cancel')
        if choice == QMessageBox.Yes:
          #self.SerialData.write('0')
          self.UI.TextEditer.setText("")
          self.__directoryPath = ""
          self.UI.progressBar.setProperty("value", 0)
          print "Cancel Successfully!" + self.__directoryPath
        else:
          ##self.SerialData.write('0')
          print "Doing Nothing with the Cancel Button!"
          pass

    # Print Button Action
    def Print_btn(self, PrintBtn):
      if self.UI.TextEditer.toPlainText() == "" or self.__directoryPath == "":
        #self.SerialData.write('1')
        print "Print Button Clicked!"
        pass
      else:
        #self.SerialData.write('1')
        self.DisplayMessage('PrintSuccess')
         

    # MenuBar Action
    def Menu(self, MenuBtn):

      if MenuBtn.text() == "Open File":

        print "Open File Button Clicked!"
        self.__directoryPath = QFileDialog.getOpenFileName(self, "Open File", self.__DefaultPath, self.__FileType)
        print "From File Opener: " + self.__directoryPath
        try:
          File = open(self.__directoryPath, 'r')
        except IOError as e:
          error = "Could Not Open File: " + str(e)
          print error
        else:
          self.completed = 0
          with File:
            text = File.read()
            self.UI.TextEditer.setText(text)
          while self.completed < 100:
            self.completed += 0.1
            self.UI.progressBar.setProperty("value", self.completed)    

      elif MenuBtn.text() == "Print File":
        #self.SerialData.write('1')
        time.sleep(5600)
        self.DisplayMessage('PrintSuccess')
        print "Print Button Clicked!" 

      elif MenuBtn.text() == "Exit":
        choice = self.DisplayMessage('Exit')
        if choice == QMessageBox.Yes:
          print "App Successfully Quited!"
          #self.SerialData.write('0')
          #self.SerialData.close()
          qApp.quit()
        else:
          pass

      elif MenuBtn.text() == "Change Color":
        Color = QColorDialog.getColor()
        self.UI.Print.setStyleSheet("QPushButton { background-color: %s; }" % Color.name())
        self.UI.TextEditer.setStyleSheet("QTextEdit { background-color: %s; }" % Color.name())
        # self.UI.Cancel.setFont(font)
        print "Change Color Button Clicked!"

      elif MenuBtn.text() == "Change Font":
        font, valid = QFontDialog.getFont()
        if valid:
          self.UI.Print.setFont(font)
          self.UI.Cancel.setFont(font)
          self.UI.TextEditer.setFont(font)
        print "Change Font Button Clicked!"

      elif MenuBtn.text() == "Change Text Color":
        Color = QColorDialog.getColor()
        self.UI.Print.setStyleSheet("QPushButton { color: %s; }" % Color.name())
        self.UI.TextEditer.setStyleSheet("QTextEdit { color: %s; }" % Color.name())
        print "Change Text Color Button Clicked!"

      elif MenuBtn.text() == "Full Screen":
        if self.__FullScreen == False:
          self.showMaximized()
          self.__FullScreen = True
          print "Full Screen Activated!"
        else:
          pass
          self.__FullScreen = False
          print "Full Screen Deactivated!"

      elif MenuBtn.text() == "Help":
        self.DisplayMessage('Help')
        print "Help Button Clicked!"

      elif MenuBtn.text() == "About":
        self.DisplayMessage('About')
        print "About Button Clicked!"
        



def main():
   app = QApplication(sys.argv)
   ex = App()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':main()


