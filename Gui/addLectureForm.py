# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addLectureForm.ui'
#
# Created: Sat Oct 30 15:07:49 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(307, 129)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.courseNameLabel = QtGui.QLabel(Dialog)
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.gridLayout.addWidget(self.courseNameLabel, 0, 0, 1, 1)
        self.LectureTitleLabel = QtGui.QLabel(Dialog)
        self.LectureTitleLabel.setObjectName("LectureTitleLabel")
        self.gridLayout.addWidget(self.LectureTitleLabel, 1, 0, 1, 1)
        self.LectureTitleLineEdit = QtGui.QLineEdit(Dialog)
        self.LectureTitleLineEdit.setObjectName("LectureTitleLineEdit")
        self.gridLayout.addWidget(self.LectureTitleLineEdit, 1, 1, 1, 3)
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 1, 1, 2)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "add Lecture", None, QtGui.QApplication.UnicodeUTF8))
        self.courseNameLabel.setText(QtGui.QApplication.translate("Dialog", "Course ", None, QtGui.QApplication.UnicodeUTF8))
        self.LectureTitleLabel.setText(QtGui.QApplication.translate("Dialog", "Lecture Title", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

