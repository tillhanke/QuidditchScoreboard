'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snitch_catch.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SnitchCatch(object):
    def setupUi(self, SnitchCatch):
        SnitchCatch.setObjectName("SnitchCatch")
        SnitchCatch.resize(1133, 606)
        self.verticalLayout = QtWidgets.QVBoxLayout(SnitchCatch)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teamLeftButton = QtWidgets.QRadioButton(SnitchCatch)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamLeftButton.setFont(font)
        self.teamLeftButton.setObjectName("teamLeftButton")
        self.horizontalLayout.addWidget(self.teamLeftButton)
        self.teamRightButton = QtWidgets.QRadioButton(SnitchCatch)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamRightButton.setFont(font)
        self.teamRightButton.setObjectName("teamRightButton")
        self.horizontalLayout.addWidget(self.teamRightButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.okButton = QtWidgets.QPushButton(SnitchCatch)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(SnitchCatch)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SnitchCatch)
        self.cancelButton.clicked.connect(SnitchCatch.accept)
        self.okButton.clicked.connect(SnitchCatch.save)
        QtCore.QMetaObject.connectSlotsByName(SnitchCatch)

    def retranslateUi(self, SnitchCatch):
        _translate = QtCore.QCoreApplication.translate
        SnitchCatch.setWindowTitle(_translate("SnitchCatch", "Snitch Catch"))
        self.teamLeftButton.setText(_translate("SnitchCatch", "Team Left"))
        self.teamRightButton.setText(_translate("SnitchCatch", "Team Right"))
        self.okButton.setText(_translate("SnitchCatch", "Ok"))
        self.cancelButton.setText(_translate("SnitchCatch", "Cancel"))

'''