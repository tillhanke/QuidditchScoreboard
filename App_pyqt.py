from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from scores_ui import Ui_main
from timekeeper_ui import Ui_Timekeeper
from setup_ui import Ui_settings
from penalty_ui import Ui_Penalty
from snitch_catch_ui import Ui_SnitchCatch
import os
import io
from PIL import Image, ImageDraw
import codecs
import shutil
import websocket
import time
import urllib.request
import json
import math
import threading
import sys




'''
Check connections in scores_ui first!

self.add10_left.clicked.connect(lambda x: main.add_left(10))
self.sub10_left.clicked.connect(lambda x: main.add_left(-10))
self.add10_right.clicked.connect(lambda x: main.add_right(10))
self.sub10_right.clicked.connect(lambda x: main.add_right(-10))

'''


class Timekeeper:
    def __init__(self, game_id, auth, scoreboard):
        self.gametime = 0
        self.gameid = game_id
        self.data = 0
        self.json_game_data = {}
        self.diff = 0
        self.auth = auth  # authentication
        self.remote_server = 'timekeeper.lucas-scheuvens.de'
        self.ssl = True if self.remote_server == 'timekeeper.lucas-scheuvens.de' else False
        self.port = 443 if self.remote_server == 'timekeeper.lucas-scheuvens.de' else 8769
        self.team_left = None
        self.team_right = None
        self.score_left = 0
        self.score_right = 0
        self.jersey_left = '#FFFFFF'
        self.jersey_right = '#FFFFFF'
        self.connected = False
        self.scoreboard = scoreboard

    def connect(self):
        try:
            config = json.loads(
                urllib.request.urlopen("http://" + self.remote_server + "/getStreamingSettings.php").read().decode(
                    "utf-8"))
            print(config)
            ws = websocket.WebSocketApp(
                "ws" + ("s" if self.ssl else "") + "://" + config['server'] + ":" + str(self.port) + "/ws",
                on_open=lambda *x: Timekeeper.on_open(self, *x),
                on_message=lambda *x: Timekeeper.on_message(self, *x),
                on_close=lambda *x: Timekeeper.on_close(self, *x),
                on_error=lambda *x: Timekeeper.on_error(self, *x))
            thread0 = threading.Thread(target=ws.run_forever)
            thread0.start()
            thread1 = threading.Thread(target=self.gametimeLoop)
            thread1.start()
        except Exception as e:
            print(e)
            input('prompt: ')

    def on_open(self, ws):
        ws.send('{"auth":"' + self.auth + '","games":["' + self.gameid + '"]}')
        print("Sent authentication")

    def on_message(self, ws, message):
        print("on_message")
        json_received = json.loads(message)
        # json_received_str = json.dumps(json_received, indent=4, sort_keys=True)
        if 'description' in json_received and json_received['public_id'] == self.gameid:
            if json_received['description'] == 'alive':
                self.json_game_data['alive_timestamp'] = json_received['timestamp']
            elif json_received['description'] == 'complete':
                self.json_game_data = json_received
            elif json_received['description'] == 'delta':
                if not (json_received['added'] is None):  # the 'added' case is not yet interesting for Livestreams
                    print('Not yet needed.')
                if not (json_received['removed'] is None):  # the 'removed' case is not yet interesting for Livestreams
                    print('Not yet needed.')
                if not (json_received['modified'] is None):
                    for key1 in list(json_received['modified']):
                        if isinstance(json_received['modified'][key1],
                                      (dict)):  # you havent reached the bottom and need to dig deeper
                            for key2 in list(json_received['modified'][key1]):
                                if isinstance(json_received['modified'][key1][key2],
                                              (dict)):  # you havent reached the bottom and need to dig deeper
                                    for key3 in list(json_received['modified'][key1][key2]):
                                        if isinstance(json_received['modified'][key1][key2][key3],
                                                      (dict)):  # you havent reached the bottom and need to dig deeper
                                            for key4 in list(json_received['modified'][key1][key2][key3]):
                                                if isinstance(json_received['modified'][key1][key2][key3][key4], (
                                                        dict)):  # you havent reached the bottom and need to dig deeper
                                                    print("ERROR. Didn't know that you're drilling for oil.")
                                                else:  # you reached the bottom and can modify entries
                                                    self.json_game_data[key1][key2][key3][key4] = \
                                                        json_received['modified'][key1][key2][key3][key4]
                                        else:  # you reached the bottom and can modify entries
                                            self.json_game_data[key1][key2][key3] = \
                                            json_received['modified'][key1][key2][
                                                key3]
                                else:  # you reached the bottom and can modify entries
                                    self.json_game_data[key1][key2] = json_received['modified'][key1][key2]
                        else:  # you reached the bottom and can modify entries
                            self.json_game_data[key1] = json_received['modified'][key1]
                    # print(json.dumps(self.json_game_data, indent=4, sort_keys=True))
                    #
            ### write all needed data to files  ###
            ### or to dedicated dicts for class ###
            #######################################
            # jersey team A
            # name team A
            # #####################################################
            #           __                  ___
            #   _  _   /   _ | _  _   _  _   | _ _  _  _  _  _  _   _   _  _|_
            #  | )(_)  \__(_)|(_)|   (_)|    |(-(_||||| )(_||||(-  _)\/| )(_| )
            #                                                        /
            # #####################################################
            score = self.getScore()
            if not self.json_game_data['switched']:
                # teamname_left = self.json_game_data['teams']['A']['name']
                # teamname_right = self.json_game_data['teams']['B']['name']
                score_left = score['A']
                score_right = score['B']

                # self.scoreboard.teamleft.color = self.json_game_data['teams']['A']['jerseyPrimaryColor']
                # self.scoreboard.teamright.color = self.json_game_data['teams']['B']['jerseyPrimaryColor']
            else:
                # teamname_left = self.json_game_data['teams']['B']['name']
                # teamname_right = self.json_game_data['teams']['A']['name']
                score_left = score['B']
                score_right = score['A']
                # self.scoreboard.teamleft.color = self.json_game_data['teams']['B']['jerseyPrimaryColor']
                # self.scoreboard.teamright.color = self.json_game_data['teams']['A']['jerseyPrimaryColor']
            # self.scoreboard.teamleft.name = teamname_left
            # self.scoreboard.teamright.name = teamname_right
            '''
            with io.open("out_teamA.txt", 'w', encoding='utf8') as f:
                f.write(teamname_left)
                f.close()
            # name team B
            with io.open("out_teamB.txt", 'w', encoding='utf8') as f:
                f.write(teamname_right)
                f.close()
            #
            '''
            # print("[CURRENT TEAMS] " + teamname_left + ' - ' + teamname_right)
            # scores
            # print("[CURRENT SCORE] " + score_left + ' - ' + score_right)
            self.scoreboard.teamleft.score_str = score_left
            self.scoreboard.teamright.score_str = score_right

            '''
            # score team A
            with io.open("out_scoreA.txt", 'w', encoding='utf8') as f:
                f.write(score_left)
                f.close()
            # score team B
            with io.open("out_scoreB.txt", 'w', encoding='utf8') as f:
                f.write(score_right)
                f.close()
            '''
            self.scoreboard.write_score()

    def on_error(self, ws, error):
        print("error:", error)

    def on_close(self, ws):
        print("### closed ###")
        sys.exit()

    '''
    def on_open(self, ws):
        print("on open")
        ws.send('{"auth":"' + self.auth + '","games":["' + self.gameid + '"]}')
        print("Sent authentication")
        self.authenticated = True
    '''

    ####################
    #### GAME TIME #####
    ####################
    def getTimestamp_ms(self):
        return int(round(time.time() * 1000))

    def syncToServer(self):  # if result is positive, local time is ahead and server time lags behind
        start = self.getTimestamp_ms()
        server_time = json.loads(
            urllib.request.urlopen(
                "http" + ("s" if self.ssl else "") + "://" + self.remote_server + "/getServerTime.php").read())
        stop = self.getTimestamp_ms()
        self.diff = int((start + stop) / 2 - server_time['time'])
        print("Time self.difference between local and server time is " + str(self.diff) + "ms")

    def getGameTimeString(self, obj, gameduration):
        if obj['active_period'] == 'firstOT':
            self.gametime = self.getFirstOTGameTimeFromGameDuration(obj, gameduration)
        elif obj['active_period'] == 'regular' or obj['active_period'] == 'secondOT':
            self.gametime = gameduration
        minutes = math.floor(self.gametime / 1000 / 60);
        seconds = math.floor(self.gametime / 1000 - minutes * 60)
        return str(minutes).zfill(2) + ":" + str(seconds).zfill(2)

    def getFirstOTGameTimeFromGameDuration(self, obj, gameduration):
        time_left = obj['gametime']['firstOT']['periodLength_ms'] - gameduration
        self.gametime = math.ceil(time_left / 1000) * 1000
        if self.gametime < 0:
            self.gametime = 0
        return self.gametime

    def getFirstOTGameDuration(self):
        if self.json_game_data['gametime']['firstOT']['running']:
            period_gameduration = self.json_game_data['gametime']['firstOT']['gameDurationLastStop_ms'] + (
                    self.getTimestamp_ms() - self.diff) - self.json_game_data['gametime']['firstOT'][
                                      'timeAtLastStart_ms']
            if period_gameduration > self.json_game_data['gametime']['firstOT']['periodLength_ms']:
                period_gameduration = self.json_game_data['gametime']['firstOT']['periodLength_ms']
        else:
            period_gameduration = self.json_game_data['gametime']['firstOT']['gameDurationLastStop_ms']
        return period_gameduration

    def gametimeLoop(self):
        time.sleep(2)  # wait for other threads to connect to websocket and fetch the data
        last_gametime_str = ''
        last_connected = False
        while True:
            if isinstance(self.json_game_data, dict):
                try:
                    if self.json_game_data['active_period'] == 'regular' or self.json_game_data['active_period'] == 'secondOT':
                        if self.json_game_data['gametime'][self.json_game_data['active_period']]['running']:
                            period_gameduration = self.json_game_data['gametime'][self.json_game_data['active_period']][
                                                      'gametimeLastStop_ms'] + (self.getTimestamp_ms() - self.diff) - \
                                                  self.json_game_data['gametime'][self.json_game_data['active_period']][
                                                      'timeAtLastStart_ms']
                        else:
                            period_gameduration = self.json_game_data['gametime'][self.json_game_data['active_period']][
                                'gametimeLastStop_ms']
                    elif self.json_game_data['active_period'] == 'firstOT':
                        period_gameduration = self.getFirstOTGameDuration()
                    gametime_str = self.getGameTimeString(self.json_game_data, period_gameduration)

                    if not gametime_str == last_gametime_str:  # write self.gametime to string if updated
                        print("[PERIOD DURATION]: " + str(period_gameduration / 1000) + "s = " + gametime_str)
                        last_gametime_str = gametime_str
                        self.gametime = gametime_str
                        self.scoreboard.time.time_str = gametime_str
                        '''
                        fwrite = open("out_gametime.txt", "w+")
                        fwrite.write(gametime_str)
                        fwrite.close()
                        '''
                        self.scoreboard.write_timer()

                    if 'alive_timestamp' in self.json_game_data:
                        delta_from_last_alive_ms = (
                                (self.getTimestamp_ms() - self.diff) - self.json_game_data['alive_timestamp'] * 1000)
                        connected = delta_from_last_alive_ms < 30000  # innerhalb von einer halben Minute bekommt man mit, dass man nicht mehr mit dem Timekeeper verbunden ist
                        if not connected == last_connected:
                            last_connected = connected
                            self.connected = connected
                            '''
                            fwrite = open("out_connected.txt", "w+")
                            fwrite.write("true" if connected else "false")
                            fwrite.close()
                            '''
                except Exception as e:
                    print(e)

    ####################
    ####################
    ####################

    ####################
    #### SCORES ########
    ####################
    def getScore(self):
        try:
            points = {'A': 0, 'B': 0}
            points_str = {'A': '0', 'B': '0'}
            periods = ['regular', 'firstOT', 'secondOT']
            for team in list(points):
                for period in periods:
                    period_data = self.json_game_data['score'][team][period]
                    if not (period_data['quaffelPoints'] is None):
                        points[team] += period_data['quaffelPoints']
                    if not (period_data['snitchPoints'] is None):
                        points[team] += period_data['snitchPoints']
                points_str[team] = str(points[team])
            for team in list(points_str):
                other_team = 'A' if team == 'B' else 'B'
                for period in periods:
                    caught = self.json_game_data['score'][team][period]['snitchCaught']
                    caught_other_team = self.json_game_data['score'][other_team][period]['snitchCaught']
                    if not (caught is None):
                        if caught or caught_other_team:
                            if caught:
                                points_str[team] += '*'
                            else:
                                points_str[team] += '°'
                        elif period == 'regular' and not caught and not caught_other_team:
                            break
                        elif period == 'firstOT' and not caught and not caught_other_team and self.getFirstOTGameTimeFromGameDuration(
                                self.json_game_data, self.getFirstOTGameDuration()) == 0:
                            points_str[team] += '°'
                        elif period == 'secondOT' and not caught and not caught_other_team and (
                                points['A'] != points['B']):
                            points_str[team] += '°'
            return points_str

        except Exception as e:
            print(e)


