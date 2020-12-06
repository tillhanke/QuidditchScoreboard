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


class Timer:
    def __init__(self, path="", upCounting=True):
        self.up = upCounting
        self.time_str = "00:00"
        self.sec = 0
        self.min = 0
        self.running = False
        self.label = None
        self.path = path

    def start(self):
        self.running = True
        timer_thread = threading.Thread(target=self.run)
        timer_thread.start()

    def write(self):
        with open(self.path, "w") as dat:
            dat.write(self.time_str)

    def run(self):
        while self.running:
            # down counting:
            if not self.up:
                if self.sec == self.min == 0:
                    self.running = False
                elif self.sec > 0:
                    self.sec = self.sec-1
                else:
                    self.sec = 59
                    self.min = self.min-1
            # up counting:
            else:
                if self.sec < 59:
                    self.sec = 1+self.sec
                else:
                    self.sec = 0
                    self.min = 1+self.min
            self.time_str = "%02d" % self.min + ":" + "%02d" % self.sec
            time.sleep(1)
            self.write()

    def stop(self):
        self.running = False

    def set(self, ui_label, minutes, seconds):
        self.stop()
        time.sleep(1.01)
        self.min = minutes
        self.sec = seconds
        self.time_str = "%02d" % self.min + ":" + "%02d" % self.sec
        ui_label.setText(self.time_str)