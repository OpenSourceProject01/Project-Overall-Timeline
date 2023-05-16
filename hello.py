import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


form = resource_path('mainwindow.ui')  # 여기에 ui파일명 입력
form_class = uic.loadUiType(form)[0]

form_second = resource_path('secondwindow.ui')
form_secondwindow = uic.loadUiType(form_second)[0]

form_thr = resource_path('signup.ui')
form_signup = uic.loadUiType(form_thr)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def loginclick(self):
        self.hide()  # 메인윈도우 숨김
        self.second = secondwindow()  #
        self.second.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.show()  # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

    def signupclick(self):
        self.hide()  # 메인윈도우 숨김
        self.thr = signupwindow()  #
        self.thr.exec()  # 두번째 창을 닫을 때 까지 기다림
        self.show()  # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐

class secondwindow(QDialog,QWidget,form_secondwindow):
    def __init__(self):
        super(secondwindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

    # 추가
    def buttonclick(self):
        self.close()

class signupwindow(QDialog,QWidget,form_signup):
    def __init__(self):
        super(signupwindow, self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)

        # 추가

    def buttonclick(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