class SnitchCatchWindow(QDialog):
    def __init__(self, scoreboard):
        super().__init__()
        self.ui = Ui_SnitchCatch()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard

    def save(self):
        if self.ui.teamLeftButton.isChecked():
            self.scoreboard.teamleft.catch_first = self.ui.firstCatchButton.isChecked()
            self.scoreboard.teamleft.catch_second = self.ui.secondCatchButton.isChecked()
        if self.ui.teamRightButton.isChecked():
            self.scoreboard.teamright.catch_first = self.ui.firstCatchButton.isChecked()
            self.scoreboard.teamright.catch_second = self.ui.secondCatchButton.isChecked()
        self.accept()
        self.scoreboard.write_score()


class PenaltyWindow(QDialog):
    def __init__(self, scoreboard):
        super().__init__()
        self.ui = Ui_Penalty()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.team = None
        try:
            with io.open("Input/penalty_reasons.txt", "r", encoding="utf-8") as dat:
                self.reasons = dat.readlines()
        except FileNotFoundError:
            self.reasons = []
        # ui setups

    def on_open(self):
        self.ui.teamLeftButton.setText(self.scoreboard.teamleft.name)
        self.ui.teamRightButton.setText(self.scoreboard.teamright.name)

    def team_chosen(self):
        players = []
        if self.ui.teamRightButton.isChecked():
            self.team = self.scoreboard.teamright
            for key, value in self.team.roster.items():
                players.append([str(key), str(value)])

        elif self.ui.teamLeftButton.isChecked():
            self.team = self.scoreboard.teamleft
            for key, value in self.team.roster.items():
                players.append([str(key), str(value)])

        players = sorted(players, key=lambda l: l[1], reverse=False)
        self.ui.list_players.addItems(["{0}: {1}".format(x, y) for x, y in players])
        self.ui.list_reasons.addItems(self.reasons)

    def ok(self):
        if self.ui.input_number.text() != "":
            player = "{0} {1}".format(self.ui.input_number.text(), self.team.roster[self.ui.input_number.text()])
        else:
            player = self.ui.list_players.currentText()
        if self.ui.input_reason.text() != "":
            reason = self.ui.input_reason.text()
            if reason not in self.reasons:
                self.reasons.append(reason)
            self.ui.list_reasons.clear()
            self.ui.list_reasons.addItems(self.reasons)
        else:
            reason = self.ui.list_reasons.currentText()
        if self.ui.redButton.isChecked():
            card = "Red.png"
        elif self.ui.yellowredButton.isChecked():
            card = "YellowRed.png"
        elif self.ui.yellowButton.isChecked():
            card = "Yellow.png"
        elif self.ui.blueButton.isChecked():
            card = "Blue.png"
        self.scoreboard.penalty = {"player": player,
                                   "reason": reason,
                                   "team": self.team,
                                   "card": card
                                   }
        self.scoreboard.write_penalty()
        self.accept()


