# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###


from PyQt4.QtGui import *
from PyQt4.QtCore import *
from os import startfile
from Custom import areyouSure, addLecture, addImportedLecture, addCourse

from xml.etree.ElementTree import Element, SubElement, ElementTree





class Courses(object):
    def loadCoursess(self):
        self.LoadCoursesToolBar()
        self.gridLayout_2.addWidget(self.CoursesToolBar, 0,0,1,1)
        self.gridLayout_2.addWidget(self.treeWidget, 1,0,1,1)
        self.loadCourses()
    
    def loadCourses(self):
        self.courselist = self.DB.GetCourses()
        for course in self.courselist:
            self.courseid = course[0]
            self.courselectures = self.DB.GetLectures(self.courseid)     
            self.courseitem = QTreeWidgetItem()
            f = QFont()
            f.setBold(True)
            self.courseitem.setFont(0, f)
            self.courseitem.courseid = self.courseid
            self.treeWidget.insertTopLevelItem(0,self.courseitem)
            self.courseitem.setText(0, course[1])
            self.courseitem.setText(1, course[2])
            for lecture in self.courselectures:
                self.lectureitem = QTreeWidgetItem()
                self.lectureitem.setFont(2,f)                
                self.courseitem.addChild(self.lectureitem)
                self.lectureitem.dbinfos = lecture
                self.lectureitem.setText(2, lecture[2])         #lecture title
                self.lectureitem.setText(3, lecture[4])         #lecture date
                self.lectureitem.setText(4, '     ' + str(lecture[5]))    # lecture views
                
                self.lectureitem.setForeground(5, QBrush(QColor("transparent")))
                if lecture[5] >= 1:
                    self.reviewed = QIcon("images/reviewed.png")
                    self.lectureitem.setIcon(5, self.reviewed)
                    self.lectureitem.setText(5, str(1))
                else:    
                    self.notreviewed = QIcon("images/notreviewed.png")
                    self.lectureitem.setIcon(5, self.notreviewed)
                    self.lectureitem.setText(5, str(0))
                self.courseitem.addChild(self.lectureitem)
                
        self.treeWidget.header().setStretchLastSection(False)
        self.treeWidget.header().resizeSection(5,80)
        self.treeWidget.header().resizeSection(3,120)
        self.treeWidget.header().resizeSection(4,50)
        self.treeWidget.header().setResizeMode(2, QHeaderView.Stretch)
        
    
    def LoadCoursesToolBar(self):
        self.CoursesToolBar = QToolBar()
        self.CoursesToolBar.setObjectName("CoursesToolBar")
        
        addCourseIcon = QIcon("images/addcourse.png")
        self.CoursesToolBar.addAction(addCourseIcon, 'Add Course', self.addCourses)

        self.CoursesToolBar.addSeparator()
        
        addLectureIcon = QIcon("images/addlecture.png")
        self.CoursesToolBar.addAction(addLectureIcon, 'Add Lecture notes', self.addLectures)
        
        self.CoursesToolBar.addSeparator()
        
        importLectureIcon = QIcon("images/importstdz.png")
        self.CoursesToolBar.addAction(importLectureIcon, 'Import Lecture notes', self.importLectures)
        
        self.CoursesToolBar.addSeparator()
    
    
    def importLectures(self):
        from xml.etree import ElementTree as ELementTree
        filepath = QFileDialog.getOpenFileName()
        if filepath !='':
            with open(filepath, 'rt') as f:
                tree = ELementTree.parse(f)
            stuff = []
            for path in ['./Title', './date', './Content']:
                node = tree.find(path)
                stuff.append(node.text)
            add = addImportedLecture(self, stuff)
    def exportLecture(self, dbinfos):
        lecturetitle = dbinfos[2]
        lecturecontent = dbinfos[3]
        lecturedate = dbinfos[4]
        savepath = QFileDialog.getSaveFileName(self, "Save Lecture as stdz", "/home/%s.stdz" % lecturetitle, "Studiz Lecture Note (*.stdz)")
        if savepath !='':
            lecture = Element('Lecture')
            title = SubElement(lecture, 'Title')
            title.text = lecturetitle
            date = SubElement(lecture, 'date')
            date.text = lecturedate
            content = SubElement(lecture, 'Content')
            content.text = lecturecontent
            ElementTree(lecture).write(savepath)
        
    def conMenu(self,point):
        item = self.treeWidget.itemAt(point)
        if (not item):
            return
        else:
            m = QMenu()
            delIcon = QIcon("images/removetask.png")
            editIcon = QIcon("images/editdoc.png")
            reviewIcon = QIcon("images/savetopdf.png")
            if item.parent():
                exportIcon = QIcon("images/exportstdz.png")
                m.addAction(reviewIcon,'Review Lecture', lambda :self.review((item)))
                m.addAction(editIcon,'Edit Lecture note', lambda :self.editer(item.dbinfos))
                m.addAction(exportIcon, 'Export Lecture note', lambda : self.exportLecture(item.dbinfos))
                m.addAction(delIcon,'Delete Lecture note', lambda :self.deleteItem(item))
                
            else:
                m.addAction(delIcon,'Delete Course', lambda :self.deleteItem(item))
            m.exec_(self.treeWidget.mapToGlobal(point))
    
    def deleteItem(self, item):
        if item.parent():   #checks wether item is toplevel or child  
                confirm= areyouSure()
                if confirm.confirmed():
                    parent = item.parent()
                    index = parent.indexOfChild(item)
                    parent.takeChild(index)
                    self.DB.DeleteLecture(item.dbinfos[0])   #lectures
                else:
                    return
        else:   
                confirm= areyouSure()
                if confirm.confirmed():
                    try:
                        self.DB.DeleteCourse(item.courseid)     #courses
                    except AttributeError:
                        self.DB.DeleteCoursebyName(str(item.text(0)).decode())
                    finally:
                        index = self.treeWidget.indexOfTopLevelItem(item)
                        self.treeWidget.takeTopLevelItem(index)
                else:
                    return
    def editer(self, lecture):
        self.tabWidget.setCurrentWidget(self.TabEdit)
        self.titleLineEdit.setText(lecture[2])
        self.textEdit.setHtml(lecture[3])
        self.lecture = lecture
        self.currentcourse = self.getCoursetitle(lecture[1])
        self.courseComboBox.addItem(self.currentcourse)
        self.courseComboBox.setDisabled(True)
    def review(self,item):
        try:
            startfile('Documents\\%s - %s.pdf' % (item.dbinfos[0], item.dbinfos[2]))
            self.DB.UpdateLectureviews((item.dbinfos[0],))
            item.setText(4, '     ' + str(int(item.text(4)) + 1))
            item.setIcon(5,QIcon("images/reviewed.png"))
            item.setText(5,str(1))
        except WindowsError:
            self.cantreviewError = QMessageBox()
            self.cantreviewError.setText('File Not Found !, Did you save yet ?')
            self.cantreviewError.setWindowTitle('Error!')
            self.cantreviewError.setIcon(QMessageBox.Warning)
            self.cantreviewError.show()
            
    def getCoursetitle(self, courseid):
        for row in self.courselist:
            if row[0] == courseid:
                return row[1]
    
    
    def addCourses(self):
        """ add Course Dialog"""
        self.course = addCourse(self)
        
    def addLectures(self):
        """add Lecture Dialog"""
        self.addlecture = addLecture(self)
        