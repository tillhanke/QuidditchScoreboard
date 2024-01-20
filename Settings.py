from PyQt5.QtWidgets import QDialog, QColorDialog
import os
from setup_ui import Ui_settings


class SettingsWindow(QDialog):
    def __init__(self, scoreboard, main_window):
        super().__init__()
        self.ui = Ui_settings()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.color_options = ["Choose Color", "Red", "Blue", "Green", "Yellow", "Lightgreen", "Pink"]
        self.list_of_teams = []
        self.path_main = ""
        # in case settings already are ok.
        # after shutdown or stuff
        self.refresh()
        self.set_from_scoreboard()
        self.main = main_window

    def set_from_scoreboard(self):
        self.ui.jerseyLeftOptions.setCurrentText("Choose Color")
        self.ui.jerseyRightOptions.setCurrentText("Choose Color")
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
        self.scoreboard.teamleft.set_path(self.ui.teamLeftOptions.currentText(), "Output/LeftPath.txt")
        self.scoreboard.teamright.set_path(self.ui.teamRightOptions.currentText(), "Output/RightPath.txt")
        color_right = self.ui.jerseyRightOptions.currentText()
        color_left = self.ui.jerseyLeftOptions.currentText()
        if not color_left == "Choose Color":
            self.scoreboard.teamleft.color = color_left
        if not color_right == "Choose Color":
            self.scoreboard.teamright.color = color_right
        self.scoreboard.write_all()
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
        if (len(self.list_of_teams) > 1):
            self.ui.teamLeftOptions.setCurrentIndex(0)
            self.ui.teamRightOptions.setCurrentIndex(1)

        # refresh Colors (just because)
        colors = self.color_options
        self.ui.jerseyRightOptions.clear()
        self.ui.jerseyLeftOptions.clear()
        self.ui.jerseyLeftOptions.addItems(colors)
        self.ui.jerseyRightOptions.addItems(colors)

    def swap(self):
        self.scoreboard.swap()

