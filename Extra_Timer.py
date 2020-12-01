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
from extra_timer_ui import Ui_extra_timer
from Timer import Timer


class ExtraTimerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_extra_timer()
        self.ui.setupUi(self)
        self.label = ""
        self.timer = Timer(path="", upCounting=True)
        self.t = threading.Thread(target=self.update_timer_ui)
        self.t.start()

    def update_timer_ui(self):

        while self.result() == 0:
            self.ui.current_time.setText(self.timer.time_str)
            time.sleep(0.5)

    def start_timer(self):
        if self.timer.running:
            self.timer.stop()
        self.label = self.ui.timer_label.text()
        if self.label == "":
            print("Please give label!")
            return None
        else:
            self.timer.path = "Output/{}.txt".format(self.label)
            print("Output/{}.txt".format(self.label))
            self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def set_timer(self):
        set_time = self.ui.timeEdit.time()
        self.timer.set(ui_label=self.ui.current_time, minutes=set_time.minute(), seconds=set_time.second())

    def set_backward(self):
        self.timer.up = False

    def set_forward(self):
        self.timer.up = True

    def close_button(self):
        self.timer.stop()
        try:
            os.remove("Output/{}.txt".format(self.label))
        except FileNotFoundError:
            None
        self.accept()
