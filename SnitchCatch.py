from snitch_catch_ui import Ui_SnitchCatch
from PyQt5.QtWidgets import QDialog


class SnitchCatchWindow(QDialog):
    def __init__(self, scoreboard, main_window):
        super().__init__()
        self.ui = Ui_SnitchCatch()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.main_window = main_window

    def save(self):
        if self.ui.teamLeftButton.isChecked():
            self.scoreboard.teamleft.snitch_catch.append(True)
            self.scoreboard.teamright.snitch_catch.append(False)
            self.main_window.add_left(30)
        if self.ui.teamRightButton.isChecked():
            self.scoreboard.teamleft.snitch_catch.append(False)
            self.scoreboard.teamright.snitch_catch.append(True)
            self.main_window.add_right(30)
        self.scoreboard.write_score()
        self.accept()
