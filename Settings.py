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
from setup_ui import Ui_settings


class SettingsWindow(QDialog):
    def __init__(self, scoreboard, main_window):
        super().__init__()
        self.ui = Ui_settings()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.color_options = ["Red", "Blue", "Green", "Yellow", "Lightgreen", "Pink", "Choose Color"]
        self.list_of_teams = []
        self.path_main = ""
        # in case settings already are ok.
        # after shutdown or stuff
        self.refresh()
        self.set_from_scoreboard()
        self.main = main_window

    def set_from_scoreboard(self):
        self.ui.jerseyLeftOptions.setCurrentText("Red")
        self.ui.jerseyRightOptions.setCurrentText("Red")
        if self.scoreboard.teamleft.path != "":
            self.ui.teamLeftOptions.setCurrentText(self.scoreboard.teamleft.path)
        if self.scoreboard.teamright.path != "":
            self.ui.teamRightOptions.setCurrentText(self.scoreboard.teamright.path)

    def highlighted_right(self, string_q):
        if string_q == "Choose Color":
            color = QColorDialog.getColor()
            self.scoreboard.teamright.color = color.name()

    def highlighted_left(self, string_q):
        if string_q == "Choose Color":
            color = QColorDialog.getColor()
            self.scoreboard.teamleft.color = color.name()

    def save(self):
        self.scoreboard.teamleft.set_path(self.ui.teamLeftOptions.currentText(), "Output/left_path.txt")
        self.scoreboard.teamright.set_path(self.ui.teamRightOptions.currentText(), "Output/right_path.txt")
        color_right = self.ui.jerseyRightOptions.currentText()
        color_left = self.ui.jerseyLeftOptions.currentText()
        if not color_left == "Choose Color":
            self.scoreboard.teamleft.color = color_left
        if not color_right == "Choose Color":
            self.scoreboard.teamright.color = color_right
        self.scoreboard.write_all()
        #  palette_left = QtGui.QPalette()
        # print(1)
        # print(self.scoreboard.teamleft.color)
        # print(QtGui.QColor(self.scoreboard.teamleft.color))
        # color = QtGui.QColor("Red")
        # print(2)
        # self.main.ui.farbe.setStyleSheet("QLabel { background-color : %s"%color.name())
        # self.main.ui.left_color.setPalette(palette_left)
        self.accept()

    def refresh(self):
        # refresh teamlist from logo folder
        self.list_of_teams = []
        self.ui.teamRightOptions.clear()
        self.ui.teamLeftOptions.clear()
        try:
            for team in os.listdir(self.path_main + "Input/Teamlogos"):
                if team[-4:] == ".png":
                    self.list_of_teams.append(team[:-4])
        except FileNotFoundError:
            self.list_of_teams = []
        self.ui.teamLeftOptions.addItems(self.list_of_teams)
        self.ui.teamRightOptions.addItems(self.list_of_teams)

        # refresh Colors (just because)
        colors = self.color_options
        self.ui.jerseyRightOptions.clear()
        self.ui.jerseyLeftOptions.clear()
        self.ui.jerseyLeftOptions.addItems(colors)
        self.ui.jerseyRightOptions.addItems(colors)

    def swap(self):
        r = self.ui.jerseyRightOptions.currentIndex()
        l = self.ui.jerseyLeftOptions.currentIndex()
        self.ui.jerseyRightOptions.setCurrentIndex(l)
        self.ui.jerseyLeftOptions.setCurrentIndex(r)
        r = self.ui.teamRightOptions.currentIndex()
        l = self.ui.teamLeftOptions.currentIndex()
        self.ui.teamRightOptions.setCurrentIndex(l)
        self.ui.teamLeftOptions.setCurrentIndex(r)
        self.scoreboard.swap()

