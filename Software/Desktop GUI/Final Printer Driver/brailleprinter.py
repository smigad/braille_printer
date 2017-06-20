# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brailleprinter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(510, 490)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(510, 490))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.DeviceStatus = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeviceStatus.setFont(font)
        self.DeviceStatus.setObjectName(_fromUtf8("DeviceStatus"))
        self.horizontalLayout_3.addWidget(self.DeviceStatus)
        self.Status = QtGui.QLabel(self.centralwidget)
        self.Status.setObjectName(_fromUtf8("Status"))
        self.horizontalLayout_3.addWidget(self.Status)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.TextArea = QtGui.QTextBrowser(self.centralwidget)
        self.TextArea.setObjectName(_fromUtf8("TextArea"))
        self.verticalLayout.addWidget(self.TextArea)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ChooseFile = QtGui.QLabel(self.centralwidget)
        self.ChooseFile.setObjectName(_fromUtf8("ChooseFile"))
        self.horizontalLayout_2.addWidget(self.ChooseFile)
        self.OpenButton = QtGui.QPushButton(self.centralwidget)
        self.OpenButton.setObjectName(_fromUtf8("OpenButton"))
        self.horizontalLayout_2.addWidget(self.OpenButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.PreviewButton = QtGui.QPushButton(self.centralwidget)
        self.PreviewButton.setObjectName(_fromUtf8("PreviewButton"))
        self.horizontalLayout.addWidget(self.PreviewButton)
        self.PrintButton = QtGui.QPushButton(self.centralwidget)
        self.PrintButton.setObjectName(_fromUtf8("PrintButton"))
        self.horizontalLayout.addWidget(self.PrintButton)
        self.CancelButton = QtGui.QPushButton(self.centralwidget)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Print", None))
        self.DeviceStatus.setText(_translate("MainWindow", "Device Status:", None))
        self.Status.setText(_translate("MainWindow", "Disconnected", None))
        self.ChooseFile.setText(_translate("MainWindow", "Choose File:", None))
        self.OpenButton.setText(_translate("MainWindow", "Open", None))
        self.OpenButton.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.PreviewButton.setText(_translate("MainWindow", "Preview", None))
        self.PreviewButton.setShortcut(_translate("MainWindow", "Ctrl+W", None))
        self.PrintButton.setText(_translate("MainWindow", "Print", None))
        self.PrintButton.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.CancelButton.setText(_translate("MainWindow", "Cancel", None))
        self.CancelButton.setShortcut(_translate("MainWindow", "Ctrl+C", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BraillePrinter = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(BraillePrinter)
    BraillePrinter.show()
    sys.exit(app.exec_())