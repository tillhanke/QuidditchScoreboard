from sureBro_ui import Ui_sureBro
from PyQt5.QtWidgets import QDialog


class SureBro(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_sureBro()
        self.ui.setupUi(self)
        self.main = main_window

    def yes(self):
        if self.main.timekeeper_w.timekeeper.connected:
            self.main.timekeeper_w.timekeeper.break_connection = True
            self.main.timekeeper_w.timekeeper.ws.keep_running = False
            self.main.timekeeper_w.timekeeper.connected = False
            self.main.ui.timekeeperButton.setText("Start Timekeeper")
        self.main.accept()
        self.accept()

    def no(self):
        self.accept()
