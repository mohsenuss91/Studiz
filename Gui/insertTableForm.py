# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertTableForm.ui'
#
# Created: Sat Oct 09 17:14:17 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(162, 230)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.rowsLabel = QtGui.QLabel(Dialog)
        self.rowsLabel.setObjectName("rowsLabel")
        self.gridLayout.addWidget(self.rowsLabel, 0, 0, 1, 1)
        self.rowsSpinBox = QtGui.QSpinBox(Dialog)
        self.rowsSpinBox.setProperty("value", 2)
        self.rowsSpinBox.setObjectName("rowsSpinBox")
        self.gridLayout.addWidget(self.rowsSpinBox, 0, 1, 1, 1)
        self.columnsLabel = QtGui.QLabel(Dialog)
        self.columnsLabel.setObjectName("columnsLabel")
        self.gridLayout.addWidget(self.columnsLabel, 1, 0, 1, 1)
        self.columnsSpinBox = QtGui.QSpinBox(Dialog)
        self.columnsSpinBox.setProperty("value", 2)
        self.columnsSpinBox.setObjectName("columnsSpinBox")
        self.gridLayout.addWidget(self.columnsSpinBox, 1, 1, 1, 1)
        self.cellPaddingLabel = QtGui.QLabel(Dialog)
        self.cellPaddingLabel.setObjectName("cellPaddingLabel")
        self.gridLayout.addWidget(self.cellPaddingLabel, 2, 0, 1, 1)
        self.cellPaddingSpinBox = QtGui.QSpinBox(Dialog)
        self.cellPaddingSpinBox.setProperty("value", 5)
        self.cellPaddingSpinBox.setObjectName("cellPaddingSpinBox")
        self.gridLayout.addWidget(self.cellPaddingSpinBox, 2, 1, 1, 1)
        self.cellSpacingLabel = QtGui.QLabel(Dialog)
        self.cellSpacingLabel.setObjectName("cellSpacingLabel")
        self.gridLayout.addWidget(self.cellSpacingLabel, 3, 0, 1, 1)
        self.cellSpacingSpinBox = QtGui.QSpinBox(Dialog)
        self.cellSpacingSpinBox.setObjectName("cellSpacingSpinBox")
        self.gridLayout.addWidget(self.cellSpacingSpinBox, 3, 1, 1, 1)
        self.backgroundColorLabel = QtGui.QLabel(Dialog)
        self.backgroundColorLabel.setObjectName("backgroundColorLabel")
        self.gridLayout.addWidget(self.backgroundColorLabel, 4, 0, 1, 1)
        self.BGButton = QtGui.QPushButton(Dialog)
        self.BGButton.setText("")
        self.BGButton.setObjectName("BGButton")
        self.gridLayout.addWidget(self.BGButton, 4, 1, 1, 1)
        self.borderColorLabel = QtGui.QLabel(Dialog)
        self.borderColorLabel.setObjectName("borderColorLabel")
        self.gridLayout.addWidget(self.borderColorLabel, 5, 0, 1, 1)
        self.BorderButton = QtGui.QPushButton(Dialog)
        self.BorderButton.setText("")
        self.BorderButton.setObjectName("BorderButton")
        self.gridLayout.addWidget(self.BorderButton, 5, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Insert Table", None, QtGui.QApplication.UnicodeUTF8))
        self.rowsLabel.setText(QtGui.QApplication.translate("Dialog", "Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.columnsLabel.setText(QtGui.QApplication.translate("Dialog", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.cellPaddingLabel.setText(QtGui.QApplication.translate("Dialog", "CellPadding", None, QtGui.QApplication.UnicodeUTF8))
        self.cellSpacingLabel.setText(QtGui.QApplication.translate("Dialog", "CellSpacing", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundColorLabel.setText(QtGui.QApplication.translate("Dialog", "Background Color", None, QtGui.QApplication.UnicodeUTF8))
        self.borderColorLabel.setText(QtGui.QApplication.translate("Dialog", "Border Color", None, QtGui.QApplication.UnicodeUTF8))

