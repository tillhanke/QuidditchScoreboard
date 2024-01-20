import os
import io
from PIL import Image, ImageDraw
import shutil
import csv
from Team import *
from Timer import *


class ScoreBoard:
    def __init__(self, window):
        self.teamleft = Team()
        self.teamright = Team()
        self.time = Timer(path="Output/Gametime", upCounting=True)
        self.oss = "-"
        self.window = window
        self.penalty = {}  # all information about a specific penalty will be saved in this dict

    def read_all(self):
        if os.path.isdir("Output"):
            try:
                with io.open("Output/ScoreLeft.txt", "r", encoding="utf-8-sig") as dat:
                    line = dat.read()
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
                with io.open("Output/ScoreRight.txt", "r", encoding="utf-8-sig") as dat:
                    line = dat.read()
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
                with io.open("Output/Gametime.txt", "r", encoding="utf-8-sig") as dat:
                    self.time.time_str = dat.read()
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
        self.write_gameinfo(False, False)
        self.write_penalty()
        self.write_jersey()
        self.write_logo()
        self.window.update_team_ui()

    def write_gameinfo(self, timekeeper_connected, swapped):
        
        try:
            if (timekeeper_connected):
                if(swapped):
                    self.teamleft.score = open("Output/ScoreRight.txt", "r").read()
                    self.teamright.score = open("Output/ScoreLeft.txt", "r").read()
                else:
                    self.teamleft.score = open("Output/ScoreLeft.txt", "r").read()
                    self.teamright.score = open("Output/ScoreRight.txt", "r").read()
            score_left = self.teamleft.score
            score_right = self.teamright.score
            team_left = self.teamleft.name
            team_right = self.teamright.name

            overtime_setscore_tk = open("Output/OvertimeSetscore.txt", "r").read()
            if(overtime_setscore_tk != "-" and timekeeper_connected):
                self.window.ui.oss_label.setText("Overtime setscore: " + overtime_setscore_tk)
                self.oss = overtime_setscore_tk
            
            with open('Output/Gameinfo.csv','w') as file:
                fieldnames = ["Team Left", "Score Left", "Team Right", "Score Right", "Overtime Setscore"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n", delimiter=",")
                writer.writeheader()
                writer.writerow({"Team Left": team_left, "Score Left": score_left, "Team Right": team_right, "Score Right": score_right, "Overtime Setscore": self.oss})
            
        except Exception as e:
            print(e)

    def write_penalty(self):
        if len(self.penalty) == 0:
            return
        else:
            with open("Output/Penalty.csv","w", encoding="utf-8-sig") as file:
                fieldnames = ["Name", "Team", "Reason"]
                writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n", delimiter=",")
                writer.writeheader()
                writer.writerow({"Name": str(self.penalty["player"]), "Team": str(self.penalty["team"].name), "Reason": str(self.penalty["reason"])})
            try:
                shutil.copyfile("Input/Cards/" + self.penalty["card"], "Output/Card.png")
            except FileExistsError:
                os.remove("Output/Card.png")
                shutil.copyfile("Input/Cards/" + self.penalty["card"], "Output/Card.png")

            # TODO: figure out new penalty behavior
            open("quadballlive_api/new_penalty.txt", "w").write("0")
            self.window.ui.new_penalty_label.setText("")

    def write_jersey(self):
        x, y = 130, 2  # size of output Image

        if self.teamright.color == "" or self.teamleft.color == "":
            print("Please choose colors for the jerseys!")
            return

        # write for team right
        im = Image.new("RGBA", (x, y))
        dr = ImageDraw.Draw(im)
        dr.rectangle([(0, 0), (x, y)], fill=self.teamright.color, outline=None)
        im.save("Output/TeamRightJersey.png")
        # write for team left
        im = Image.new("RGBA", (x, y))
        dr = ImageDraw.Draw(im)
        dr.rectangle([(0, 0), (x, y)], fill=self.teamleft.color, outline=None)
        im.save("Output/TeamLeftJersey.png")

    def write_timer(self):
        self.time.write()

    def write_logo(self):
        try:
            shutil.copyfile(self.teamleft.logo, "Output/TeamLeftLogo.png")
            self.teamleft.rosterpic = "Input/TeamrosterPNGs/" + self.teamleft.path + "Left.png"
            shutil.copyfile(self.teamleft.rosterpic, "Output/TeamLeftRoster.png")
        except FileExistsError:
            os.remove("Output/TeamLeftLogo.png")
            shutil.copyfile(self.teamleft.logo, "Output/TeamLeftLogo.png")
            self.teamleft.rosterpic = "Input/TeamrosterPNGs/" + self.teamleft.path + "Left.png"
            shutil.copyfile(self.teamleft.rosterpic, "Output/TeamLeftRoster.png")
        except FileNotFoundError as e:
            print(e)

        try:
            shutil.copyfile(self.teamright.logo, "Output/TeamRightLogo.png")
            self.teamright.rosterpic = "Input/TeamrosterPNGs/" + self.teamright.path + "Right.png"
            shutil.copyfile(self.teamright.rosterpic, "Output/TeamRightRoster.png")
        except FileExistsError:
            os.remove("Output/TeamRightLogo.png")
            shutil.copyfile(self.teamright.logo, "Output/TeamRightLogo.png")
            self.teamright.rosterpic = "Input/TeamrosterPNGs/" + self.teamright.path + "Right.png"
            shutil.copyfile(self.teamright.rosterpic, "Output/TeamRightRoster.png")
        except FileNotFoundError as e:
            print(e)
