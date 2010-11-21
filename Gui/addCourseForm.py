# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addCourseForm.ui'
#
# Created: Sat Oct 30 15:07:36 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(243, 134)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.courseNameLabel = QtGui.QLabel(Dialog)
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.gridLayout.addWidget(self.courseNameLabel, 0, 0, 1, 1)
        self.courseNameLineEdit = QtGui.QLineEdit(Dialog)
        self.courseNameLineEdit.setObjectName("courseNameLineEdit")
        self.gridLayout.addWidget(self.courseNameLineEdit, 0, 2, 1, 2)
        self.courseInstructorLabel = QtGui.QLabel(Dialog)
        self.courseInstructorLabel.setObjectName("courseInstructorLabel")
        self.gridLayout.addWidget(self.courseInstructorLabel, 1, 0, 1, 2)
        self.courseInstructorLineEdit = QtGui.QLineEdit(Dialog)
        self.courseInstructorLineEdit.setObjectName("courseInstructorLineEdit")
        self.gridLayout.addWidget(self.courseInstructorLineEdit, 1, 2, 1, 2)
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 1, 1, 2)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "add Course", None, QtGui.QApplication.UnicodeUTF8))
        self.courseNameLabel.setText(QtGui.QApplication.translate("Dialog", "Course name", None, QtGui.QApplication.UnicodeUTF8))
        self.courseInstructorLabel.setText(QtGui.QApplication.translate("Dialog", "Course Instructor", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

