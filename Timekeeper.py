import urllib.request
import json
import math
import websocket
import threading
import sys
import time


class Timekeeper:
    def __init__(self, scoreboard, main_window):
        self.gametime = 0
        self.gameid = ""
        self.data = 0
        self.json_game_data = {}
        self.diff = 0
        self.auth = ""  # authentication
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
        self.break_connection = False
        self.ws = None
        self.main_window = main_window

    def connect(self):
        try:
            config = json.loads(
                urllib.request.urlopen("http://" + self.remote_server + "/getStreamingSettings.php").read().decode(
                    "utf-8"))
            # print(config)
            self.ws = websocket.WebSocketApp(
                "ws" + ("s" if self.ssl else "") + "://" + config['server'] + ":" + str(self.port) + "/ws",
                on_open=lambda *x: Timekeeper.on_open(self, *x),
                on_message=lambda *x: Timekeeper.on_message(self, *x),
                on_close=lambda *x: Timekeeper.on_close(self, *x),
                on_error=lambda *x: Timekeeper.on_error(self, *x))
            self.connected = True
            thread0 = threading.Thread(target=self.ws.run_forever)
            thread0.start()
            thread1 = threading.Thread(target=self.gametimeLoop)
            thread1.start()
        except Exception as e:
            print(e)
            self.connected = False

    def on_open(self, ws):
        ws.send('{"auth":"' + self.auth + '","games":["' + self.gameid + '"]}')

    def on_message(self, ws, message):
        json_received = json.loads(message)
        # json_received_str = json.dumps(json_received, indent=4, sort_keys=True)
        if 'description' in json_received and json_received['public_id'] == self.gameid:
            # print("recieved dict from ", self.gameid)
            if json_received['description'] == 'alive':
                self.json_game_data['alive_timestamp'] = json_received['timestamp']
            elif json_received['description'] == 'complete':
                self.json_game_data = json_received
            elif json_received['description'] == 'delta':
                if not (json_received['added'] is None):  # the 'added' case is not yet interesting for Livestreams
                    # # print('Not yet needed.')
                    None
                if not (json_received['removed'] is None):  # the 'removed' case is not yet interesting for Livestreams
                    # # print('Not yet needed.')
                    None
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
                                                    None
                                                    # print("ERROR. Didn't know that you're drilling for oil.")
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
                    # # print(json.dumps(self.json_game_data, indent=4, sort_keys=True))
                    #
            ### write all needed data to files  ###
            ### or to dedicated dicts for class ###
            #######################################
            # jersey team A
            # name team A
            # #####################################################
            #              __                      ___
            #   _  _ |    (_  _ _  _ _   _  _  _|   | . _  _
            #  (_)| )|\/  __)(_(_)| (-  (_|| )(_|   | ||||(-
            #         /
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
            self.main_window.update_score_ui()
        # print("through with message")

    def on_error(self, ws, error):
        print("error:", error)
        self.connected = False

    def on_close(self, ws):
        print("### closed ###")
        self.connected = False
        sys.exit()

    '''
    def on_open(self, ws):
        # print("on open")
        ws.send('{"auth":"' + self.auth + '","games":["' + self.gameid + '"]}')
        # print("Sent authentication")
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
        # print("Time self.difference between local and server time is " + str(self.diff) + "ms")

    def getGameTimeString(self, obj, gameduration):
        if obj['active_period'] == 'firstOT':
            self.gametime = self.getFirstOTGameTimeFromGameDuration(obj, gameduration)
        elif obj['active_period'] == 'regular' or obj['active_period'] == 'secondOT':
            self.gametime = gameduration
        minutes = math.floor(self.gametime / 1000 / 60)
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

    '''
    def gametimeLoop(self):
        time.sleep(2)  # wait for other threads to connect to websocket and fetch the data
        last_gametime_str = ''
        last_connected = False
        while True:
            if self.break_connection:
                return
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
                        # print("[PERIOD DURATION]: " + str(period_gameduration / 1000) + "s = " + gametime_str)
                        last_gametime_str = gametime_str
                        self.gametime = gametime_str
                        self.scoreboard.time.time_str = gametime_str

                        fwrite = open("out_gametime.txt", "w+")
                        fwrite.write(gametime_str)
                        fwrite.close()

                        self.scoreboard.write_timer()

                    if 'alive_timestamp' in self.json_game_data:
                        delta_from_last_alive_ms = (
                                (self.getTimestamp_ms() - self.diff) - self.json_game_data['alive_timestamp'] * 1000)
                        connected = delta_from_last_alive_ms < 30000  # innerhalb von einer halben Minute bekommt man mit, dass man nicht mehr mit dem Timekeeper verbunden ist
                        if not connected == last_connected:
                            last_connected = connected
                            self.connected = connected

                            fwrite = open("out_connected.txt", "w+")
                            fwrite.write("true" if connected else "false")
                            fwrite.close()

                except Exception as e:
                    # print("exception Gametimeloop: ", e)
                    input('prompt: ')

    ####################
    ####################
    ####################

    ####################
    #### SCORES ########
    ####################
    '''

    def gametimeLoop(self):
        time.sleep(2)  # wait for other threads to connect to websocket and fetch the data
        last_gametime_str = ''
        gametime_str = ''
        # last_connected = False
        while True:
            time.sleep(0.2)
            self.syncToServer()
            if self.break_connection:
                return
            if isinstance(self.json_game_data, dict):
                # print("yea is instance")
                try:
                    if 'active_period' in self.json_game_data:
                        if self.json_game_data['active_period'] == 'regular' or self.json_game_data['active_period'] == 'secondOT':
                            if self.json_game_data['gametime'][self.json_game_data['active_period']]['running']:
                                period_gameduration = self.json_game_data['gametime'][self.json_game_data['active_period']]['gametimeLastStop_ms'] + (self.getTimestamp_ms() - self.diff) - self.json_game_data['gametime'][self.json_game_data['active_period']]['timeAtLastStart_ms']
                            else:
                                period_gameduration = self.json_game_data['gametime'][self.json_game_data['active_period']]['gametimeLastStop_ms']
                        elif self.json_game_data['active_period'] == 'firstOT':
                            period_gameduration = self.getFirstOTGameDuration()
                        gametime_str = self.getGameTimeString(self.json_game_data, period_gameduration)

                    if not gametime_str == last_gametime_str:  # write gametime to string if updated
                        # print("[PERIOD DURATION]: " + str(period_gameduration / 1000) + "s = " + gametime_str)
                        last_gametime_str = gametime_str
                        self.scoreboard.time.time_str = gametime_str
                        # self.main_window.update_timer_ui()
                        # fwrite = open("out_gametime.txt", "w+")
                        # fwrite.write(gametime_str)
                        # fwrite.close()

                    # if 'alive_timestamp' in self.json_game_data:
                    #    delta_from_last_alive_ms = (
                    #             (self.getTimestamp_ms() - self.diff) - self.json_game_data['alive_timestamp'] * 1000)
                    #     connected = delta_from_last_alive_ms < 30000
                    # innerhalb von einer halben Minute bekommt man mit, dass man nicht mehr mit dem Timekeeper verbunden ist
                    # if not connected == last_connected:
                    #     last_connected = connected
                    #     self.connected = connected
                    # fwrite = open("out_connected.txt", "w+")
                    # fwrite.write("true" if connected else "false")
                    # fwrite.close()
                except Exception as e:
                    self.connected = False
                    print("Error in gametimeloop:", e)

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
            self.connected = False
            print("Error in score:", e)
