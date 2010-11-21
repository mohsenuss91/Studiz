# -*- coding: latin_1 -*-


###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###




from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Database import TasksDB


class Todo(object):
    
    def loadTodo(self):
        """Loads Todo Components"""
        self.loadTodoToolBar()
        self.TodoList.header().resizeSection(0,30)
        self.TodoList.header().resizeSection(2,70)
        self.TodoList.header().resizeSection(3,30)
        self.TodoList.header().setStretchLastSection(False)
        self.TodoList.header().setResizeMode(3, QHeaderView.Fixed)
        self.TodoList.header().setResizeMode(1, QHeaderView.Stretch)
        self.loadTasks()
        self.setTasksNotification()
    
    def setTasksNotification(self):
        """sets Notification on Tasks Icon"""
        notdone = len(self.TasksDB.getUndoneTasks())
        if notdone > 0:
            x = QPixmap()
            x.load('images/tasks.png')
            painter = QPainter()
            painter.begin(x)
            painter.setPen(Qt.red)
            painter.setFont(QFont('Decorative', 24))
            painter.drawText(15,39, str(notdone))
            painter.end()
            self.tasksIcon.setIcon(QIcon(x))
        elif notdone ==0:
            x = QPixmap()
            x.load('images/tasks.png')
            self.tasksIcon.setIcon(QIcon(x))
    def loadTodoToolBar(self):
        """Loads Todo's ToolBar"""
        TodoToolbar = QToolBar(self.TabTodo)
        TodoToolbar.setObjectName("TodoToolbar")
        
        addTaskIcon = QIcon("images/addtask1.png")
        TodoToolbar.addAction(addTaskIcon, 'Add Task', self.addTask)
        
        TodoToolbar.addSeparator()
        
        selectallIcon = QIcon("images/selectall.png")
        TodoToolbar.addAction(selectallIcon, 'Selects all tasks', self.selectAllTasks)
        
        TodoToolbar.addSeparator()
        
        setTaskdonelIcon = QIcon("images/taskdoneicon.png")
        TodoToolbar.addAction(setTaskdonelIcon, 'Mark Task as Done', self.setTaskdone)
                
        TodoToolbar.addSeparator()
        
        deleteTasksIcon = QIcon("images/removetask.png")
        TodoToolbar.addAction(deleteTasksIcon, 'Delete Selected Tasks', self.deleteTasks)
        
        self.gridLayout_5.addWidget(TodoToolbar, 0,0,1,1)
        self.gridLayout_5.addWidget(self.TodoList, 1,0,1,1)
    
    def loadTasks(self):
        """Loads the tasks from the Database"""
        self.TasksDB = TasksDB()
        Tasklist = self.TasksDB.GetTasks()
        self.tasklistlength = len(Tasklist)
        for task in Tasklist:
            item = QTreeWidgetItem(self.TodoList)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            item.setCheckState(0,0)
            item.setText(1, task[1])
            item.setText(2,str(task[2]))
            brush = QColor('transparent')
            item.setForeground(2,brush)
            f = QFont()
            f.setBold(True)
            item.setFont(1, f)
            item.DBiD = task[0]
            if task[2] ==0:
                notdoneIcon = QIcon("images/tasknotdone.png")
                item.setIcon(2, notdoneIcon)
            else:
                doneIcon = QIcon("images/taskdoneicon.png")
                item.setIcon(2, doneIcon)
                
        self.TodoList.itemChanged.connect(self.updateTask)


    def addTask(self):
        """ Add a new Task"""
        self.tabWidget.setCurrentWidget(self.TabTodo)
        item = QTreeWidgetItem()
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable)
        item.setCheckState(0, 0)
        item.setText(1, 'type your task here')
        f = QFont()
        f.setBold(True)
        item.setFont(1, f)
        notdoneIcon = QIcon("images/tasknotdone.png")
        item.setIcon(2,notdoneIcon)
        args = (str(item.text(1)).decode(),0)
        self.TasksDB.addTask(args)
        item.DBiD = len(self.TasksDB.GetTasks())
        self.TodoList.insertTopLevelItem(0, item)
        self.setTasksNotification()
        self.TodoList.editItem(item,1)
        self.statusbar.showMessage('Task Added', 2000)
    def updateTask(self,item,itemindex):
        """Update Existing Task"""
        if itemindex ==1:
            if hasattr(item, 'DBiD'):
                args = (str(item.text(1)).decode(), item.DBiD)
                self.TasksDB.UpdateTask(args)
                self.statusbar.showMessage('Task(s) Updated', 2000)
            else:
                return
    def deleteTasks(self):
        """Delete Checked Tasks"""
        deletelist = []
        itemnumber = self.TodoList.topLevelItemCount()
        for i in range(0,itemnumber):
            item = self.TodoList.topLevelItem(i)
            if item.checkState(0) ==2:
                deletelist.append(item)
        for item in deletelist:
            index = self.TodoList.indexOfTopLevelItem(item)
            self.TodoList.takeTopLevelItem(index)
            self.TasksDB.removeTask((item.DBiD,))
        self.setTasksNotification()
        self.statusbar.showMessage('Task(s) Deleted', 2000)
        
    def selectAllTasks(self):
        """Checks all Task items"""
        itemnumber = self.TodoList.topLevelItemCount()
        for i in range(0,itemnumber):
            item = item = self.TodoList.topLevelItem(i)
            item.setCheckState(0,2)
    
    def setTaskdone(self):
        """Sets Task state to Done"""
        donelist = []
        itemnumber = self.TodoList.topLevelItemCount()
        for i in range(0,itemnumber):
            item = self.TodoList.topLevelItem(i)
            if item.checkState(0) ==2:
                donelist.append(item)
        for item in donelist:
            doneIcon = QIcon("images/taskdoneicon.png")
            item.setIcon(2,doneIcon)
            self.TasksDB.UpdateTaskStatus((1,item.DBiD))
        self.setTasksNotification()