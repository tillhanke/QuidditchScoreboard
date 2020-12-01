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
import csv
import codecs
from Team import *
from Timer import *


class ScoreBoard:
    def __init__(self, window):
        self.teamleft = Team()
        self.teamright = Team()
        self.time = Timer(path="Output/timer.txt", upCounting=True)
        self.window = window
        self.penalty = {}  # all information about a specific penalty will be saved in this dict

    def read_all(self):
        if os.path.isdir("Output"):
            try:
                with io.open("Output/score_left.txt", "r", encoding="utf-8") as dat:
                    line = dat.readline()
                    score = ""
                    for letter in line:
                        if letter == "*":
                            self.teamleft.snitch_catch.append(True)
                        elif letter == "°":
                            self.teamleft.snitch_catch.append(False)
                        else:
                            score += letter
                    self.teamleft.score = int(score)
            except FileNotFoundError:
                None

            try:
                with io.open("Output/score_right.txt", "r", encoding="utf-8") as dat:
                    line = dat.readline()
                    score = ""
                    for letter in line:
                        if letter == "*":
                            self.teamright.snitch_catch.append(True)
                        elif letter == "°":
                            self.teamright.snitch_catch.append(False)
                        else:
                            score += letter
                    self.teamright.score = int(score)
            except FileNotFoundError:
                None

            try:
                with io.open("Output/left_path.txt", "r", encoding="utf-8") as dat:
                    self.teamleft.set_path(dat.readline())
            except FileNotFoundError:
                None

            try:
                with io.open("Output/right_path.txt", "r", encoding="utf-8") as dat:
                    self.teamright.set_path(dat.readline())
            except FileNotFoundError:
                None

            try:
                with io.open("Output/timer.txt", "r", encoding="utf-8") as dat:
                    self.time.time_str = dat.readline()
                    self.time.min = int(self.time.time_str.split(":")[0])
                    self.time.sec = int(self.time.time_str.split(":")[1])
            except FileNotFoundError:
                None
        else:
            os.mkdir("Output")

    def write_all(self):
        '''
        writes everything to the designated files
        :return:
        '''
        self.write_penalty()
        self.write_score()
        self.write_jersey()
        self.write_teams()
        self.write_logo()

    def write_teams(self):
        self.window.update_team_ui()
        with io.open("Output/TeamLeft.txt", "w", encoding="utf-8") as dat:
            dat.write(self.teamleft.name)
        with io.open("Output/TeamRight.txt", "w", encoding="utf-8") as dat:
            dat.write(self.teamright.name)

    def write_score(self):
        '''
        writes the scores to the files "Output/score*"
        :return:
        '''
        with io.open("Output/score_left.txt", "w", encoding="utf-8") as dat:
            dat.write(self.teamleft.get_score_str())
        with io.open("Output/score_right.txt", "w", encoding="utf-8") as dat:
            dat.write(self.teamright.get_score_str())

    def write_penalty(self):
        if len(self.penalty) == 0:
            return
        else:
            if os.path.isfile('Output/penalty.csv'):
                os.remove('Output/penalty.csv')
            with open('Output/penalty.csv','w') as file:
                fieldnames = ["Name", 'Team', 'Reason']
                writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n", delimiter=",")
                writer.writeheader()
                writer.writerow({"Name": str(self.penalty["player"]), "Team": str(self.penalty["team"].name), "Reason": str(self.penalty["reason"])})
            with io.open("Output/PenaltyTeam.txt", "w", encoding="utf-8") as dat:
                dat.write(self.penalty["team"].name)
            with io.open("Output/PenaltyPlayer.txt", "w", encoding="utf-8") as dat:
                dat.write(self.penalty["player"])
            with io.open("Output/PenaltyReason.txt", "w", encoding="utf-8") as dat:
                dat.write(self.penalty["reason"])
            try:
                shutil.copyfile("Input/Cards/" + self.penalty["card"], "Output/card.png")
            except FileExistsError:
                os.remove("Output/card.png")
                shutil.copyfile("Input/Cards/" + self.penalty["card"], "Output/card.png")
        penalty_thread = threading.Thread(target=self.reset_penalty)
        penalty_thread.start()

    def write_jersey(self):
        x, y = 47, 60  # size of output Image

        if self.teamright.color == "" or self.teamleft.color == "":
            print("Please choose colors for the jerseys!")
            return

        # write for team right
        im = Image.new("RGBA", (x, y))
        dr = ImageDraw.Draw(im)
        dr.polygon([(0, 0), (x / 2, y), (x, y), (x / 2, 0)], fill=self.teamright.color, outline=None)
        im.save("Output/TeamRightJersey.png")
        # write for team left
        im = Image.new("RGBA", (x, y))
        dr = ImageDraw.Draw(im)
        dr.polygon([(0, 0), (x / 2, y), (x, y), (x / 2, 0)], fill=self.teamleft.color, outline=None)
        im.save("Output/TeamLeftJersey.png")

    def write_timer(self):
        self.time.write()

    def write_logo(self):
        try:
            shutil.copyfile(self.teamleft.logo, "Output/TeamLeftLogo.png")
        except FileExistsError:
            os.remove("Output/TeamLeftLogo.png")
            shutil.copyfile(self.teamleft.logo, "Output/TeamLeftLogo.png")
        except FileNotFoundError as e:
            print(e)

        try:
            shutil.copyfile(self.teamright.logo, "Output/TeamRightLogo.png")
        except FileExistsError:
            os.remove("Output/TeamRightLogo.png")
            shutil.copyfile(self.teamright.logo, "Output/TeamRightLogo.png")
        except FileNotFoundError as e:
            print(e)

    def reset_penalty(self):
        time.sleep(15)
        with open("Output/PenaltyTeam.txt", "w") as dat:
            dat.write("")
        with open("Output/PenaltyPlayer.txt", "w") as dat:
            dat.write("")
        with open("Output/PenaltyReason.txt", "w") as dat:
            dat.write("")
        im = Image.new("RGBA", (100, 100))
        im.save("Output/card.png")

    def swap(self):
        inter = self.teamright
        self.teamright = self.teamleft
        self.teamleft = inter
        self.write_all()
