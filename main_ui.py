# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scores.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

def clickable(widget):
        class Filter(QtCore.QObject):
            clicked = QtCore.pyqtSignal()
            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QtCore.QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True
                return False
        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

class Ui_main(object):
    def setupUi(self, main):

        main.setObjectName("main")
        #main.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, QtWidgets.QDesktopWidget().screenGeometry(-1).width(), QtWidgets.QDesktopWidget().screenGeometry(-1).height()))
        self.tabWidget.setObjectName("tabWidget")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tabWidget.addTab(self.tab1, "")

        #self.tab2 = QtWidgets.QWidget()
        #self.tab2.setObjectName("tab2")
        #self.tabWidget.addTab(self.tab2, "")

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tabWidget.addTab(self.tab3, "")


        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout.setContentsMargins(50, 100, 50, 100)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.time_header = QtWidgets.QLabel(main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_header.sizePolicy().hasHeightForWidth())
        self.time_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.time_header.setFont(font)
        self.time_header.setTextFormat(QtCore.Qt.AutoText)
        self.time_header.setAlignment(QtCore.Qt.AlignCenter)
        self.time_header.setObjectName("time_header")
        self.gridLayout_2.addWidget(self.time_header, 0, 0, 1, 1)
        self.timerLayout = QtWidgets.QHBoxLayout()
        self.timerLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLayout.setObjectName("timerLayout")
        spacerItem_tl = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timerLayout.addItem(spacerItem_tl)
        self.startTimer = QtWidgets.QPushButton(main)
        self.startTimer.setFixedSize(120, 100)
        self.startTimer.setObjectName("startTimer")
        self.timerLayout.addWidget(self.startTimer)
        self.stopTimer = QtWidgets.QPushButton(main)
        self.stopTimer.setFixedSize(120, 100)
        self.stopTimer.setObjectName("stopTimer")
        self.timerLayout.addWidget(self.stopTimer)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.setTimer = QtWidgets.QPushButton(main)
        self.setTimer.setFixedSize(120, 70)
        self.setTimer.setObjectName("setTimer")
        self.verticalLayout_3.addWidget(self.setTimer)
        self.timeEdit = QtWidgets.QTimeEdit(main)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_3.addWidget(self.timeEdit)
        self.timerLayout.addLayout(self.verticalLayout_3)
        spacerItem_tl2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timerLayout.addItem(spacerItem_tl2)
        self.gridLayout_2.addLayout(self.timerLayout, 2, 0, 1, 1)
        self.time_label = QtWidgets.QLabel(main)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.time_label.setFont(font)
        self.time_label.setTextFormat(QtCore.Qt.AutoText)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.gridLayout_2.addWidget(self.time_label, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.extratimerButton = QtWidgets.QPushButton(main)
        self.extratimerButton.setObjectName("extratimerButton")
        self.horizontalLayout_4.addWidget(self.extratimerButton)
        self.extratimerButton.setFixedWidth(200)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(main)
        self.line.setMinimumSize(QtCore.QSize(0, 8))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.score_header = QtWidgets.QLabel(main)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.score_header.sizePolicy().hasHeightForWidth())
        self.score_header.setSizePolicy(sizePolicy)
        self.score_header.setBaseSize(QtCore.QSize(3, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.score_header.setFont(font)
        self.score_header.setAlignment(QtCore.Qt.AlignCenter)
        self.score_header.setObjectName("score_header")
        self.verticalLayout_4.addWidget(self.score_header)
        self.scoreLayout = QtWidgets.QGridLayout()
        self.scoreLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.scoreLayout.setHorizontalSpacing(0)
        self.scoreLayout.setVerticalSpacing(0)
        self.scoreLayout.setObjectName("scoreLayout")
        self.score_labels = QtWidgets.QHBoxLayout()
        self.score_labels.setSpacing(0)
        self.score_labels.setObjectName("score_labels")

        self.oss_label = QtWidgets.QLabel(main)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.oss_label.sizePolicy().hasHeightForWidth())
        self.oss_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.oss_label.setFont(font)
        self.oss_label.setTextFormat(QtCore.Qt.AutoText)
        self.oss_label.setAlignment(QtCore.Qt.AlignCenter)
        self.oss_label.setObjectName("oss_label")
        self.scoreLayout.addWidget(self.oss_label, 2, 2)

        self.score_left = QtWidgets.QLabel(main)
        self.score_left.setFixedSize(250, 300)
        font = QtGui.QFont()
        font.setPointSize(60)
        self.score_left.setFont(font)
        self.score_left.setObjectName("score_left")
        self.score_labels.addWidget(self.score_left)
        self.point = QtWidgets.QLabel(main)
        self.point.setFixedSize(40, 80)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.point.setFont(font)
        self.point.setAlignment(QtCore.Qt.AlignCenter)
        self.point.setObjectName("point")
        self.score_labels.addWidget(self.point)
        self.score_right = QtWidgets.QLabel(main)
        self.score_right.setFixedSize(250, 300)
        font = QtGui.QFont()
        font.setPointSize(60)
        self.score_right.setFont(font)
        self.score_left.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score_right.setObjectName("score_right")
        self.score_labels.addWidget(self.score_right)
        self.scoreLayout.addLayout(self.score_labels, 0, 2)
        #self.scoreLayout.addWidget(self.score_left, 0, 2)
        #self.scoreLayout.addWidget(self.point, 0, 3)
        #self.scoreLayout.addWidget(self.score_right, 0, 4)
        self.scorebutton_left = QtWidgets.QVBoxLayout()
        self.scorebutton_left.setSpacing(0)
        self.scorebutton_left.setObjectName("scorebutton_left")
        self.add10_left = QtWidgets.QPushButton(main)
        self.add10_left.setFixedSize(100, 80)
        self.add10_left.setDefault(False)
        self.add10_left.setFlat(False)
        self.add10_left.setObjectName("add10_left")
        self.scorebutton_left.addWidget(self.add10_left)
        self.resetscore_left = QtWidgets.QPushButton(main)
        self.resetscore_left.setFixedSize(100, 80)
        self.resetscore_left.setObjectName("resetscore_left")
        self.scorebutton_left.addWidget(self.resetscore_left)
        self.sub10_left = QtWidgets.QPushButton(main)
        self.sub10_left.setFixedSize(100, 80)
        self.sub10_left.setObjectName("sub10_left")
        self.scorebutton_left.addWidget(self.sub10_left)
        self.scoreLayout.addLayout(self.scorebutton_left, 0, 1)
        self.scorebutton_right = QtWidgets.QVBoxLayout()
        self.scorebutton_right.setSpacing(0)
        self.scorebutton_right.setObjectName("scorebutton_right")
        self.add10_right = QtWidgets.QPushButton(main)
        self.add10_right.setFixedSize(100, 80)
        self.add10_right.setObjectName("add10_right")
        self.scorebutton_right.addWidget(self.add10_right)
        self.resetscore_right = QtWidgets.QPushButton(main)
        self.resetscore_right.setFixedSize(100, 80)
        self.resetscore_right.setObjectName("resetscore_right")
        self.scorebutton_right.addWidget(self.resetscore_right)
        self.sub10_right = QtWidgets.QPushButton(main)
        self.sub10_right.setFixedSize(100, 80)
        self.sub10_right.setObjectName("sub10_right")
        self.scorebutton_right.addWidget(self.sub10_right)
        self.scoreLayout.addLayout(self.scorebutton_right, 0, 3)
        self.teamname_left = QtWidgets.QLabel(main)
        self.teamname_left.setWordWrap(True)
        self.teamname_left.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.teamname_left.setFixedHeight(300)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamname_left.setFont(font)
        self.teamname_left.setObjectName("teamname_left")
        self.scoreLayout.addWidget(self.teamname_left, 0, 0)
        self.teamname_right = QtWidgets.QLabel(main)
        self.teamname_right.setWordWrap(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamname_right.setFont(font)
        #self.teamname_right.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.teamname_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.teamname_right.setObjectName("teamname_right")
        self.scoreLayout.addWidget(self.teamname_right, 0, 4)
        #self.scoreLayout.setColumnMinimumWidth(2, 250)
        #self.scoreLayout.setColumnMinimumWidth(4, 250)
        #self.scoreLayout.setColumnStretch(0, 6)
        #self.scoreLayout.setColumnStretch(1, 6)
        #self.scoreLayout.setColumnStretch(2, 1)
        #self.scoreLayout.setColumnStretch(3, 1)
        #self.scoreLayout.setColumnStretch(4, 1)
        #self.scoreLayout.setColumnStretch(5, 6)
        #self.scoreLayout.setColumnStretch(6, 6)
        #self.scoreLayout.setHorizontalSpacing(0)
        self.verticalLayout_4.addLayout(self.scoreLayout)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        #self.horizontalLayout = QtWidgets.QHBoxLayout()
        #self.horizontalLayout.setObjectName("horizontalLayout")
        #spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.horizontalLayout.addItem(spacerItem)
        
        #self.snitchCatchButton = QtWidgets.QPushButton(main)
        #font = QtGui.QFont()
        #font.setPointSize(15)
        #font.setBold(True)
        #font.setWeight(75)
        #self.snitchCatchButton.setFont(font)
        #self.snitchCatchButton.setObjectName("snitchCatchButton")
        #self.horizontalLayout.addWidget(self.snitchCatchButton)
        spacerItem = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.snitchcatch_layout = QtWidgets.QHBoxLayout()
        self.snitchcatch_layout.setObjectName("snitchcatch_layout")
        self.snitchcatch_layout.addStretch()
        self.snitchcatch_layout.setSpacing(200)
        self.snitchcatch_left = QtWidgets.QPushButton(main)
        #self.snitchcatch_left.setFixedSize(70, 50)
        self.snitchcatch_left.setObjectName("snitchcatch_left")
        self.snitchcatch_right = QtWidgets.QPushButton(main)
        #self.snitchcatch_right.setFixedSize(70, 50)
        self.snitchcatch_right.setObjectName("snitchcatch_right")
        self.snitchcatch_left.setEnabled(True)
        self.snitchcatch_right.setEnabled(True)
        self.snitchcatch_layout.addWidget(self.snitchcatch_left)
        self.snitchcatch_layout.addWidget(self.snitchcatch_right)
        self.snitchcatch_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.snitchcatch_layout)
        self.snitchcatch_layout.setAlignment(self.verticalLayout, QtCore.Qt.AlignHCenter)
        #spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.horizontalLayout.addItem(spacerItem1)
        #self.verticalLayout.addLayout(self.horizontalLayout)
        #self.label = QtWidgets.QLabel(main)
        #self.label.setAlignment(QtCore.Qt.AlignCenter)
        #self.label.setObjectName("label")
        #self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.settingsButton = QtWidgets.QPushButton(main)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout_5.addWidget(self.settingsButton)
        self.timekeeperButton = QtWidgets.QPushButton(main)
        self.timekeeperButton.setObjectName("timekeeperButton")
        self.horizontalLayout_5.addWidget(self.timekeeperButton)
        self.penaltyButton = QtWidgets.QPushButton(main)
        self.penaltyButton.setObjectName("penaltyButton")
        self.horizontalLayout_5.addWidget(self.penaltyButton)
        self.closeButton = QtWidgets.QPushButton(main)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_5.addWidget(self.closeButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.stopTimer.setEnabled(False)

        self.scLayout = QtWidgets.QVBoxLayout(self.tab3)
        self.scLayout.setContentsMargins(50, 50, 50, 100)
        self.scLayout.setObjectName("scLayout")
        self.scLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.scLayout.setAlignment(QtCore.Qt.AlignTop)

        self.horizontalLayout_sc = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sc.setObjectName("horizontalLayout_sc")

        self.scorecrawlButton = QtWidgets.QPushButton()
        self.scorecrawlButton.setObjectName("scorecrawlButton")
        self.scorecrawlButton.setFixedWidth(220)
        self.scorecrawlButton.setFixedHeight(80)
        self.horizontalLayout_sc.addWidget(self.scorecrawlButton)

        self.readGameIDs = QtWidgets.QPushButton()
        self.readGameIDs.setObjectName("readGameIDs")
        self.readGameIDs.setFixedWidth(220)
        self.readGameIDs.setFixedHeight(80)
        self.horizontalLayout_sc.addWidget(self.readGameIDs)

        self.horizontalLayout_sc.setAlignment(self.scorecrawlButton, QtCore.Qt.AlignCenter)
        self.horizontalLayout_sc.setAlignment(self.scorecrawlButton, QtCore.Qt.AlignTop)
        self.horizontalLayout_sc.setAlignment(self.readGameIDs, QtCore.Qt.AlignCenter)
        self.horizontalLayout_sc.setAlignment(self.readGameIDs, QtCore.Qt.AlignTop)

        self.scLayout.addLayout(self.horizontalLayout_sc)

        self.scroll = QtWidgets.QScrollArea()
        self.scLayout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scrollcontent = QtWidgets.QWidget(self.scroll)
        self.scrolllayout = QtWidgets.QVBoxLayout(self.scrollcontent)
        self.scrolllayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollcontent.setLayout(self.scrolllayout)
        self.scroll.setWidget(self.scrollcontent)

        self.retranslateUi(main)
        self.add10_left.clicked.connect(lambda x: main.add_left(10))
        self.sub10_left.clicked.connect(lambda x: main.add_left(-10))
        self.add10_right.clicked.connect(lambda x: main.add_right(10))
        self.sub10_right.clicked.connect(lambda x: main.add_right(-10))
        self.startTimer.clicked.connect(main.start_timer)
        self.stopTimer.clicked.connect(main.stop_timer)
        self.setTimer.clicked.connect(main.set_timer)
        self.resetscore_left.clicked.connect(main.reset_left)
        self.resetscore_right.clicked.connect(main.reset_right)
        self.closeButton.clicked.connect(main.close)
        self.timekeeperButton.clicked.connect(main.timekeeper_start)
        self.settingsButton.clicked.connect(main.settings_start)
        self.penaltyButton.clicked.connect(main.open_penalty)
        self.snitchcatch_left.clicked.connect(main.snitch_catch_left)
        self.snitchcatch_right.clicked.connect(main.snitch_catch_right)
        self.extratimerButton.clicked.connect(main.add_timer)
        self.scorecrawlButton.clicked.connect(main.scorecrawl_start)
        self.readGameIDs.clicked.connect(main.read_gameids_sc)
        clickable(self.oss_label).connect(main.delete_oss)
        QtCore.QMetaObject.connectSlotsByName(main)



    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Main"))
        self.time_header.setText(_translate("main", "Game Time"))
        self.startTimer.setText(_translate("main", "Start"))
        self.stopTimer.setText(_translate("main", "Stop"))
        self.setTimer.setText(_translate("main", "Set"))
        self.timeEdit.setDisplayFormat(_translate("main", "mm:ss"))
        self.time_label.setText(_translate("main", "00:00"))
        self.extratimerButton.setText(_translate("main", "Get extra timer"))
        self.score_header.setText(_translate("main", "Scores"))
        self.score_left.setText(_translate("main", "score"))
        self.point.setText(_translate("main", ":"))
        self.score_right.setText(_translate("main", "score"))
        self.add10_left.setText(_translate("main", "+10"))
        self.resetscore_left.setText(_translate("main", "reset"))
        self.sub10_left.setText(_translate("main", "-10"))
        self.add10_right.setText(_translate("main", "+10"))
        self.resetscore_right.setText(_translate("main", "reset"))
        self.sub10_right.setText(_translate("main", "-10"))
        self.teamname_left.setText(_translate("main", "Team A"))
        self.teamname_right.setText(_translate("main", "Team B"))
        self.snitchcatch_left.setText(_translate("main", "Catch"))
        self.snitchcatch_right.setText(_translate("main", "Catch"))
        self.settingsButton.setText(_translate("main", "Settings"))
        self.timekeeperButton.setText(_translate("main", "Start Timekeeper"))
        self.penaltyButton.setText(_translate("main", "Set Penalty"))
        self.closeButton.setText(_translate("main", "Close"))
        self.scorecrawlButton.setText(_translate("main", "Start score crawl"))
        self.readGameIDs.setText(_translate("main", "Read GameIDs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("main", "Main Window"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("main", "Extra Timers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("main", "Score Crawl"))