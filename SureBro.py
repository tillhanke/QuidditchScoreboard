from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
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
from sureBro_ui import Ui_sureBro


class SureBro(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_sureBro()
        self.ui.setupUi(self)
        self.main = main_window

    def yes(self):
        if self.main.timekeeper_w.timekeeper.connected:
            self.main.timekeeper_w.timekeeper.break_connection = True
            #self.main.timekeeper_w.timekeeper.ws.keep_running = False
            self.main.timekeeper_w.timekeeper.connected = False
            self.main.ui.timekeeperButton.setText("Start Timekeeper")
            self.main.timekeeper_w.timekeeper.disconnect_js()
        for timer in self.main.extra_timers:
            timer.close()
        open("Output/score_left.csv", "w").write("Score Left\n0")
        open("Output/score_right.csv", "w").write("Score Right\n0")
        open("Output/TeamLeft.csv", "w").write("Team Left\n")
        open("Output/TeamLeft.csv", "w").write("Team Right\n")
        open("Output/timer.csv", "w").write("Gametime\n00:00")
        open("Output/Gameinfo.csv", "w").write("Gametime,Team Left,Score Left,Team Right,Score Right\n")
        open("quidditchlive_api/new_penalty.txt", "w").write("0")
        open("Output/overtime_setscore.csv", "w").write("Overtime setscore\n")
        self.main.accept()
        self.accept()

    def no(self):
        self.accept()
