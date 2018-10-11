import codecs
from tkinter import *
import os
import shutil


class Team:
    def __init__(self, team_type, path):
        self.path_main = path
        self.logo = None
        self.name = StringVar()
        self.roster = {}   # Roster will be setup as a Dict with Number as key and name as element
        self.is_set = False
        self.team_type = team_type

    def set(self, team_name, destfile):
        self.logo = team_name+".png"
        self.logo = self.path_main.get() + "Input/Teamlogos/{}.png".format(team_name)
        try:
            shutil.copyfile(self.logo, self.path_main.get() + "Output/"+destfile)
        except FileExistsError:
            os.remove(self.path_main.get() + "Output/"+destfile)
            shutil.copyfile(self.logo, self.path_main.get() + "Output/"+destfile)
        # ---- set National Flag ----
        try:
            shutil.copyfile(self.path_main.get() + "Input/TeamFlagsUpright/"+team_name+".png", self.path_main.get() + "Output/"+self.team_type+"FlagUpright.png")
        except FileExistsError:
            os.remove(self.path_main.get() + "Output/"+self.team_type+"FlagUpright.png")
            shutil.copyfile(self.path_main.get() + "Input/TeamFlagsUpright/"+team_name+".png", self.path_main.get() + "Output/"+self.team_type+"FlagUpright.png")
        try:
            shutil.copyfile(self.path_main.get() + "Input/TeamFlags/"+team_name+".png", self.path_main.get() + "Output/"+self.team_type+"Flag.png")
        except FileExistsError:
            os.remove(self.path_main.get() + "Output/"+self.team_type+"Flag.png")
            shutil.copyfile(self.path_main.get() + "Input/TeamFlags/"+team_name+".png", self.path_main.get() + "Output/"+self.team_type+"Flag.png")
        # ---- Set roster ----
        # with open(self.path_main.get() + "Input/Teamrosters/"+team_name+".txt", "r", encoding="utf8") as roster_file:
        #
        # use 'iso-8859-1' to make german umlaute available to the rosters
        #
        with codecs.open(self.path_main.get() + "Input/Teamrosters/"+team_name+".txt", "r", 'utf-8') as roster_file:
            content = roster_file.readlines()
            self.name.set(content[0][0:-1])
        for line in content[1:]:
            if ":" not in line:
                continue
            number, name = line.split(":")
            self.roster[number] = name
        with open(self.path_main.get() + "Output/{}.txt".format(self.team_type), "w") as file:
            file.write(self.name.get())
        self.is_set = True
        print("Team:" + self.name.get() + " successfully set.")

    def set_color(self, colorfile):
        #
        # Setting jersey color for team from colors in Input/Jerseycolors
        # to Output/Team(A/B)jersey.png
        #
        try:
            shutil.copyfile(self.path_main.get() + "Input/Jerseycolors/"+colorfile, self.path_main.get() + "Output/"+self.team_type+"jersey.png")
        except FileExistsError:
            os.remove(self.path_main.get() + "Output/"+self.team_type+"jersey.png")
            shutil.copyfile(self.path_main.get() + "Input/Jerseycolors/"+colorfile, self.path_main.get() + "Output/"+self.team_type+"jersey.png")

