from PyQt5.QtWidgets import QDialog
import os
from sureBro_ui import Ui_sureBro


class SureBro(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_sureBro()
        self.ui.setupUi(self)
        self.main = main_window

    def yes(self):
        if self.main.timekeeper_w.timekeeper.connected:
            self.main.timekeeper_w.timekeeper.break_connection = True
            self.main.timekeeper_w.timekeeper.connected = False
            self.main.ui.timekeeperButton.setText("Start Timekeeper")
            self.main.timekeeper_w.timekeeper.disconnect_js()
        for timer in self.main.extra_timers:
            timer.close()
        if self.main.scorecrawl_connected:
            self.main.disconnect_sc
        filelist = [ f for f in os.listdir("Output")  ]
        for f in filelist:
            os.remove(os.path.join("Output/", f))
        self.accept()
        self.main.close()

    def no(self):
        self.accept()
