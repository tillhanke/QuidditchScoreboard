# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sureBro.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sureBro(object):
    def setupUi(self, sureBro):
        sureBro.setObjectName("sureBro")
        sureBro.resize(1595, 1039)
        self.verticalLayout = QtWidgets.QVBoxLayout(sureBro)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(sureBro)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(sureBro)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(sureBro)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(sureBro)
        self.pushButton_2.clicked.connect(sureBro.yes)
        self.pushButton.clicked.connect(sureBro.no)
        QtCore.QMetaObject.connectSlotsByName(sureBro)

    def retranslateUi(self, sureBro):
        _translate = QtCore.QCoreApplication.translate
        sureBro.setWindowTitle(_translate("sureBro", "Dialog"))
        self.label.setText(_translate("sureBro", "Really wanna close this pal?"))
        self.pushButton_2.setText(_translate("sureBro", "Yea sure!"))
        self.pushButton.setText(_translate("sureBro", "No please take me back."))

