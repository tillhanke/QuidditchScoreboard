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
from snitch_catch_ui import Ui_SnitchCatch


class SnitchCatchWindow(QDialog):
    def __init__(self, scoreboard, main_window):
        super().__init__()
        self.ui = Ui_SnitchCatch()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.main_window = main_window

    def save(self):
        if self.ui.teamLeftButton.isChecked():
            self.scoreboard.teamleft.snitch_catch.append(True)
            self.scoreboard.teamright.snitch_catch.append(False)
            self.main_window.add_left(30)
        if self.ui.teamRightButton.isChecked():
            self.scoreboard.teamleft.snitch_catch.append(False)
            self.scoreboard.teamright.snitch_catch.append(True)
            self.main_window.add_right(30)
        self.scoreboard.write_score()
        self.accept()
