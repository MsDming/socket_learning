# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\client\ui\ui_hall.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hall(object):
    def setupUi(self, hall):
        hall.setObjectName("hall")
        hall.resize(420, 782)
        hall.setMinimumSize(QtCore.QSize(420, 782))
        hall.setMaximumSize(QtCore.QSize(592, 1118))
        self.centralwidget = QtWidgets.QWidget(hall)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_channels = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_channels.setObjectName("listWidget_channels")
        self.verticalLayout_2.addWidget(self.listWidget_channels)
        hall.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hall)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 30))
        self.menubar.setObjectName("menubar")
        hall.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hall)
        self.statusbar.setObjectName("statusbar")
        hall.setStatusBar(self.statusbar)

        self.retranslateUi(hall)
        QtCore.QMetaObject.connectSlotsByName(hall)

    def retranslateUi(self, hall):
        _translate = QtCore.QCoreApplication.translate
        hall.setWindowTitle(_translate("hall", "OO聊天室"))

