import subprocess

class Timekeeper:
    def __init__(self, scoreboard, main_window):
        self.gametime = 0
        self.gameid = ""
        self.data = 0
        self.json_game_data = {}
        self.diff = 0
        self.remote_server = 'quadball.live'  # 'timekeeper.lucas-scheuvens.de'
        self.ssl = True  # if self.remote_server == 'timekeeper.lucas-scheuvens.de' else False
        self.port = 443  # if self.remote_server == 'timekeeper.lucas-scheuvens.de' else 8769
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

    def connect_js(self, gameid):
        self.timekeeper_proc = subprocess.Popen('node .\quadballlive_api\quadballlive_api.js' + " " + gameid)
        self.connected = True

    def disconnect_js(self):
        self.timekeeper_proc.kill()
        open("quadballlive_api/connected.txt", "w").write("false")
        self.connected = False