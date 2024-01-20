from PyQt5.QtWidgets import QDialog
from timekeeper_ui import Ui_Timekeeper
from Timekeeper import Timekeeper


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
        self.timekeeper.gameid = self.ui.gameID.displayText()
        if (self.timekeeper.gameid == ""):
            return
        self.timekeeper.connect_js(self.timekeeper.gameid)
        self.scoreboard.timekeeper = self.timekeeper
        if self.timekeeper.connected:
            self.main.ui.timekeeperButton.setText("Stop Timekeeper")
        self.accept()

    def disconnect(self):
        self.timekeeper.disconnect_js()