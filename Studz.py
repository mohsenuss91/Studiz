# -*- coding: latin_1 -*-

###   App By : Redouane            ###
###   E-MAIL : unrealdz@gmail.com  ###
###   BLOG : dzpp.blogspot.com     ### 
###   LICENSE : GNU GPL v3         ###



from PyQt4.QtGui import QApplication, QIcon
import sys
from Database import initDB
from Main import Main
from os import mkdir, path


def main():
    class App(QApplication):
        def __init__(self, argv):
            super(App, self).__init__(argv)
            if not path.exists('Documents'):
                mkdir('Documents')
            self.initializeDB = initDB()
            self.app = Main()
            try:
                f = open("styles/style.css", "r")
                self.setStyleSheet(f.read())
            except:
                return
            self.setWindowIcon(QIcon("images/studiz.png"))
    Studz = App(sys.argv)
    Studz.exec_()
    
if __name__ == '__main__':
    main()