class SettingsWindow(QDialog):
    def __init__(self, scoreboard):
        super().__init__()
        self.ui = Ui_settings()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.list_of_teams = []
        self.path_main = ""
        # in case settings already are ok.
        # after shutdown or stuff
        self.refresh()
        self.set_from_scoreboard()

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
        self.scoreboard.teamleft.set_path(self.ui.teamLeftOptions.currentText(), "Output/left_path.txt")
        self.scoreboard.teamright.set_path(self.ui.teamRightOptions.currentText(), "Output/right_path.txt")
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

        # refresh Colors (just because)
        colors = ["Red", "Blue", "Green", "Yellow", "Lightgreen", "Choose Color"]
        self.ui.jerseyRightOptions.clear()
        self.ui.jerseyLeftOptions.clear()
        self.ui.jerseyLeftOptions.addItems(colors)
        self.ui.jerseyRightOptions.addItems(colors)

    def swap(self):
        r = self.ui.jerseyRightOptions.currentIndex()
        l = self.ui.jerseyLeftOptions.currentIndex()
        self.ui.jerseyRightOptions.setCurrentIndex(l)
        self.ui.jerseyLeftOptions.setCurrentIndex(r)
        r = self.ui.teamRightOptions.currentIndex()
        l = self.ui.teamLeftOptions.currentIndex()
        self.ui.teamRightOptions.setCurrentIndex(l)
        self.ui.teamLeftOptions.setCurrentIndex(r)
        self.scoreboard.swap()


