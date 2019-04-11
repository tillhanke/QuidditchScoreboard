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
from penalty_ui import Ui_Penalty


class PenaltyWindow(QDialog):
    def __init__(self, scoreboard):
        super().__init__()
        self.ui = Ui_Penalty()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.team = None
        try:
            with io.open("Input/penalty_reasons.txt", "r", encoding="utf-8") as dat:
                self.reasons = dat.readlines()
        except FileNotFoundError:
            self.reasons = []
        # ui setups

    def on_open(self):
        self.ui.teamLeftButton.setText(self.scoreboard.teamleft.name)
        self.ui.teamRightButton.setText(self.scoreboard.teamright.name)

    def team_chosen(self):
        players = []
        if self.ui.teamRightButton.isChecked():
            self.team = self.scoreboard.teamright
            for key, value in self.team.roster.items():
                players.append([str(key), str(value)])

        elif self.ui.teamLeftButton.isChecked():
            self.team = self.scoreboard.teamleft
            for key, value in self.team.roster.items():
                players.append([str(key), str(value)])

        players = sorted(players, key=lambda l: l[1], reverse=False)
        self.ui.list_players.addItems(["{0}: {1}".format(x, y) for x, y in players])
        self.ui.list_reasons.addItems(self.reasons)

    def ok(self):
        if self.ui.input_number.text() != "":
            player = "{0} {1}".format(self.ui.input_number.text(), self.team.roster[self.ui.input_number.text()])
        else:
            player = self.ui.list_players.currentText()
        if self.ui.input_reason.text() != "":
            reason = self.ui.input_reason.text()
            if reason not in self.reasons:
                self.reasons.append(reason)
            self.ui.list_reasons.clear()
            self.ui.list_reasons.addItems(self.reasons)
        else:
            reason = self.ui.list_reasons.currentText()
        if self.ui.redButton.isChecked():
            card = "Red.png"
        elif self.ui.yellowredButton.isChecked():
            card = "YellowRed.png"
        elif self.ui.yellowButton.isChecked():
            card = "Yellow.png"
        elif self.ui.blueButton.isChecked():
            card = "Blue.png"
        else:
            print("Please choose card")
            return None
        self.scoreboard.penalty = {"player": player,
                                   "reason": reason,
                                   "team": self.team,
                                   "card": card
                                   }
        self.scoreboard.write_penalty()
        self.accept()

