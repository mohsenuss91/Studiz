# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###


from Gui import addCourseForm, addLectureForm, insertTableForm
from PyQt4.QtGui import *
from PyQt4.QtCore import *



class Genericadd(QDialog):
    def __init__(self):
        super(Genericadd, self).__init__()
        self.setupUi(self)
        self.show()
        self.addButton.setIcon(QIcon("images/Add.png"))
        self.cancelButton.setIcon(QIcon("images/removetask.png"))
        self.addButton.clicked.connect(self.add)
        self.cancelButton.clicked.connect(lambda close: self.close())
    def updateUi(self):
        self.arg.treeWidget.clear()
        self.arg.loadCourses()
        
class addCourse(Genericadd, addCourseForm.Ui_Dialog):
    def __init__(self, arg):
        super(addCourse, self).__init__()
        self.arg = arg
        self.DB = arg.DB  
    def add(self):
        self.coursename = str(self.courseNameLineEdit.text()).decode()
        self.courseinstructor = str(self.courseInstructorLineEdit.text()).decode()
        item = QTreeWidgetItem()
        item.setText(0,self.coursename)
        item.setText(1,self.courseinstructor)
        f = QFont()
        f.setBold(True)
        item.setFont(0, f)
        self.arg.treeWidget.addTopLevelItem(item)
        args = (self.coursename, self.courseinstructor)
        self.DB.addCourse(args)
        self.arg.statusbar.showMessage('Course Added', 2000)
        self.close()

class addLecture(Genericadd, addLectureForm.Ui_Dialog):
    def __init__(self, arg):
        super(addLecture, self).__init__()
        self.arg = arg
        self.DB = arg.DB
        self.initCourses()
    def initCourses(self):
        self.courselist = self.DB.GetCourses()
        for row in self.courselist:
            self.comboBox.addItem(row[1])
    def getcourseid(self, coursename):
        for row in self.courselist:
            if row[1] == coursename:
                return row[0]
    def add(self):
        self.text = ""
        self.title = str(self.LectureTitleLineEdit.text()).decode()
        self.coursename = self.comboBox.currentText()
        self.courseid = self.getcourseid(self.coursename)
        if self.courseid == None:
            self.comboBox.setStyleSheet("border:1px solid red; border-radius:5px;")
        else:
            args = (self.courseid, self.title, self.text)
            self.DB.addLecture(args)
            self.updateUi()
            self.arg.tabWidget.setCurrentWidget(self.arg.TabEdit)
            self.title = (self.title,)
            self.currentlecture = self.DB.getaddedLectureID(self.title)
            self.arg.statusbar.showMessage('Lecture Note Added', 2000)
            self.close()
            self.arg.editer(self.currentlecture)
            self.arg.textEdit.setHtml("<br/> < span style='background:#e9e9e9; color:#25587E; font-size:14pt; border:solid 1px red;'>    <i><u> %s :</u></i></span> <br/><hr/><br/><br/>" % self.title[0])
class InsertTable(QDialog, insertTableForm.Ui_Dialog):
    def __init__(self, arg):
        super(InsertTable, self).__init__()
        self.setupUi(self)
        self.show()
        self.arg = arg
        self.BGcolorIcon =self.arg.createPixMapIcon(Qt.white)
        self.BGButton.setIcon(self.BGcolorIcon)
        self.BordercolorIcon =self.arg.createPixMapIcon(Qt.black)
        self.BorderButton.setIcon(self.BordercolorIcon)
        self.chosenBGColor = Qt.white
        self.chosenBorderColor = Qt.black
        self.BGButton.clicked.connect(self.getBGColor)
        self.BorderButton.clicked.connect(self.getBorderColor)
        self.buttonBox.accepted.connect(self.insert)
        self.buttonBox.rejected.connect(self.close)
    def getBGColor(self):
        self.chosenBGColor = QColorDialog.getColor()
        colorBGIcon = self.arg.createPixMapIcon(self.chosenBGColor)
        self.BGButton.setIcon(colorBGIcon)
    def getBorderColor(self):
        self.chosenBorderColor = QColorDialog.getColor()
        colorBorderIcon = self.arg.createPixMapIcon(self.chosenBorderColor)
        self.BGButton.setIcon(colorBorderIcon)
    def insert(self):
        self.textcursor = self.arg.textEdit.textCursor()
        tableformat = QTextTableFormat()
        tableformat.setBackground(self.chosenBGColor)
        tableformat.setBorderBrush(self.chosenBorderColor)
        tableformat.setCellPadding(self.cellPaddingSpinBox.value())
        tableformat.setCellSpacing(self.cellSpacingSpinBox.value())
        self.textcursor.insertTable(self.rowsSpinBox.value(),self.columnsSpinBox.value(), tableformat)
        self.close()


class areyouSure(QMessageBox):
    def __init__(self):
        super(areyouSure, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setText("Are you Sure ?!")
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Confirmation")
        self.show()
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    def confirmed(self):
        res = self.exec_()
        if (res == QMessageBox.No):
            return False
        elif (res == QMessageBox.Yes):
            return True


class addImportedLecture(addLecture):
    def __init__(self,arg,stuff):
        super(addImportedLecture, self).__init__(arg)
        self.load()
        self.importedtitle = stuff[0]
        self.importeddate = stuff[1]
        self.importedcontent = stuff[2]
    def load(self):
        self.LectureTitleLineEdit.hide()
        self.LectureTitleLabel.hide()
        self.setWindowTitle("Import Lecture in :")
        
    def add(self):
        self.coursename = self.comboBox.currentText()
        self.courseid = self.getcourseid(self.coursename)
        if self.courseid == None:
            self.comboBox.setStyleSheet("border:1px solid red; border-radius:5px;")
        else:
            args = (self.courseid, self.importedtitle, self.importedcontent)
            self.DB.addLecture(args)
            self.updateUi()
            self.arg.tabWidget.setCurrentWidget(self.arg.TabEdit)
            self.title = (self.importedtitle,)
            self.currentlecture = self.DB.getaddedLectureID(self.title)
            self.arg.statusbar.showMessage('Lecture Added', 2000)
            self.close()
            self.arg.editer(self.currentlecture)
    