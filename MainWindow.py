from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from PyQt5 import QtGui
import os
import io
from PIL import Image, ImageDraw
import shutil
import websocket
import time
import urllib.request
import json
import math
import threading
import sys
import codecs
from Scoreboard import ScoreBoard
from main_ui import Ui_main
from SureBro import SureBro
from TimekeeperWindow import TimekeeperWindow
from Penalty import PenaltyWindow
from Settings import SettingsWindow
from SnitchCatch import SnitchCatchWindow
from Extra_Timer import ExtraTimerWindow
from timekeeper import Timekeeper

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.scoreboard = ScoreBoard(self)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.show()
        self.really_ui = SureBro(self)
        # in case of restart
        self.scoreboard.read_all()
        self.set_from_scoreboard()

        self.timekeeper_w = TimekeeperWindow(self.scoreboard, self)
        self.penalty_w = PenaltyWindow(self.scoreboard)
        self.settings_w = SettingsWindow(self.scoreboard, self)
        self.settings_w.show()
        self.snitch_w = SnitchCatchWindow(self.scoreboard, self)
        self.extra_timers = []

        time_thread = threading.Thread(target=self.update_timer_ui)
        time_thread.start()
        # self.ui.timekeeperButton.deleteLater()

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
        self.ui.stopTimer.setEnabled(True);
        self.ui.startTimer.setEnabled(False);

    def stop_timer(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.time.stop()
        self.ui.stopTimer.setEnabled(False);
        self.ui.startTimer.setEnabled(True);

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

    def snitch_catch(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        if self.scoreboard.time.running:
            return
        self.snitch_w.ui.teamRightButton.setText(self.scoreboard.teamright.name)
        self.snitch_w.ui.teamLeftButton.setText(self.scoreboard.teamleft.name)
        self.scoreboard.time.stop()
        self.snitch_w.show()

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
                gametime = open("Output/timer.txt").read()
                if(str(self.scoreboard.teamleft.get_score_str()) != open("Output/score_left.txt", "r").read() or str(self.scoreboard.teamright.get_score_str()) != open("Output/score_right.txt", "r").read()):
                   self.update_score_ui_tk()
            else:
                gametime = self.scoreboard.time.time_str
            self.ui.time_label.setText(gametime)
            time.sleep(0.5)

    def update_score_ui(self):
        self.ui.score_left.setText(str(self.scoreboard.teamleft.get_score_str()))
        self.ui.score_right.setText(str(self.scoreboard.teamright.get_score_str()))
        self.scoreboard.write_score()

    def close(self):
        self.scoreboard.time.stop()
        self.really_ui.show()

    def update_score_ui_tk(self):
        score_left = open("Output/score_left.txt", "r").read()
        score_right = open("Output/score_right.txt", "r").read()
        self.ui.score_left.setText(score_left)
        self.ui.score_right.setText(score_right)