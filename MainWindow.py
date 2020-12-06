from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
import os
import io
from PIL import Image, ImageDraw
import shutil
#import websocket
import time
import urllib.request
import json
import math
import threading
import sys
import codecs
import subprocess
from Scoreboard import ScoreBoard
from main_ui import Ui_main
from SureBro import SureBro
from TimekeeperWindow import TimekeeperWindow
from Penalty import PenaltyWindow
from Settings import SettingsWindow
#from SnitchCatch import SnitchCatchWindow
from Extra_Timer import ExtraTimerWindow
from timekeeper import Timekeeper

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.scoreboard = ScoreBoard(self)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        #self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        #self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.showMaximized()
        self.really_ui = SureBro(self)
        # in case of restart
        self.scoreboard.read_all()
        self.set_from_scoreboard()

        self.timekeeper_w = TimekeeperWindow(self.scoreboard, self)
        self.penalty_w = PenaltyWindow(self.scoreboard)
        self.settings_w = SettingsWindow(self.scoreboard, self)
        self.settings_w.show()
        #self.snitch_w = SnitchCatchWindow(self.scoreboard, self)
        self.extra_timers = []

        time_thread = threading.Thread(target=self.update_timer_ui)
        time_thread.start()
        # self.ui.timekeeperButton.deleteLater()
        
        new_penalty_thread = threading.Thread(target=self.new_penalty)
        new_penalty_thread.start()
        
        self.scorecrawl_connected = 0

    def set_from_scoreboard(self):
        self.ui.time_label.setText(self.scoreboard.time.time_str)
        self.update_score_ui()
        self.update_team_ui()

    def add_timer(self):
        '''
        if(self.ui.extratimerButtonchecked == False):
            self.ui.expand(self)
            self.ui.extratimerButton.setText("Close extra timer")
        elif(self.ui.extratimerButtonchecked == True):
            self.ui.shrink(self)
            self.ui.extratimerButton.setText("Get extra timer")
        '''
        self.extra_timers.append(ExtraTimerWindow())
        self.extra_timers[-1].show()

    def start_timer(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.time.start()
        self.ui.stopTimer.setEnabled(True)
        self.ui.startTimer.setEnabled(False)
        self.ui.snitchcatch_right.setEnabled(False)
        self.ui.snitchcatch_left.setEnabled(False)

    def stop_timer(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.time.stop()
        self.ui.stopTimer.setEnabled(False)
        self.ui.startTimer.setEnabled(True)
        self.ui.snitchcatch_right.setEnabled(True)
        self.ui.snitchcatch_left.setEnabled(True)

    def set_timer(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        time = self.ui.timeEdit.time()
        self.scoreboard.time.set(ui_label=self.ui.time_label, minutes=time.minute(), seconds=time.second())

    def add_left(self, amount):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamleft.score += amount
        self.update_score_ui()

    def reset_left(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamleft.score = 0
        self.scoreboard.teamleft.snitch_catch = []
        self.update_score_ui()

    def reset_right(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamright.score = 0
        self.scoreboard.teamright.snitch_catch = []
        self.update_score_ui()

    def add_right(self, amount):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamright.score += amount
        self.update_score_ui()

    def timekeeper_start(self):
        if self.timekeeper_w.timekeeper.connected:
            self.timekeeper_w.timekeeper.break_connection = True
            #self.timekeeper_w.timekeeper.ws.keep_running = False
            self.timekeeper_w.timekeeper.connected = False
            self.scoreboard.read_all()
            self.timekeeper_w.disconnect()
            print("Disconnected Timekeeper")
            self.ui.timekeeperButton.setText("Start Timekeeper")
            return
        else:
            self.scoreboard.read_all()
            self.timekeeper_w.show()

    def settings_start(self):
        self.settings_w.show()

    def snitch_catch_left(self):
        self.scoreboard.teamleft.snitch_catch.append(True)
        self.scoreboard.teamright.snitch_catch.append(False)
        self.add_left(30)
        self.scoreboard.write_score()

    def snitch_catch_right(self):
        self.scoreboard.teamleft.snitch_catch.append(False)
        self.scoreboard.teamright.snitch_catch.append(True)
        self.add_right(30)
        self.scoreboard.write_score()

    '''
    def snitch_catch(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        if self.scoreboard.time.running:
            return
        self.snitch_w.ui.teamRightButton.setText(self.scoreboard.teamright.name)
        self.snitch_w.ui.teamLeftButton.setText(self.scoreboard.teamleft.name)
        self.scoreboard.time.stop()
        self.snitch_w.show()
    '''

    def open_penalty(self):
        self.penalty_w = PenaltyWindow(self.scoreboard)
        self.penalty_w.show()
        self.penalty_w.on_open()

    def update_team_ui(self):
        self.ui.teamname_left.setText(self.scoreboard.teamleft.name)
        self.ui.teamname_right.setText(self.scoreboard.teamright.name)

    def update_timer_ui(self):
        while self.result() == 0:
            if self.timekeeper_w.timekeeper.connected:
                gametime = open("Output/timer.csv", "r", encoding="utf-8").readlines()[1]
                if(str(self.scoreboard.teamleft.get_score_str()) != open("Output/score_left.csv", "r").read() or str(self.scoreboard.teamright.get_score_str()) != open("Output/score_right.csv", "r").read()):
                   self.update_score_ui_tk()
            else:
                gametime = self.scoreboard.time.time_str
            self.ui.time_label.setText(gametime)
            time.sleep(0.5)

    def update_score_ui(self):
        self.ui.score_left.setText(str(self.scoreboard.teamleft.get_score_str()))
        self.ui.score_right.setText(str(self.scoreboard.teamright.get_score_str()))
        self.scoreboard.write_score()
    def new_penalty(self):
        alt = 0
        '''
        while self.result() == 0:
            alt = (alt+1)%2
            if self.timekeeper_w.timekeeper.connected:
                new_penalty = open("quidditchlive_api/new_penalty.txt").read()
                if(new_penalty == "1"):
                    if(alt == 0):
                        self.ui.penaltyButton.setStyleSheet('background-color: #D77D00')
                    else:
                        self.ui.penaltyButton.setStyleSheet('background-color: #C0C0C0')
                elif(new_penalty == "2"):
                    if(alt == 0):
                        self.ui.penaltyButton.setStyleSheet('background-color: #228B22')
                    else:
                        self.ui.penaltyButton.setStyleSheet('background-color: #C0C0C0')
                else:
                    self.ui.penaltyButton.setStyleSheet('background-color: #C0C0C0')
            time.sleep(0.5)
        '''
    def close(self):
        self.scoreboard.time.stop()
        self.really_ui.show()

    def update_score_ui_tk(self):
        score_left = open("Output/score_left.csv", "r").readlines()[1]
        score_right = open("Output/score_right.csv", "r").readlines()[1]
        self.ui.score_left.setText(score_left)
        self.ui.score_right.setText(score_right)

    def scorecrawl_start(self):
        if(self.scorecrawl_connected == False):
            self.connect_sc()
            self.ui.scorecrawlButton.setText("Stop score crawl")
        else:
            self.disconnect_sc()
            self.ui.scorecrawlButton.setText("Start score crawl")
    
    def connect_sc(self):
        sc_file = open("quidditchlive_api/GameIDs_ScoreCrawl.txt", "w")
        sc_file.write("")
        sc_file.close()
        sc_file = open("quidditchlive_api/GameIDs_ScoreCrawl.txt", "a")
        first = 1
        for i in range(self.ui.scrolllayout.count()):
            if(self.ui.scrolllayout.itemAt(i).widget().isChecked()):
                if(first == 0):
                    sc_file.write("\n")
                sc_file.write(self.ui.scrolllayout.itemAt(i).widget().text()[:13])
                first = 0
        sc_file.close()

        self.scorecrawl_proc = subprocess.Popen('node .\quidditchlive_api\quidditchlive_scorecrawl.js')
        self.scorecrawl_connected = True

    def disconnect_sc(self):
        self.scorecrawl_proc.kill()
        print("Quidditch Score Crawl disconnected.")
        self.scorecrawl_connected = False

    def read_gameids_sc(self):
        open("quidditchlive_api/gameidstonames.txt", "w").write("")
        self.gameidstonames_proc = subprocess.Popen('node .\quidditchlive_api\quidditchlive_gameidtonames.js')
        time.sleep(3)
        self.gameidstonames_proc.kill()
        for i in reversed(range(self.ui.scrolllayout.count())): 
            self.ui.scrolllayout.itemAt(i).widget().setParent(None)
        with open("quidditchlive_api/gameidstonames.txt") as f:
            self.gameids_list = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        self.gameids_list = [x.strip() for x in self.gameids_list]
        for entry in self.gameids_list:
            self.ui.name = QtWidgets.QCheckBox(entry)
            self.ui.scrolllayout.addWidget(self.ui.name)
    
    def closeEvent(self, event):
        self.accept()