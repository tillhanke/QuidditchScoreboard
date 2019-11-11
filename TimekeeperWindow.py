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
from timekeeper_ui import Ui_Timekeeper
from timekeeper import Timekeeper


class TimekeeperWindow(QDialog):
    def __init__(self, scoreboard, main_ui):
        super().__init__()
        self.ui = Ui_Timekeeper()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.main = main_ui
        self.timekeeper = Timekeeper(self.scoreboard, self.main)

    def connect(self):
        self.scoreboard.time.stop()
        self.timekeeper.auth, self.timekeeper.gameid = self.ui.auth.displayText(), self.ui.gameID.displayText(),
        #self.timekeeper.gameid, self.timekeeper.auth = "A-403-559-343", "83d4b05926f1b081e2f6da408bf5b1e5"  # for debugging insert info
        #self.timekeeper.connect()
        self.timekeeper.connect_js(self.timekeeper.auth, self.timekeeper.gameid)
        self.scoreboard.timekeeper = self.timekeeper
        if self.timekeeper.connected:
            self.main.ui.timekeeperButton.setText("Stop Timekeeper")
        self.accept()

    def disconnect(self):
        self.timekeeper.disconnect_js()