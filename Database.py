# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###



import sqlite3

class DB(object):
    def __init__(self):
        """Connect / Create the database"""
        self.con = sqlite3.connect('Studiz.db')
        self.cursor = self.con.cursor() 

class initDB(DB):
    def __init__(self):
        """Initializes the Database for first time Launch"""
        super(initDB, self).__init__() 
        self.cursor.execute("""create table if not exists courses(id integer primary key, coursename text, taughtby text)""")
        self.cursor.execute("""create table if not exists lectures(id integer primary key, courseid integer, title text, content text, date date, views integer, revision integer)""")
        self.cursor.execute("""create table if not exists tasks(id integer primary key, task text, state integer) """)        
        self.con.commit()
        self.cursor.close()

class CoursesDB(DB):
    def __init__(self):
        super(CoursesDB, self).__init__()
    def GetCourses(self):
        """reeturns list of courses rows"""
        self.cursor.execute("""SELECT * FROM courses""")
        self.courselist = self.cursor.fetchall()
        return self.courselist
    def GetAllLectures(self):
        """returns list of lecture rows"""
        self.cursor.execute("""SELECT * FROM lectures """)
        self.lecturelist = self.cursor.fetchall()
        return self.lecturelist
    def GetLectures(self, courseid):
        """returns given course's id lectures as a list"""
        self.cursor.execute("""SELECT * FROM lectures WHERE courseid = ?""", (courseid,))
        self.lecturelist = self.cursor.fetchall()
        return self.lecturelist
    def addLecture(self, args):
        """add Lecture to DB"""
        self.cursor.execute("""insert into lectures values(NULL, ?, ?, ?, datetime('now'), 0, 0)""", args)
        self.con.commit()
    def addCourse(self, args):
        """add Course to DB"""
        self.cursor.execute("""insert into courses values(NULL,?,?)""", args)
        self.con.commit()
    def updateLecture(self, args):
        """Updates existing Lecture's title / content"""
        self.cursor.execute("""UPDATE lectures set title=?, content=? where id=?""", args)
        self.con.commit()
    def getaddedLectureID(self, args):
        """returns given lectures titles lecture id"""
        self.cursor.execute("""SELECT * from lectures where title=?""", args)
        self.currentlecture = self.cursor.fetchall()
        return self.currentlecture[0]
    def UpdateLectureviews(self,args):
        """updates Lecture Reviews"""
        self.cursor.execute("""UPDATE lectures set views = views+1 where id=?""", args)
        self.con.commit()
    def DeleteLecture(self,ID):
        self.cursor.execute(""" DELETE FROM lectures WHERE id=?""", (ID,))
        self.con.commit()
    def DeleteCourse(self,ID):
        self.cursor.execute(""" DELETE FROM courses WHERE id=?""", (ID,))
        self.cursor.execute(""" DELETE FROM lectures WHERE courseid=?""", (ID,))
        self.con.commit()
    def DeleteCoursebyName(self,Name):
        self.cursor.execute(""" SELECT * FROM courses WHERE coursename=?""", (Name,))
        ID = self.cursor.fetchall()[0][0]
        self.cursor.execute(""" DELETE FROM courses WHERE id=?""", (ID,))
        self.cursor.execute(""" DELETE FROM lectures WHERE courseid=?""", (ID,))
        self.con.commit()
    
class TasksDB(DB):
    def __init__(self):
        super(TasksDB, self).__init__()
    def GetTasks(self):
        """returns list of tasks"""
        self.cursor.execute("""SELECT * from tasks """)
        self.tasklist = self.cursor.fetchall()
        return self.tasklist
    def addTask(self, args):
        """add task to the db"""
        self.cursor.execute("""insert into tasks values(NULL,?,?)""", args)
        self.con.commit()
    def UpdateTask(self,args):
        """update existing task"""
        self.cursor.execute("""UPDATE tasks set task = ? where id = ?""", args)
        self.con.commit()
    def removeTask(self,args):
        """delete task from db"""
        self.cursor.execute("""DELETE FROM tasks WHERE id=?""", args)
        self.con.commit()
    def UpdateTaskStatus(self,args):
        """update task state"""
        self.cursor.execute("""UPDATE tasks set state = ? where id = ?""", args)
        self.con.commit()
    def getUndoneTasks(self):
        """returns not-done yet tasks as a list"""
        self.cursor.execute("""SELECT * FROM tasks WHERE state=0""")
        list = self.cursor.fetchall()
        return list
