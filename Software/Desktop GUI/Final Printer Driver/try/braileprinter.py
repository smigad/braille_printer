# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'braileprinter.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(515, 490)
        Form.setMinimumSize(QtCore.QSize(515, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setMargin(10)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 5, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 4, 1, 1)
        self.ChooseFileLabel = QtGui.QLabel(Form)
        self.ChooseFileLabel.setMaximumSize(QtCore.QSize(69, 27))
        self.ChooseFileLabel.setObjectName(_fromUtf8("ChooseFileLabel"))
        self.gridLayout.addWidget(self.ChooseFileLabel, 2, 0, 1, 1)
        self.TextEdit = QtGui.QTextEdit(Form)
        self.TextEdit.setObjectName(_fromUtf8("TextEdit"))
        self.gridLayout.addWidget(self.TextEdit, 1, 0, 1, 6)
        self.StatusLabel = QtGui.QLabel(Form)
        self.StatusLabel.setMaximumSize(QtCore.QSize(68, 12))
        self.StatusLabel.setTextFormat(QtCore.Qt.AutoText)
        self.StatusLabel.setObjectName(_fromUtf8("StatusLabel"))
        self.gridLayout.addWidget(self.StatusLabel, 0, 5, 1, 1, QtCore.Qt.AlignRight)
        self.FileOpenerButton = QtGui.QPushButton(Form)
        self.FileOpenerButton.setMaximumSize(QtCore.QSize(143, 27))
        self.FileOpenerButton.setAutoDefault(False)
        self.FileOpenerButton.setObjectName(_fromUtf8("FileOpenerButton"))
        self.gridLayout.addWidget(self.FileOpenerButton, 2, 1, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setMaximumSize(QtCore.QSize(85, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.DeviceStatus = QtGui.QLabel(Form)
        self.DeviceStatus.setMaximumSize(QtCore.QSize(75, 12))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DeviceStatus.setFont(font)
        self.DeviceStatus.setObjectName(_fromUtf8("DeviceStatus"))
        self.gridLayout.addWidget(self.DeviceStatus, 0, 4, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Print", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.pushButton_2.setShortcut(_translate("Form", "Ctrl+C", None))
        self.pushButton.setText(_translate("Form", "Print", None))
        self.pushButton.setShortcut(_translate("Form", "Ctrl+P", None))
        self.ChooseFileLabel.setText(_translate("Form", "Choose File:", None))
        self.StatusLabel.setText(_translate("Form", "Disconnected", None))
        self.FileOpenerButton.setText(_translate("Form", "Open", None))
        self.FileOpenerButton.setShortcut(_translate("Form", "Ctrl+O", None))
        self.pushButton_3.setText(_translate("Form", "Preview", None))
        self.pushButton_3.setShortcut(_translate("Form", "Ctrl+W", None))
        self.DeviceStatus.setText(_translate("Form", "Device Status:", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BraillePrinter = QtGui.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(BraillePrinter)
    BraillePrinter.show()
    sys.exit(app.exec_())