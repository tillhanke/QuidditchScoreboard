# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timekeeper_connect.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Timekeeper(object):
    def setupUi(self, Timekeeper):
        Timekeeper.setObjectName("Timekeeper")
        Timekeeper.resize(1272, 471)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Timekeeper)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Timekeeper)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gameID = QtWidgets.QLineEdit(Timekeeper)
        self.gameID.setObjectName("gameID")
        self.horizontalLayout.addWidget(self.gameID)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Timekeeper)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.auth = QtWidgets.QLineEdit(Timekeeper)
        self.auth.setObjectName("auth")
        self.horizontalLayout_2.addWidget(self.auth)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connectButton = QtWidgets.QPushButton(Timekeeper)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_3.addWidget(self.connectButton)
        self.closeButton = QtWidgets.QPushButton(Timekeeper)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Timekeeper)
        self.connectButton.clicked.connect(Timekeeper.connect)
        self.closeButton.clicked.connect(Timekeeper.close)
        QtCore.QMetaObject.connectSlotsByName(Timekeeper)

    def retranslateUi(self, Timekeeper):
        _translate = QtCore.QCoreApplication.translate
        Timekeeper.setWindowTitle(_translate("Timekeeper", "Timekeeper"))
        self.label.setText(_translate("Timekeeper", "Game ID"))
        self.label_2.setText(_translate("Timekeeper", "Authentifizierung"))
        self.connectButton.setText(_translate("Timekeeper", "Connect"))
        self.closeButton.setText(_translate("Timekeeper", "Close"))

