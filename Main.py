# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###




from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Gui import MainForm
from Database import CoursesDB
from Courses import Courses
from Edit import Edit
from Todo import Todo
from Schedule import Schedule
from Stats import Stats


class Main(QMainWindow, MainForm.Ui_MainWindow, Courses, Edit, Todo, Schedule, Stats):
    def __init__(self):
        """ Initializes App components / Modules"""
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Studiz")
        self.show()
        self.loadToolbarItems()
        self.DB = CoursesDB()
        self.loadCoursess()
        self.loadEdit()
        self.LoadScheduleTab()
        self.loadTodo()
        self.loadMenuActions()
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.conMenu)
        
    def loadMenuActions(self):
        self.actionaddCourse.triggered.connect(self.addCourses)
        self.actionaddLecture.triggered.connect(self.addLectures)
        self.actionaddTask.triggered.connect(self.addTask)
    
        self.actionviewCourses.triggered.connect(self.viewCourses)
        self.actionviewSchedule.triggered.connect(self.viewSchedule)
        self.actionviewStatistics.triggered.connect(self.viewStats)
        self.actionviewTo_Do_Tasks.triggered.connect(self.viewTasks)
        
        self.actionQuit.triggered.connect(qApp.closeAllWindows)
        self.actionAbout.triggered.connect(self.viewAbout)
        
    
    def loadToolbarItems(self):
        """Loads MainWindows ToolBarItems """
        
        viewCoursesIcon = QIcon("images/courses.png")
        self.toolBar.addAction(viewCoursesIcon, 'View Courses', self.viewCourses)
        
        self.toolBar.addSeparator()
        
        viewTasksIcon = QIcon("images/tasks.png")
        self.tasksIcon  = self.toolBar.addAction(viewTasksIcon, 'View Tasks', self.viewTasks)
        
        self.toolBar.addSeparator()
        
        viewScheduleIcon = QIcon('images/Schedule.png')
        self.toolBar.addAction(viewScheduleIcon, 'View Schedule', self.viewSchedule)
        
        self.toolBar.addSeparator()
        
        viewStatsIcon = QIcon('images/stats.png')
        self.toolBar.addAction(viewStatsIcon, 'View Statistics', self.viewStats)
        
        self.toolBar.addSeparator()
            
    def viewCourses(self):
        """ Switches Tab to Courses """
        self.tabWidget.setCurrentWidget(self.Tabcourses)
    def viewTasks(self):
        """ Switches Tab to Tasks """
        self.tabWidget.setCurrentWidget(self.TabTodo)
        
    def viewSchedule(self):
        """ Switches Tab to Schedule """
        self.tabWidget.setCurrentWidget(self.Tabschedule)
    def viewAbout(self):
        m = QMessageBox()
        m.about(self, 'About Author', """ 
        <b>Version</b> : 1.0 <br/>
        <b> Written By :</b> Redouane <br/>
        <b> E-mail:</b> <a href='mailto:unrealdz@gmail.com?Subject=Studiz'>unrealdz@gmail.com</a>    <br/>
        <b>Repository :</b> <a href="https://github.com/redouane/Studiz">https://github.com/redouane/Studiz</a><br/>
        <b>Blog : </b><a href='http://dzpp.blogspot.com'>dzpp.blogspot.com</a><br/>
        """)
        
    
        