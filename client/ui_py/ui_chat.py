# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\client\ui\ui_chat.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chatWindow(object):
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(738, 630)
        self.verticalLayout = QtWidgets.QVBoxLayout(chatWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_channelName = QtWidgets.QLabel(chatWindow)
        self.label_channelName.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 170, 0);\n"
"}")
        self.label_channelName.setTextFormat(QtCore.Qt.RichText)
        self.label_channelName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_channelName.setObjectName("label_channelName")
        self.verticalLayout.addWidget(self.label_channelName)
        self.line_2 = QtWidgets.QFrame(chatWindow)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.textBrowser_show = QtWidgets.QTextBrowser(chatWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser_show.sizePolicy().hasHeightForWidth())
        self.textBrowser_show.setSizePolicy(sizePolicy)
        self.textBrowser_show.setObjectName("textBrowser_show")
        self.verticalLayout.addWidget(self.textBrowser_show)
        self.line = QtWidgets.QFrame(chatWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.textEdit_input = QtWidgets.QTextEdit(chatWindow)
        self.textEdit_input.setObjectName("textEdit_input")
        self.verticalLayout.addWidget(self.textEdit_input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_sendFile = QtWidgets.QPushButton(chatWindow)
        self.pushButton_sendFile.setObjectName("pushButton_sendFile")
        self.horizontalLayout.addWidget(self.pushButton_sendFile)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_send = QtWidgets.QPushButton(chatWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_send.sizePolicy().hasHeightForWidth())
        self.pushButton_send.setSizePolicy(sizePolicy)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout.addWidget(self.pushButton_send)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(chatWindow)
        QtCore.QMetaObject.connectSlotsByName(chatWindow)

    def retranslateUi(self, chatWindow):
        _translate = QtCore.QCoreApplication.translate
        chatWindow.setWindowTitle(_translate("chatWindow", "Form"))
        self.label_channelName.setText(_translate("chatWindow", "TextLabel"))
        self.pushButton_sendFile.setText(_translate("chatWindow", "选择文件"))
        self.pushButton_send.setText(_translate("chatWindow", "发送"))

