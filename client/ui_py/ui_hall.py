# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\client\ui\ui_hall.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_hall(object):
    def setupUi(self, hall):
        hall.setObjectName("hall")
        hall.resize(529, 1109)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_channels = QtWidgets.QListWidget(hall)
        self.listWidget_channels.setObjectName("listWidget_channels")
        self.verticalLayout.addWidget(self.listWidget_channels)
        hall.setLayout(self.verticalLayout)

        self.retranslateUi(hall)
        QtCore.QMetaObject.connectSlotsByName(hall)

    def retranslateUi(self, hall):
        pass

