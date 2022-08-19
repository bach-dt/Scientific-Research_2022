# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiFile/borrow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(300, 0))
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setObjectName("widget")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 300, 140))
        self.label_9.setStyleSheet("background-color: rgb(192, 32, 52 );\n"
"border-radius:20px;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.main_frame_3 = QtWidgets.QLabel(self.widget)
        self.main_frame_3.setGeometry(QtCore.QRect(0, 60, 300, 401))
        self.main_frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(186, 189, 182);\n"
"border-radius: 20px")
        self.main_frame_3.setText("")
        self.main_frame_3.setObjectName("main_frame_3")
        self.building = QtWidgets.QPushButton(self.widget)
        self.building.setGeometry(QtCore.QRect(70, 15, 160, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.building.setFont(font)
        self.building.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(192, 32, 52);\n"
"border-radius: 10px;")
        self.building.setObjectName("building")
        self.back = QtWidgets.QPushButton(self.widget)
        self.back.setGeometry(QtCore.QRect(10, 15, 21, 31))
        self.back.setStyleSheet("border-radius: 25px;\n"
"image: url(:/newPrefix/previous.png);\n"
"background-color: rgb(192, 32, 52);\n"
"")
        self.back.setText("")
        self.back.setObjectName("back")
        self.QR_2 = QtWidgets.QLabel(self.widget)
        self.QR_2.setEnabled(False)
        self.QR_2.setGeometry(QtCore.QRect(0, 170, 300, 291))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.QR_2.setFont(font)
        self.QR_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.QR_2.setObjectName("QR_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 180, 300, 191))
        self.label_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.023, stop:0 rgba(235, 235, 235, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.QR = QtWidgets.QLabel(self.widget)
        self.QR.setEnabled(False)
        self.QR.setGeometry(QtCore.QRect(0, 65, 300, 291))
        self.QR.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.QR.setText("")
        self.QR.setObjectName("QR")
        self.remainTime = QtWidgets.QLabel(self.widget)
        self.remainTime.setGeometry(QtCore.QRect(9, 404, 152, 46))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.remainTime.setFont(font)
        self.remainTime.setStyleSheet("image: url(:/newPrefix/countdown.gif);")
        self.remainTime.setText("")
        self.remainTime.setObjectName("remainTime")
        self.continue_ = QtWidgets.QPushButton(self.widget)
        self.continue_.setGeometry(QtCore.QRect(170, 405, 120, 44))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.continue_.setFont(font)
        self.continue_.setStyleSheet("QPushButton {\n"
"    background-color: rgb(252, 175, 62);\n"
"    color: rgb(255, 255, 255 );\n"
"   border-radius: 22px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(255, 195, 82);\n"
"   color: rgb(255, 255, 255 );\n"
"    border-radius: 22px;\n"
"}\n"
"\n"
"")
        self.continue_.setObjectName("continue_")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 190, 281, 141))
        self.scrollArea.setStyleSheet("border-radius: 2px;\n"
"background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 338, 141))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMinimumSize(QtCore.QSize(270, 0))
        self.label_5.setMaximumSize(QtCore.QSize(270, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(85, 87, 83);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setMinimumSize(QtCore.QSize(320, 100))
        self.widget_3.setMaximumSize(QtCore.QSize(320, 100))
        self.widget_3.setObjectName("widget_3")
        self.subject = QtWidgets.QLabel(self.widget_3)
        self.subject.setGeometry(QtCore.QRect(70, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.subject.setFont(font)
        self.subject.setStyleSheet("background-color: rgb(250, 245, 240);")
        self.subject.setObjectName("subject")
        self.start = QtWidgets.QLabel(self.widget_3)
        self.start.setGeometry(QtCore.QRect(10, 20, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgb(250, 245, 240);")
        self.start.setAlignment(QtCore.Qt.AlignCenter)
        self.start.setObjectName("start")
        self.room = QtWidgets.QLabel(self.widget_3)
        self.room.setGeometry(QtCore.QRect(70, 70, 191, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        font.setItalic(False)
        self.room.setFont(font)
        self.room.setStyleSheet("color: rgb(52, 101, 164);\n"
"background-color: rgb(250, 245, 240);")
        self.room.setObjectName("room")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 265, 100))
        self.label_18.setStyleSheet("background-color: rgb(250, 245, 240);\n"
"border-radius:5px;")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.code = QtWidgets.QLabel(self.widget_3)
        self.code.setGeometry(QtCore.QRect(70, 50, 191, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        font.setItalic(False)
        self.code.setFont(font)
        self.code.setStyleSheet("color: rgb(52, 101, 164);\n"
"background-color: rgb(250, 245, 240);")
        self.code.setObjectName("code")
        self.label_ = QtWidgets.QLabel(self.widget_3)
        self.label_.setGeometry(QtCore.QRect(10, 20, 41, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_.setFont(font)
        self.label_.setStyleSheet("background-color: rgb(250, 245, 240);")
        self.label_.setAlignment(QtCore.Qt.AlignCenter)
        self.label_.setObjectName("label_")
        self.end = QtWidgets.QLabel(self.widget_3)
        self.end.setGeometry(QtCore.QRect(10, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.end.setFont(font)
        self.end.setStyleSheet("background-color: rgb(250, 245, 240);")
        self.end.setAlignment(QtCore.Qt.AlignCenter)
        self.end.setObjectName("end")
        self.label_18.raise_()
        self.subject.raise_()
        self.room.raise_()
        self.code.raise_()
        self.label_.raise_()
        self.end.raise_()
        self.start.raise_()
        self.verticalLayout.addWidget(self.widget_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 280, 91))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 70, 70))
        self.label_4.setStyleSheet("image: url(:/newPrefix/user.png);\n"
"image: url(:/newPrefix/user.png);\n"
"image: url(:/newPrefix/user.png);\n"
"background-color: rgb(245, 245, 245);\n"
"border-radius:5px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setGeometry(QtCore.QRect(110, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(90, 90, 90);")
        self.name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.email = QtWidgets.QLabel(self.widget)
        self.email.setGeometry(QtCore.QRect(110, 140, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setUnderline(True)
        self.email.setFont(font)
        self.email.setStyleSheet("color: rgb(54, 122, 201);\n"
"background-color: rgb(255, 255, 255);")
        self.email.setObjectName("email")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(110, 120, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(136, 138, 133);\n"
"background-color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 350, 281, 44))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(241, 90, 90);\n"
"    color: rgb(255, 255, 255 );\n"
"   border-radius: 22px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_9.raise_()
        self.main_frame_3.raise_()
        self.building.raise_()
        self.back.raise_()
        self.QR_2.raise_()
        self.QR.raise_()
        self.label_7.raise_()
        self.remainTime.raise_()
        self.continue_.raise_()
        self.scrollArea.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.name.raise_()
        self.email.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setMinimumSize(QtCore.QSize(475, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(475, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 475, 140))
        self.label_10.setStyleSheet("background-color: rgb(192, 32, 52 );\n"
"border-radius:20px;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.main_frame = QtWidgets.QLabel(self.widget_2)
        self.main_frame.setGeometry(QtCore.QRect(0, 65, 475, 395))
        self.main_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px")
        self.main_frame.setText("")
        self.main_frame.setObjectName("main_frame")
        self.main_frame_2 = QtWidgets.QLabel(self.widget_2)
        self.main_frame_2.setGeometry(QtCore.QRect(0, 60, 475, 251))
        self.main_frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(186, 189, 182);\n"
"border-radius: 20px")
        self.main_frame_2.setText("")
        self.main_frame_2.setObjectName("main_frame_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 441, 61))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.hdmi_btn_ = QtWidgets.QPushButton(self.widget_2)
        self.hdmi_btn_.setGeometry(QtCore.QRect(40, 290, 230, 55))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.hdmi_btn_.setFont(font)
        self.hdmi_btn_.setStyleSheet("QPushButton {\n"
"   background-color: rgb(192, 32, 52 );\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 0px;\n"
"    border-bottom: 5px solid rgb(162, 2, 22);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 22, 42);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"   border-bottom: 5px solid rgb(162, 2, 22);\n"
"}\n"
"")
        self.hdmi_btn_.setText("")
        self.hdmi_btn_.setObjectName("hdmi_btn_")
        self.mcr_btn_ = QtWidgets.QPushButton(self.widget_2)
        self.mcr_btn_.setGeometry(QtCore.QRect(40, 350, 230, 55))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.mcr_btn_.setFont(font)
        self.mcr_btn_.setStyleSheet("QPushButton {\n"
"   background-color: rgb(192, 32, 52 );\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 0px;\n"
"    border-bottom: 5px solid rgb(162, 2, 22);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 22, 42);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"   border-bottom: 5px solid rgb(162, 2, 22);\n"
"}")
        self.mcr_btn_.setText("")
        self.mcr_btn_.setObjectName("mcr_btn_")
        self.rmt_btn_ = QtWidgets.QPushButton(self.widget_2)
        self.rmt_btn_.setEnabled(True)
        self.rmt_btn_.setGeometry(QtCore.QRect(40, 170, 230, 55))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.rmt_btn_.setFont(font)
        self.rmt_btn_.setStyleSheet("QPushButton {\n"
"   background-color: rgb(192, 32, 52 );\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 0px;\n"
"    border-bottom: 5px solid rgb(162, 2, 22);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 22, 42);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"   border-bottom: 5px solid rgb(162, 2, 22);\n"
"}")
        self.rmt_btn_.setText("")
        self.rmt_btn_.setObjectName("rmt_btn_")
        self.lsr_btn_ = QtWidgets.QPushButton(self.widget_2)
        self.lsr_btn_.setGeometry(QtCore.QRect(40, 230, 230, 55))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lsr_btn_.setFont(font)
        self.lsr_btn_.setStyleSheet("QPushButton {\n"
"   background-color: rgb(192, 32, 52 );\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 0px;\n"
"    border-bottom: 5px solid rgb(162, 2, 22);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 22, 42);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"   border-bottom: 5px solid rgb(162, 2, 22);\n"
"}")
        self.lsr_btn_.setText("")
        self.lsr_btn_.setObjectName("lsr_btn_")
        self.label_27 = QtWidgets.QLabel(self.widget_2)
        self.label_27.setGeometry(QtCore.QRect(20, 170, 5, 235))
        self.label_27.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setGeometry(QtCore.QRect(280, 340, 166, 64))
        self.label_17.setStyleSheet("border-radius: 32px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(206, 22, 40 );")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.confirm = QtWidgets.QPushButton(self.widget_2)
        self.confirm.setGeometry(QtCore.QRect(290, 350, 146, 44))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("QPushButton {\n"
"   background-color: rgb(206, 22, 40 );\n"
"    color: rgb(255, 255, 255 );\n"
"   border-radius: 22px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(226, 42, 60);\n"
"   color: rgb(255, 255, 255 );\n"
"    border-radius: 22px;\n"
"}\n"
"")
        self.confirm.setObjectName("confirm")
        self.timeline = QtWidgets.QLabel(self.widget_2)
        self.timeline.setGeometry(QtCore.QRect(280, 200, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.timeline.setFont(font)
        self.timeline.setStyleSheet("color: rgb(204, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.timeline.setObjectName("timeline")
        self.note = QtWidgets.QLabel(self.widget_2)
        self.note.setGeometry(QtCore.QRect(280, 165, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.note.setFont(font)
        self.note.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.note.setObjectName("note")
        self.line = QtWidgets.QLabel(self.widget_2)
        self.line.setGeometry(QtCore.QRect(280, 225, 161, 2))
        self.line.setStyleSheet("\n"
"background-color: rgb(46, 52, 54);")
        self.line.setText("")
        self.line.setObjectName("line")
        self.you_borrowed = QtWidgets.QLabel(self.widget_2)
        self.you_borrowed.setGeometry(QtCore.QRect(280, 235, 231, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.you_borrowed.setFont(font)
        self.you_borrowed.setStyleSheet("color: rgb(52, 101, 164);\n"
"background-color: rgb(255, 255, 255);")
        self.you_borrowed.setObjectName("you_borrowed")
        self.refirm = QtWidgets.QTextBrowser(self.widget_2)
        self.refirm.setGeometry(QtCore.QRect(280, 255, 171, 71))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.refirm.setFont(font)
        self.refirm.setStyleSheet("color: rgb(52, 101, 164);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"DejaVu Sans\";\n"
"border-radius:0px;")
        self.refirm.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.refirm.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.refirm.setObjectName("refirm")
        self.label_31 = QtWidgets.QLabel(self.widget_2)
        self.label_31.setGeometry(QtCore.QRect(200, 420, 71, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(7)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_31.setObjectName("label_31")
        self.label_29 = QtWidgets.QLabel(self.widget_2)
        self.label_29.setGeometry(QtCore.QRect(59, 420, 81, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(7)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_29.setObjectName("label_29")
        self.label_28 = QtWidgets.QLabel(self.widget_2)
        self.label_28.setGeometry(QtCore.QRect(40, 420, 15, 20))
        self.label_28.setStyleSheet("background-color: rgb(243, 193, 8);")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_32 = QtWidgets.QLabel(self.widget_2)
        self.label_32.setGeometry(QtCore.QRect(181, 420, 16, 20))
        self.label_32.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.laser_cb = QtWidgets.QCheckBox(self.widget_2)
        self.laser_cb.setGeometry(QtCore.QRect(50, 245, 20, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.laser_cb.setFont(font)
        self.laser_cb.setStyleSheet("QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}\n"
"\n"
"")
        self.laser_cb.setObjectName("laser_cb")
        self.micro_cb = QtWidgets.QCheckBox(self.widget_2)
        self.micro_cb.setGeometry(QtCore.QRect(50, 365, 20, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.micro_cb.setFont(font)
        self.micro_cb.setStyleSheet("QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}\n"
"")
        self.micro_cb.setObjectName("micro_cb")
        self.remote_cb = QtWidgets.QCheckBox(self.widget_2)
        self.remote_cb.setGeometry(QtCore.QRect(50, 185, 20, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.remote_cb.setFont(font)
        self.remote_cb.setAutoFillBackground(False)
        self.remote_cb.setStyleSheet("QCheckBox::indicator {\n"
"    color: rgb(255, 255, 255);\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}\n"
"")
        self.remote_cb.setObjectName("remote_cb")
        self.hdmi_cb = QtWidgets.QCheckBox(self.widget_2)
        self.hdmi_cb.setGeometry(QtCore.QRect(50, 305, 20, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.hdmi_cb.setFont(font)
        self.hdmi_cb.setStyleSheet("QCheckBox::indicator {\n"
"     width: 20px;\n"
"     height: 20px;\n"
"}\n"
"")
        self.hdmi_cb.setObjectName("hdmi_cb")
        self.date = QtWidgets.QLabel(self.widget_2)
        self.date.setGeometry(QtCore.QRect(20, 35, 181, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(8)
        font.setItalic(False)
        self.date.setFont(font)
        self.date.setStyleSheet("background-color: rgb(192, 32, 52);border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date.setObjectName("date")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        self.label_15.setEnabled(False)
        self.label_15.setGeometry(QtCore.QRect(90, 180, 101, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(7)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setEnabled(False)
        self.label_16.setGeometry(QtCore.QRect(90, 190, 171, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setEnabled(False)
        self.label_19.setGeometry(QtCore.QRect(90, 240, 101, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(7)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setEnabled(False)
        self.label_20.setGeometry(QtCore.QRect(90, 250, 171, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_2)
        self.label_21.setEnabled(False)
        self.label_21.setGeometry(QtCore.QRect(90, 300, 101, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(7)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.widget_2)
        self.label_22.setEnabled(False)
        self.label_22.setGeometry(QtCore.QRect(90, 310, 171, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_2)
        self.label_23.setEnabled(False)
        self.label_23.setGeometry(QtCore.QRect(90, 360, 101, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(7)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.widget_2)
        self.label_24.setEnabled(False)
        self.label_24.setGeometry(QtCore.QRect(90, 370, 171, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.rmt_btn = QtWidgets.QPushButton(self.widget_2)
        self.rmt_btn.setGeometry(QtCore.QRect(70, 170, 200, 55))
        self.rmt_btn.setStyleSheet("QPushButton {\n"
"background-color: rgba(192, 32, 52, 0);\n"
"   border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgba(164, 0, 0, 50);\n"
"    border-radius: 0px;\n"
"}")
        self.rmt_btn.setText("")
        self.rmt_btn.setObjectName("rmt_btn")
        self.lsr_btn = QtWidgets.QPushButton(self.widget_2)
        self.lsr_btn.setGeometry(QtCore.QRect(70, 230, 200, 55))
        self.lsr_btn.setStyleSheet("QPushButton {\n"
"background-color: rgba(192, 32, 52, 0);\n"
"   border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgba(164, 0, 0, 50);\n"
"    border-radius: 0px;\n"
"}")
        self.lsr_btn.setText("")
        self.lsr_btn.setObjectName("lsr_btn")
        self.hdmi_btn = QtWidgets.QPushButton(self.widget_2)
        self.hdmi_btn.setGeometry(QtCore.QRect(70, 290, 200, 55))
        self.hdmi_btn.setStyleSheet("QPushButton {\n"
"   border-radius: 0px;background-color: rgba(192, 32, 52, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgba(164, 0, 0, 50);\n"
"    border-radius: 0px;\n"
"}")
        self.hdmi_btn.setText("")
        self.hdmi_btn.setObjectName("hdmi_btn")
        self.mcr_btn = QtWidgets.QPushButton(self.widget_2)
        self.mcr_btn.setGeometry(QtCore.QRect(70, 350, 200, 55))
        self.mcr_btn.setStyleSheet("QPushButton {\n"
"   border-radius: 0px;background-color: rgba(192, 32, 52, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgba(164, 0, 0, 50);\n"
"    border-radius: 0px;\n"
"}")
        self.mcr_btn.setText("")
        self.mcr_btn.setObjectName("mcr_btn")
        self.mic_state = QtWidgets.QLabel(self.widget_2)
        self.mic_state.setGeometry(QtCore.QRect(250, 350, 10, 41))
        self.mic_state.setStyleSheet("background-color: rgb(243, 193, 8);")
        self.mic_state.setText("")
        self.mic_state.setObjectName("mic_state")
        self.hdmi_state = QtWidgets.QLabel(self.widget_2)
        self.hdmi_state.setGeometry(QtCore.QRect(250, 290, 10, 41))
        self.hdmi_state.setStyleSheet("background-color: rgb(243, 193, 8);")
        self.hdmi_state.setText("")
        self.hdmi_state.setObjectName("hdmi_state")
        self.laser_state = QtWidgets.QLabel(self.widget_2)
        self.laser_state.setGeometry(QtCore.QRect(250, 230, 10, 41))
        self.laser_state.setStyleSheet("background-color: rgb(243, 193, 8);")
        self.laser_state.setText("")
        self.laser_state.setObjectName("laser_state")
        self.remote_state = QtWidgets.QLabel(self.widget_2)
        self.remote_state.setGeometry(QtCore.QRect(250, 170, 10, 41))
        self.remote_state.setStyleSheet("background-color: rgb(243, 193, 8);")
        self.remote_state.setText("")
        self.remote_state.setObjectName("remote_state")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(235, 10, 230, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Condensed")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(192, 32, 52);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(210, 20, 20, 23))
        self.label_12.setStyleSheet("background-color: rgb(192, 32, 52);image: url(:/newPrefix/logoHUST.png);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(235, 30, 230, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Condensed")
        font.setPointSize(7)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(192, 32, 52);color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.today = QtWidgets.QLabel(self.widget_2)
        self.today.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.today.setFont(font)
        self.today.setStyleSheet("background-color: rgb(192, 32, 52);\n"
"color: rgb(255, 255, 255);")
        self.today.setObjectName("today")
        self.label_10.raise_()
        self.main_frame_2.raise_()
        self.main_frame.raise_()
        self.label_2.raise_()
        self.hdmi_btn_.raise_()
        self.mcr_btn_.raise_()
        self.rmt_btn_.raise_()
        self.lsr_btn_.raise_()
        self.label_27.raise_()
        self.timeline.raise_()
        self.note.raise_()
        self.line.raise_()
        self.you_borrowed.raise_()
        self.refirm.raise_()
        self.label_17.raise_()
        self.confirm.raise_()
        self.label_31.raise_()
        self.label_29.raise_()
        self.label_28.raise_()
        self.label_32.raise_()
        self.laser_cb.raise_()
        self.micro_cb.raise_()
        self.remote_cb.raise_()
        self.hdmi_cb.raise_()
        self.date.raise_()
        self.label_16.raise_()
        self.label_20.raise_()
        self.label_22.raise_()
        self.label_24.raise_()
        self.mic_state.raise_()
        self.hdmi_state.raise_()
        self.laser_state.raise_()
        self.remote_state.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_15.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.label_19.raise_()
        self.rmt_btn.raise_()
        self.lsr_btn.raise_()
        self.hdmi_btn.raise_()
        self.mcr_btn.raise_()
        self.today.raise_()
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.building.setText(_translate("Dialog", "HUST D6"))
        self.QR_2.setText(_translate("Dialog", "TextLabel"))
        self.continue_.setText(_translate("Dialog", "TIẾP TỤC"))
        self.label_5.setText(_translate("Dialog", "TIẾT HỌC SẮP DIỄN RA"))
        self.subject.setText(_translate("Dialog", "Công nghệ chế tạo máy"))
        self.start.setText(_translate("Dialog", "12:30"))
        self.room.setText(_translate("Dialog", "Phòng 304 - D6"))
        self.code.setText(_translate("Dialog", "717196 "))
        self.label_.setText(_translate("Dialog", "|"))
        self.end.setText(_translate("Dialog", "14:55"))
        self.name.setText(_translate("Dialog", "Đặng Trần Bách"))
        self.email.setText(_translate("Dialog", "Email: Bach.dt190103@sis.hust.edu.vn"))
        self.label_8.setText(_translate("Dialog", "Sđt:"))
        self.label.setText(_translate("Dialog", "Bạn chưa chọn thiết bị nào!"))
        self.label_2.setText(_translate("Dialog", "CHỌN THIẾT BỊ"))
        self.confirm.setText(_translate("Dialog", "XÁC NHẬN MƯỢN"))
        self.timeline.setText(_translate("Dialog", "Chủ Nhật, ngày 19/05, lúc 07:30"))
        self.note.setText(_translate("Dialog", "GHI CHÚ"))
        self.you_borrowed.setText(_translate("Dialog", "THIẾT BỊ MƯỢN:"))
        self.refirm.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">     01 ĐIỀU KHIỂN </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">     01 BÚT LASER<br />     01 MÍC DI ĐỘNG<br />     01 CÁP HDMI</span></p></body></html>"))
        self.label_31.setText(_translate("Dialog", "Thiết bị đã hết"))
        self.label_29.setText(_translate("Dialog", "Thiết bị sẵn sàng"))
        self.laser_cb.setText(_translate("Dialog", "     Bút Laser"))
        self.micro_cb.setText(_translate("Dialog", "     Míc "))
        self.remote_cb.setText(_translate("Dialog", "     Điều khiển điều hòa"))
        self.hdmi_cb.setText(_translate("Dialog", "     Cáp HDMI"))
        self.date.setText(_translate("Dialog", " ngày 10 tháng 11 năm 2022"))
        self.label_15.setText(_translate("Dialog", "THIẾT BỊ"))
        self.label_16.setText(_translate("Dialog", "ĐIỀU KHIỂN "))
        self.label_19.setText(_translate("Dialog", "THIẾT BỊ"))
        self.label_20.setText(_translate("Dialog", "BÚT LASER"))
        self.label_21.setText(_translate("Dialog", "THIẾT BỊ"))
        self.label_22.setText(_translate("Dialog", "DÂY CÁP HDMI"))
        self.label_23.setText(_translate("Dialog", "THIẾT BỊ"))
        self.label_24.setText(_translate("Dialog", "MÍC DI ĐỘNG"))
        self.label_11.setText(_translate("Dialog", "TRƯỜNG ĐẠI HỌC BÁCH KHOA HÀ NỘI"))
        self.label_13.setText(_translate("Dialog", "HANOI UNIVERSITY OF SCIENCE AND TECHNOLOGY"))
        self.today.setText(_translate("Dialog", "Chủ Nhật"))
import Images_rc