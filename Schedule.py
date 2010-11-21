# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###




from PyQt4.QtGui import *
from PyQt4.QtCore import *
import csv
import urllib


class Schedule(object):
    def LoadScheduleTab(self):
        """Loads Schedule Components"""
        self.loadScheduleToolBar()
        self.loadSchedule()
    
    def loadScheduleToolBar(self):
        """Loads Schedule's ToolBar"""
        ScheduleToolbar = QToolBar(self.Tabschedule)        
        ScheduleToolbar.setObjectName("ScheduleToolbar")
        importscsvIcon = QIcon('images/importcsv.png')
        ScheduleToolbar.addAction(importscsvIcon, 'Import CSV File', self.importCSV)
        
        ScheduleToolbar.addSeparator()
        
        exportIcon = QIcon('images/exportcsv.gif')
        ScheduleToolbar.addAction(exportIcon, 'Export CSV File', self.exporttoCSV)
        
        ScheduleToolbar.addSeparator()
        
        self.gridLayout_4.addWidget(ScheduleToolbar, 0,0,1,1)
        self.gridLayout_4.addWidget(self.tableWidget,1,0,1,1)

    def loadSchedule(self):
        """Loads The Schedule from the present file"""
        try:
            with open('Schedule.csv', 'rb') as f:
                data = list(csv.reader(f))
            biggest = 0
            for row in data:
                if biggest < len(row):
                    biggest = len(row)
            self.tableWidget.setColumnCount(biggest)
            i = 0
            j = 0
            brush = QBrush(QColor(85, 170, 255))
            brush.setStyle(Qt.Dense6Pattern)
            font = QFont()
            font.setBold(True)
            font.setPointSize(8)
            for row in data:
                for col in row:
                    if i==0:
                        horizitem = QTableWidgetItem("t - %d" % j)
                        self.tableWidget.setHorizontalHeaderItem(j, horizitem)
                    item = QTableWidgetItem()
                    self.tableWidget.setItem(i,j,item)
                    if i==0:
                        self.tableWidget.item(i,j).setBackground(brush)
                        self.tableWidget.item(i,j).setForeground(Qt.black)
                        self.tableWidget.item(i,j).setFont(font)
                    self.tableWidget.item(i,j).setText(col)
                    j+=1
                i+=1
                j=0
        except:
            return
        self.tableWidget.resizeColumnsToContents()
        self.connect(self.tableWidget, SIGNAL("cellChanged(int,int)"), self.saveCSV)
    def exporttoCSV(self):
        """Export current Schedule as CSV"""
        savepath = QFileDialog.getSaveFileName(self, "Save Schedule as CSV", "/home/Schedule.csv" , "Comma-separated values (*.csv)")
        if savepath !="":
            rows = self.tableWidget.rowCount()
            cols = self.tableWidget.columnCount()
            currentdata = []
            rowlist = []
            for row in range(0,rows):
                if len(rowlist) >0:
                    currentdata.append(rowlist)
                    rowlist = []
                for col in range(0,cols):
                    try:
                        item =  self.tableWidget.item(row,col).text()
                    except AttributeError:
                        continue
                    rowlist.append(item)
            currentdata.append(rowlist)
            writer = csv.writer(open(savepath, 'w'))
            for row in currentdata:
                writer.writerow(row)
    
    def saveCSV(self):
        """Saves Current Schedule as the local-loaded by the app CSV"""
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()
        currentdata = []
        rowlist = []
        for row in range(0,rows):
            if len(rowlist) >0:
                currentdata.append(rowlist)
                rowlist = []
            for col in range(0,cols):
                try:
                    item =  self.tableWidget.item(row,col).text()
                except AttributeError:
                    continue
                rowlist.append(item)
        currentdata.append(rowlist)
        writer = csv.writer(open('Schedule.csv', 'w'))
        for row in currentdata:
            writer.writerow(row)
        self.tableWidget.resizeColumnsToContents()
    def importCSV(self):
        """Import CSV file and fill the table"""
        filepath = QFileDialog.getOpenFileName(self, 'Load CSV file',"","Comma-separated values (*.csv)")
        if filepath !="":
            urllib.urlretrieve('file:/// %s' % filepath,'Schedule.csv')
            self.tableWidget.clear()
            self.loadSchedule()