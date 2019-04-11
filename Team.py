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


class Team:
    def __init__(self):
        self.color = ""
        self.score = 0
        self.score_str = ""
        self.name = ""
        self.snitch_catch = []
        self.path = ""
        self.logo = ""
        self.roster = {}

    def get_score_str(self):
        if self.score_str != "":
            return self.score_str
        else:
            out = str(self.score)
            if len(self.snitch_catch) == 0:
                return out
            else:
                for i in self.snitch_catch:
                    if i:
                        out += "*"
                    else:
                        out += "°"
                return out

    def set_path(self, path, datafile=""):
        self.path = path
        if not datafile == "":
            with open(datafile, "w") as dat:
                dat.write(self.path)
        # set logo path
        self.logo = "Input/Teamlogos/" + self.path + ".png"
        # set name and roster
        try:
            with codecs.open("Input/Teamrosters/"+self.path+".txt", "r", 'utf-8') as roster_file:
                content = roster_file.readlines()
                self.name = content[0][0:-1]
            for line in content[1:]:
                if ":" not in line:
                    continue
                number, name = line.split(":")
                self.roster[number] = name
        except FileNotFoundError as e:
            print(e)
