from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWidgets
import os
import io
import time
import threading
import csv
import subprocess
from Scoreboard import ScoreBoard
from main_ui import Ui_MainWindow
from SureBro import SureBro
from TimekeeperWindow import TimekeeperWindow
from Penalty import PenaltyWindow
from Settings import SettingsWindow
from Extra_Timer import ExtraTimerWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setCentralWidget(self.ui.centralwidget)
        self.scoreboard = ScoreBoard(self)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle("Quadball Scoreboard")
        self.really_ui = SureBro(self)
        self.swapped = False

        self.timekeeper_w = TimekeeperWindow(self.scoreboard, self)
        self.penalty_w = PenaltyWindow(self.scoreboard)
        self.settings_w = SettingsWindow(self.scoreboard, self)
        self.extra_timers = []

        # in case of restart
        self.scoreboard.read_all()
        self.set_from_scoreboard()

        self.time_thread = threading.Thread(target=self.update_timer_ui)
        self.time_thread.start()
        self.time_thread.run = True
        
        self.new_penalty_thread = threading.Thread(target=self.new_penalty)
        self.new_penalty_thread.start()
        self.new_penalty_thread.run = True
        
        self.scorecrawl_connected = 0
        self.gameids_list = []

    def set_from_scoreboard(self):
        self.ui.time_label.setText(self.scoreboard.time.time_str)
        self.update_score_ui()
        self.update_team_ui()

    def add_timer(self):
        self.extra_timers.append(ExtraTimerWindow())
        self.extra_timers[-1].show()

    def start_timer(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.time.start()
        self.ui.stopTimer.setEnabled(True)
        self.ui.startTimer.setEnabled(False)
        self.ui.snitchcatch_right.setEnabled(False)
        self.ui.snitchcatch_left.setEnabled(False)

    def stop_timer(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.time.stop()
        self.ui.stopTimer.setEnabled(False)
        self.ui.startTimer.setEnabled(True)
        self.ui.snitchcatch_right.setEnabled(True)
        self.ui.snitchcatch_left.setEnabled(True)

    def set_timer(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        time = self.ui.timeEdit.time()
        self.scoreboard.time.set(ui_label=self.ui.time_label, minutes=time.minute(), seconds=time.second())

    def add_left(self, amount):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamleft.score += amount
        self.update_score_ui()

    def reset_left(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamleft.score = 0
        self.scoreboard.teamleft.snitch_catch = []
        self.scoreboard.swapped = 0
        self.update_score_ui()

    def reset_right(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamright.score = 0
        self.scoreboard.teamright.snitch_catch = []
        self.scoreboard.swapped = 0
        self.update_score_ui()

    def add_right(self, amount):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamright.score += amount
        self.update_score_ui()

    def timekeeper_start(self):
        if self.timekeeper_w.timekeeper.connected:
            self.timekeeper_w.timekeeper.break_connection = True
            #self.timekeeper_w.timekeeper.ws.keep_running = False
            self.timekeeper_w.timekeeper.connected = False
            self.scoreboard.read_all()
            self.timekeeper_w.disconnect()
            print("Disconnected Timekeeper")
            self.ui.timekeeperButton.setText("Start Timekeeper")
            self.scoreboard.swapped = 0
            return
        else:
            self.scoreboard.read_all()
            self.timekeeper_w.show()

    def settings_start(self):
        self.settings_w.show()

    def snitch_catch_left(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamleft.snitch_catch.append(True)
        self.scoreboard.teamright.snitch_catch.append(False)
        self.add_left(30)
        self.scoreboard.write_gameinfo(self.timekeeper_w.timekeeper.connected, self.swapped)

    def snitch_catch_right(self):
        if self.timekeeper_w.timekeeper.connected:
            return
        self.scoreboard.teamleft.snitch_catch.append(False)
        self.scoreboard.teamright.snitch_catch.append(True)
        self.add_right(30)
        self.scoreboard.write_gameinfo(self.timekeeper_w.timekeeper.connected, self.swapped)

    def open_penalty(self):
        self.penalty_w = PenaltyWindow(self.scoreboard)
        self.penalty_w.show()
        self.penalty_w.on_open()

    def update_team_ui(self):
        self.ui.teamname_left.setText(self.scoreboard.teamleft.name)
        self.ui.teamname_right.setText(self.scoreboard.teamright.name)

    def update_timer_ui(self):
        t = threading.currentThread()
        while getattr(t, "run", True):
            if self.timekeeper_w.timekeeper.connected:
                self.scoreboard.time.time_str = open("Output/Gametime.txt", "r", encoding="utf-8").read()
                self.update_score_ui_tk()
            self.ui.time_label.setText(self.scoreboard.time.time_str)
            time.sleep(0.5)

    def update_score_ui(self):
        self.ui.score_left.setText(str(self.scoreboard.teamleft.get_score_str()))
        self.ui.score_right.setText(str(self.scoreboard.teamright.get_score_str()))
        self.scoreboard.write_gameinfo(self.timekeeper_w.timekeeper.connected, self.swapped)

    def new_penalty(self):
        t = threading.currentThread()
        while getattr(t, "run", True):
            if self.timekeeper_w.timekeeper.connected:
                new_penalty = open("quadballlive_api/new_penalty.txt", "r").read()
                if(new_penalty == "1"):
                    penalty_team = open("quadballlive_api/penalty_team.txt", "r").read()
                    if(penalty_team == "a" or (penalty_team == "b" and self.swapped)):
                        team = self.scoreboard.teamleft
                    elif(penalty_team == "b" or (penalty_team == "a" and self.swapped)):
                        team = self.scoreboard.teamright

                    if(os.path.isfile("quadballlive_api/penalty_card.txt")):
                        penalty_card = open("quadballlive_api/penalty_card.txt", "r").read()
                        if(penalty_card == "blue"):
                            card = "Blue.png"
                        elif(penalty_card == "yellow"):
                            card = "Yellow.png"
                        elif(penalty_card == "yellowejection"):
                            card = "YellowEjection.png"
                        elif(penalty_card == "red"):
                            card = "Red.png"
                        elif(penalty_card == "ejection"):
                            card = "Ejection.png"

                    if(os.path.isfile("quadballlive_api/penalty_playernumber.txt")):
                        number = open("quadballlive_api/penalty_playernumber.txt", "r").read()

                    if(os.path.isfile("quadballlive_api/penalty_reason.txt")):
                        reason = open("quadballlive_api/penalty_reason.txt", "r").read()

                    if number != "":
                        if number in team.roster:
                            player = "{0} - {1}".format(number, team.roster[number])
                        else:
                            player = "{0}".format(number)
                    else:
                        player = ""

                    self.scoreboard.penalty = {"player": player,
                                            "reason": reason,
                                            "team": team,
                                            "card": card
                                            }
                    #self.scoreboard.write_penalty()
                    
                    # TODO: SHOW NEW PENALTY ON MAIN UI
                    self.ui.new_penalty_label.setText("New penalty available!")
            time.sleep(3)
        
    def closeQSB(self):
        self.scoreboard.time.stop()
        self.really_ui.show()

    def update_score_ui_tk(self):
        if(self.swapped == 0):
            score_left = open("Output/ScoreLeft.txt", "r").read()
            score_right = open("Output/ScoreRight.txt", "r").read()
        else:
            score_left = open("Output/ScoreRight.txt", "r").read()
            score_right = open("Output/ScoreLeft.txt", "r").read()
        self.scoreboard.write_gameinfo(self.timekeeper_w.timekeeper.connected, self.swapped)
        self.ui.score_left.setText(score_left)
        self.ui.score_right.setText(score_right)

    def scorecrawl_start(self):
        if self.ui.verticalLayout_10.count() == 0:
            return
        if(self.scorecrawl_connected == False):
            ans = self.connect_sc()
            if(ans != -1):
                self.ui.scorecrawlButton.setText("Stop score crawl")
        else:
            self.disconnect_sc()
            self.ui.scorecrawlButton.setText("Start score crawl")
    
    def connect_sc(self):
        sc_file = open("quadballlive_api/gameids_scorecrawl.txt", "w")
        sc_file.write("")
        sc_file.close()
        sc_file = open("quadballlive_api/gameids_scorecrawl.txt", "a")
        first = 1
        for i in range(self.ui.verticalLayout_10.count()):
            if(self.ui.verticalLayout_10.itemAt(i).widget().isChecked()):
                if(first == 0):
                    sc_file.write("\n")
                sc_file.write(self.ui.verticalLayout_10.itemAt(i).widget().text()[:13])
                first = 0
        sc_file.close()
        if(first == 1):
            return -1
        self.scorecrawl_proc = subprocess.Popen('node .\quadballlive_api\quadballlive_scorecrawl.js')
        self.scorecrawl_connected = True
        return 1

    def disconnect_sc(self):
        self.scorecrawl_proc.kill()
        print("Quadball Score Crawl disconnected.")
        with open('Output/ScoreCrawl.csv','w') as file:
            fieldnames = ["Scorecrawl"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n", delimiter=",")
            writer.writeheader()
            writer.writerow({"Scorecrawl": ""})
        self.scorecrawl_connected = False

    def read_gameids_sc(self):
        open("quadballlive_api/gameidstonames.txt", "w").write("")
        self.gameidstonames_proc = subprocess.Popen('node .\quadballlive_api\quadballlive_gameidtonames.js')
        time.sleep(3)
        self.gameidstonames_proc.kill()
        for i in reversed(range(self.ui.verticalLayout_10.count())): 
            self.ui.verticalLayout_10.itemAt(i).widget().setParent(None)
        with open("quadballlive_api/gameidstonames.txt", encoding="utf-8-sig") as f:
            self.gameids_list = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        self.gameids_list = [x.strip() for x in self.gameids_list]
        for entry in self.gameids_list:
            self.ui.name = QtWidgets.QCheckBox(entry)
            self.ui.name.setObjectName("scrollcontent")
            self.ui.verticalLayout_10.addWidget(self.ui.name)

    def swap_scores(self):
        self.swapped = (self.swapped + 1) % 2
        self.scoreboard.teamleft.score, self.scoreboard.teamright.score = self.scoreboard.teamright.score, self.scoreboard.teamleft.score
        if(self.timekeeper_w.timekeeper.connected):
            self.update_score_ui_tk()
        else:
            self.update_score_ui()

    def delete_oss(self):
        self.ui.oss_label.setText("")
        self.scoreboard.oss = "-"
        self.scoreboard.write_gameinfo(False, self.swapped)
    
    def closeEvent(self, event):
        self.time_thread.run = False
        self.new_penalty_thread.run = False
        self.close()