# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###




from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Custom import InsertTable

class Edit(object):
    
    def loadEdit(self):
        self.loadEditToolbar()
        self.loadFontToolbar()
        self.gridLayout_3.addWidget(self.EditToolbar, 0,0,1,8)
        self.gridLayout_3.addWidget(self.fontToolbar, 1,0,1,8)
        self.gridLayout_3.addWidget(self.textEdit, 2,0,1,10)
        self.gridLayout_3.addWidget(self.groupBox, 0,8,2,2)
        
    def loadEditToolbar(self):
        """Loads Edit ToolBar"""
        self.EditToolbar = QToolBar(self.TabEdit)        #icons toolbar
        self.EditToolbar.setObjectName("EditToolbar")
        self.saveLectureicon =QIcon('images/savetodb.png')
        saveAction = self.EditToolbar.addAction(self.saveLectureicon, 'Save Lecture to the Database', self.saveLecture)
        saveAction.setShortcut('Ctrl+S')
        
        self.EditToolbar.addSeparator()
        
        self.savetopdfIcon = QIcon('images/savetopdf.png')
        exportPdfAction = self.EditToolbar.addAction(self.savetopdfIcon, 'Export as PDF', self.saveasPdf)
        exportPdfAction.setShortcut('Ctrl+E')
        
        self.EditToolbar.addSeparator()
        
        self.boldicon = QIcon('images/textbold.png')
        self.bold = self.EditToolbar.addAction(self.boldicon, 'Bold', self.setBold)
        self.bold.setCheckable(True)
        
        self.EditToolbar.addSeparator()
        
        self.italicicon = QIcon('images/textitalic.png')
        self.italic = self.EditToolbar.addAction(self.italicicon, 'Italic', self.setItalic)
        self.italic.setCheckable(True)
        
        self.EditToolbar.addSeparator()
        
        self.underlinedicon = QIcon('images/textunder.png')
        self.underlined = self.EditToolbar.addAction(self.underlinedicon, 'Underlined', self.setUnderlined)
        self.underlined.setCheckable(True)
        
        self.EditToolbar.addSeparator()
        
        self.EditToolbar.addAction(QIcon("images/editundo.png"), 'Undo', self.textEdit.undo)
        self.EditToolbar.addSeparator()
        self.EditToolbar.addAction(QIcon("images/editredo.png"), 'Redo', self.textEdit.redo)
        self.EditToolbar.addSeparator()
        
        self.textlefticon = QIcon('images/textleft.png')
        self.textleft = self.EditToolbar.addAction(self.textlefticon, 'Align left', self.leftText)
        self.textleft.setCheckable(True)
        self.textleft.setChecked(True)
        
        self.EditToolbar.addSeparator()
        
        self.textcentericon = QIcon('images/textcenter.png')
        self.textcenter = self.EditToolbar.addAction(self.textcentericon, 'Align Center', self.centerText)
        self.textcenter.setCheckable(True)
        
        self.EditToolbar.addSeparator()
        
        self.textrighticon = QIcon('images/textright.png')
        self.textright = self.EditToolbar.addAction(self.textrighticon, 'Align Right', self.rightText)
        self.textright.setCheckable(True)
        
        self.EditToolbar.addSeparator()
        
        
        self.textjustifyicon = QIcon('images/textjustify.png')
        self.textjustify = self.EditToolbar.addAction(self.textjustifyicon, 'Align Justify', self.justifyText)
        self.textjustify.setCheckable(True)
        
        self.EditToolbar.addSeparator()
        
        
        self.addTableIcon =  QIcon('images/table.png')
        self.addTable = self.EditToolbar.addAction(self.addTableIcon, 'Insert Table', self.TableInsert)
        
               
    def loadFontToolbar(self):
        """ Loads Edit's Font ToolBar"""    
        self.fontToolbar = QToolBar(self.TabEdit)   #font toolbar
        self.fontToolbar.setObjectName("fontToolbar")
        self.selectFont = QFontComboBox()
        self.fontToolbar.addWidget(self.selectFont)
        
        self.fontToolbar.addSeparator()
        
        self.fontsize = QComboBox()
        for i in range(2,13):
            self.fontsize.addItem(str(i))
        i = 14
        while i<49:
            self.fontsize.addItem(str(i))
            i+=2
        self.fontsize.addItems(['60','72'])
        self.fontsize.setCurrentIndex(9)
        self.textEdit.setFontPointSize(11)
        self.fontsize.setEditable(True)
        self.fontToolbar.addWidget(self.fontsize)
        
        self.fontToolbar.addSeparator()
        
        self.selectFont.currentFontChanged.connect(self.textEdit.setCurrentFont)
        self.fontsize.currentIndexChanged.connect(lambda : self.textEdit.setFontPointSize(float(self.fontsize.currentText())))
        
        self.fontcolorpix = QPixmap(13,13)
        self.fontcoloricon = QIcon(self.fontcolorpix)
        self.fontcolor = self.fontToolbar.addAction(self.fontcoloricon, 'color', self.setTextColor)
        
        self.fontToolbar.addSeparator()
        
        
        self.searchinput = QLineEdit()
        self.searchinput.setStyleSheet("background:url('images/search_icon.gif') no-repeat;")
        self.searchinput.setTextMargins(15,0,0,0)
        self.searchinputAction = self.fontToolbar.addWidget(self.searchinput)
        
        self.fontToolbar.addSeparator()
        
        self.searchButton = QPushButton('Search!')
        self.searchButtonAction = self.fontToolbar.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.Search)
    
    
    def TableInsert(self):
        self.table = InsertTable(self)
    def Search(self):
        """Searches for given string"""
        self.q = self.searchinput.text()
        self.textEdit.find(self.q)
        self.textEdit.setFocus()
    def setTextColor(self):
        """Sets Text Color"""
        self.color = QColorDialog.getColor()
        self.fontcoloricon = self.createPixMapIcon(self.color)
        self.fontcolor.setIcon(self.fontcoloricon)
        self.textEdit.setTextColor(self.color)
    def createPixMapIcon(self,color):
        """returns colored Pixmap"""
        colorpix = QPixmap(13,13)
        colorpix.fill(color)
        coloricon = QIcon(colorpix)
        return coloricon
        
    def centerText(self):
        """aligns the text to the center"""
        self.textjustify.setChecked(False)
        self.textleft.setChecked(False)
        self.textright.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignCenter)
        
    def justifyText(self):
        """ aligns the text as justify"""
        self.textleft.setChecked(False)
        self.textright.setChecked(False)
        self.textcenter.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignJustify)
    def leftText(self):
        """ align the text to the left"""
        self.textjustify.setChecked(False)
        self.textcenter.setChecked(False)
        self.textright.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignLeft)
    def rightText(self):
        """aligns the text to the right"""
        self.textjustify.setChecked(False)
        self.textleft.setChecked(False)
        self.textcenter.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignRight)
        
    def setBold(self):
        """sets Bold Text"""
        if self.bold.isChecked():
            self.textEdit.setFontWeight(QFont.Bold)
        else:
            self.textEdit.setFontWeight(QFont.Light)
    def setItalic(self):
        """ sets Italic Text"""
        if self.italic.isChecked():
            self.textEdit.setFontItalic(True)
        else:
            self.textEdit.setFontItalic(False)
    def setUnderlined(self):
        """Sets Underlined Text"""
        if self.underlined.isChecked():
            self.textEdit.setFontUnderline(True)
        else:
            self.textEdit.setFontUnderline(False)
    
        
    def saveasPdf(self):
        """Exports as a PDF"""
        self.lecturetitle = str(self.titleLineEdit.text()).decode()
        self.savepath = QFileDialog.getSaveFileName(self, "Save Lecture as PDF", "/home/%s - %s.pdf" %(self.courseComboBox.currentText(), self.lecturetitle), "Portable Document Format (*.pdf)")
        if self.savepath !="":
            self.p = QPrinter()
            self.p.setOutputFormat(QPrinter.PdfFormat)
            self.p.setOutputFileName(self.savepath)
            self.textEdit.print_(self.p)
            self.statusbar.showMessage('PDF Exported', 2000)
        
    def saveLecture(self):
        """ Saves Lecture to the database"""
        self.content = str(self.textEdit.toHtml()).decode()
        self.title = str(self.titleLineEdit.text()).decode()
        args = (self.title, self.content, self.lecture[0])
        self.DB.updateLecture(args)
        self.treeWidget.clear()
        self.loadCourses()
        self.lecturetitle = self.lecture[2]
        self.p = QPrinter()
        self.p.setOutputFormat(QPrinter.PdfFormat)
        self.savepath = 'Documents/%s - %s.pdf' % (self.lecture[0], self.lecture[2])
        self.p.setOutputFileName(self.savepath)
        self.textEdit.print_(self.p)
        self.statusbar.showMessage('Lecture Saved', 2000)