class TimekeeperWindow(QDialog):
    def __init__(self, scoreboard, main_ui):
        super().__init__()
        self.ui = Ui_Timekeeper()
        self.ui.setupUi(self)
        self.timekeeper = None
        self.scoreboard = scoreboard
        self.main = main_ui

    def connect(self):
        self.timekeeper = Timekeeper(self.ui.gameID.displayText(), self.ui.auth.displayText(), self.scoreboard)
        self.timekeeper.connect()
        self.scoreboard.timekeeper = self.timekeeper
        print("got here")
        self.main.timerLayout.setEnabled(False)
        self.accept()


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.scoreboard = ScoreBoard(self)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.show()
        # in case of restart
        self.scoreboard.read_all()
        self.set_from_scoreboard()

        self.timekeeper_w = TimekeeperWindow(self.scoreboard, self.ui)
        self.penalty_w = PenaltyWindow(self.scoreboard)
        self.settings_w = SettingsWindow(self.scoreboard)
        self.settings_w.show()
        self.snitch_w = SnitchCatchWindow(self.scoreboard)

        time_thread = threading.Thread(target=self.update_timer_ui)
        time_thread.start()

    def set_from_scoreboard(self):
        self.ui.time_label.setText(self.scoreboard.time.time_str)
        self.update_score_ui()
        self.update_team_ui()

    def start_timer(self):
        self.scoreboard.time.start()

    def stop_timer(self):
        self.scoreboard.time.stop()

    def set_timer(self):
        time = self.ui.timeEdit.time()
        self.scoreboard.time.set(ui_label=self.ui.time_label, minutes=time.minute(), seconds=time.second())

    def add_left(self, amount):
        self.scoreboard.teamleft.score += amount
        self.update_score_ui()

    def reset_left(self):
        self.scoreboard.teamleft.score = 0
        self.scoreboard.teamleft.catch_second = False
        self.scoreboard.teamleft.catch_first = False
        self.update_score_ui()

    def reset_right(self):
        self.scoreboard.teamright.score = 0
        self.scoreboard.teamright.catch_first = False
        self.scoreboard.teamright.catch_second = False
        self.update_score_ui()

    def add_right(self, amount):
        self.scoreboard.teamright.score += amount
        self.update_score_ui()

    def timekeeper_start(self):
        self.timekeeper_w.show()

    def settings_start(self):
        self.settings_w.show()

    def snitch_catch(self):
        self.snitch_w.show()

    def open_penalty(self):
        self.penalty_w.show()
        self.penalty_w.on_open()

    def update_team_ui(self):
        self.ui.teamname_left.setText(self.scoreboard.teamleft.name)
        self.ui.teamname_right.setText(self.scoreboard.teamright.name)

    def update_timer_ui(self):
        while self.result() == 0:
            self.ui.time_label.setText(self.scoreboard.time.time_str)
            time.sleep(0.5)

    def update_score_ui(self):
        self.ui.score_right.setText(str(self.scoreboard.teamright.get_score_str()))
        self.ui.score_left.setText(str(self.scoreboard.teamleft.get_score_str()))
        self.scoreboard.write_score()

    def close(self):
        self.accept()


