# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###




from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Stats(object):
    def viewStats(self):
        totalcourses = len(self.DB.GetCourses())
        totallectures = len(self.DB.GetAllLectures())
        totaltasks =  len(self.TasksDB.GetTasks())
        totalundonetasks = totaltasks - len(self.TasksDB.getUndoneTasks())
        self.stats = QMessageBox()
        self.stats.about(self, "Statistics","""
        Total Courses : <b> %s</b>  <br/>
        Total Lecture notes : <b> %s   </b> <br/>
        <hr>
        Total Tasks : <b>%s</b>    <br/>
        Tasks Done : <b>%s</b>    <br/>
        """ % (totalcourses,totallectures, totaltasks,totalundonetasks))
