from timekeeper_ui import *
from PyQt5.QtWidgets import QDialog
from Timekeeper import *


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
        self.timekeeper.gameid, self.timekeeper.auth = self.ui.gameID.displayText(), self.ui.auth.displayText(),
        # self.timekeeper.gameid, self.timekeeper.auth = "", ""  # for debugging insert info
        self.timekeeper.connect()
        self.scoreboard.timekeeper = self.timekeeper
        if self.timekeeper.connected:
            self.main.ui.timekeeperButton.setText("Stop Timekeeper")
        self.accept()