class ScoreBoard:
    def __init__(self, window):
        self.teamleft = Team()
        self.teamright = Team()
        self.time = Timer(self)
        self.window = window
        self.penalty = {}  # all information about a specific penalty will be saved in this dict

    def read_all(self):
        if os.path.isdir("Output"):
            try:
                with io.open("Output/score_left.txt", "r", encoding="utf-8") as dat:
                    line = dat.readline()
                    if (line[-1] == "*") or (line[-1] == "°"):
                        if line[-1] == "*":
                            self.teamleft.catch_first = True
                        if line[-1] == "°":
                            self.teamleft.catch_second = True
                        self.teamleft.score = int(line[:-1])
                    else:
                        self.teamleft.score = int(line)
            except FileNotFoundError:
                None

            try:
                with io.open("Output/score_right.txt", "r", encoding="utf-8") as dat:
                    line = dat.readline()
                    if (line[-1] == "*") or (line[-1] == "°"):
                        if line[-1] == "*":
                            self.teamright.catch_first = True
                        if line[-1] == "°":
                            self.teamright.catch_second = True
                        self.teamright.score = int(line[:-1])
                    else:
                        self.teamright.score = int(line)
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
        x, y = 200, 120  # size of output Image

        if self.teamright.color == "" or self.teamright.color=="":
            print("Please choose colors for the jerseys!")
            return

        # write for team right
        im = Image.new("RGBA", (x, y))
        dr = ImageDraw.Draw(im)
        dr.polygon([(0, y), (x / 2, y), (x, 0), (x / 2, 0)], fill=self.teamright.color, outline=None)
        im.save("Output/TeamRightJersey.png")
        # write for team left
        im = Image.new("RGBA", (x, y))
        dr = ImageDraw.Draw(im)
        dr.polygon([(0, y), (x / 2, y), (x, 0), (x / 2, 0)], fill=self.teamleft.color, outline=None)
        im.save("Output/TeamLeftJersey.png")

    def write_timer(self):
        with open("Output/timer.txt", "w") as dat:
            dat.write(self.time.time_str)

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


