# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brailleprintergui.ui'
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

class Ui_Print(object):
    def setupUi(self, Print):
        Print.setObjectName(_fromUtf8("Print"))
        Print.resize(510, 490)
        Print.setMinimumSize(QtCore.QSize(510, 490))
        Print.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Print.setWindowIcon(icon)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Print)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.DeviceStatus = QtGui.QLabel(Print)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeviceStatus.setFont(font)
        self.DeviceStatus.setObjectName(_fromUtf8("DeviceStatus"))
        self.horizontalLayout_3.addWidget(self.DeviceStatus)
        self.Status = QtGui.QLabel(Print)
        self.Status.setObjectName(_fromUtf8("Status"))
        self.horizontalLayout_3.addWidget(self.Status)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.TextArea = QtGui.QTextBrowser(Print)
        self.TextArea.setObjectName(_fromUtf8("TextArea"))
        self.verticalLayout.addWidget(self.TextArea)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ChooseFile = QtGui.QLabel(Print)
        self.ChooseFile.setObjectName(_fromUtf8("ChooseFile"))
        self.horizontalLayout_2.addWidget(self.ChooseFile)
        self.OpenButton = QtGui.QPushButton(Print)
        self.OpenButton.setObjectName(_fromUtf8("OpenButton"))
        self.horizontalLayout_2.addWidget(self.OpenButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.PreviewButton = QtGui.QPushButton(Print)
        self.PreviewButton.setObjectName(_fromUtf8("PreviewButton"))
        self.horizontalLayout.addWidget(self.PreviewButton)
        self.PrintButton = QtGui.QPushButton(Print)
        self.PrintButton.setObjectName(_fromUtf8("PrintButton"))
        self.horizontalLayout.addWidget(self.PrintButton)
        self.CancelButton = QtGui.QPushButton(Print)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Print)
        QtCore.QMetaObject.connectSlotsByName(Print)

    def retranslateUi(self, Print):
        Print.setWindowTitle(_translate("Print", "Print", None))
        self.DeviceStatus.setText(_translate("Print", "Device Status:", None))
        self.Status.setText(_translate("Print", "Disconnected", None))
        self.ChooseFile.setText(_translate("Print", "Choose File:", None))
        self.OpenButton.setText(_translate("Print", "Open", None))
        self.PreviewButton.setText(_translate("Print", "Preview", None))
        self.PrintButton.setText(_translate("Print", "Print", None))
        self.CancelButton.setText(_translate("Print", "Cancel", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BraillePrinter = QtGui.QMainWindow()
    ui = Ui_Print()
    ui.setupUi(BraillePrinter)
    BraillePrinter.show()
    sys.exit(app.exec_())