class Team:
    def __init__(self):
        self.color = ""
        self.score = 0
        self.score_str = ""
        self.name = ""
        self.catch_first = False
        self.catch_second = False
        self.path = ""
        self.logo = ""
        self.roster = {}

    def get_score_str(self):
        if self.score_str != "":
            return self.score_str
        out = str(self.score)
        if self.catch_first:
            out += "*"
        if self.catch_second:
            out += "°"
        return out

    def set_path(self, path, datafile=""):
        self.path = path
        if not datafile == "":
            with open(datafile, "w") as dat:
                dat.write(self.path)
        # set logo path
        self.logo = "Input/Teamlogos/" + self.path + ".png"
        # set name and roster
        try:
            with codecs.open("Input/Teamrosters/"+self.path+".txt", "r", 'utf-8') as roster_file:
                content = roster_file.readlines()
                self.name = content[0][0:-1]
            for line in content[1:]:
                if ":" not in line:
                    continue
                number, name = line.split(":")
                self.roster[number] = name
        except FileNotFoundError as e:
            print(e)


class Timer:
    def __init__(self, scoreboard, upCounting=True):
        self.up = upCounting
        self.time_str = "00:00"
        self.sec = 0
        self.min = 0
        self.running = False
        self.label = None
        self.scoreboard = scoreboard

    def start(self):
        timer_thread = threading.Thread(target=self.run)
        self.running = True
        timer_thread.start()

    def run(self):
        while self.running:
            # down counting:
            if not self.up:
                if self.sec == self.min == 0:
                    self.running = False
                elif self.sec > 0:
                    self.sec = self.sec-1
                else:
                    self.sec = 59
                    self.min = self.min-1
            # up counting:
            else:
                if self.sec < 59:
                    self.sec = 1+self.sec
                else:
                    self.sec = 0
                    self.min = 1+self.min
            self.time_str = "%02d" % self.min + ":" + "%02d" % self.sec
            time.sleep(1)
            self.scoreboard.write_timer()

    def stop(self):
        self.running = False

    def set(self, ui_label, minutes, seconds):
        self.stop()
        time.sleep(1.01)
        self.min = minutes
        self.sec = seconds
        self.time_str = "%02d" % self.min + ":" + "%02d" % self.sec
        ui_label.setText(self.time_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    updater = threading.Thread(target=w.update)
    updater.start()
    sys.exit(app.exec_())
