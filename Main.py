from tkinter import *
import os
import shutil
# import time


def donothing():
    return None


class Timer:
    '''
        sets up a Timer with a span of 4 cols and 4 rows
        takes a master, upper left corner and a boolean to tell it to count up or down
    '''

    def __init__(self, master, col, row, countdown):
        self.master = master
        self.countdown = countdown
        self.running = False
        if countdown:
            self.timer_label = Label(master, text="Down counting timer (set start)")
        else:
            self.timer_label = Label(master, text="Up counting timer (set start)")
        self.timer_label.grid(columnspan=4, column=col, row=row)

        #Entry
        self.timer_set = Entry(master)
        self.timer_set.insert(0, "min:sec")
        self.timer_set.grid(columnspan=4, column=col, row=row+1)

        #Current Timer
        self.current_time = StringVar()
        self.current_label = Label(master, textvariable=self.current_time, relief=GROOVE)
        self.current_label.grid(columnspan=4, column=col, row=row+2, sticky=E+W)

        #Buttons
        self.timer_start = Button(master, command=self.start, text="Start")
        self.timer_start.grid(columnspan=2, column=col, row=row+3, sticky=E+W)

        self.timer_pause = Button(master, command=self.pause, text="Pause")
        self.timer_pause.grid(columnspan=2, column=col+2, row=row+3, sticky=E+W)

    def start(self):
        self.running = True
        if self.countdown:
            self.minutes, self.seconds = self.timer_set.get().split(":")
            self.current_time.set(self.minutes+":"+self.seconds)
        else:
            self.minutes, self.seconds = self.timer_set.get().split(":")
            self.current_time.set(self.minutes + ":" + self.seconds)
        self.update_timer()

    def update_timer(self):
        if self.running:
            if self.countdown:
                if int(self.seconds) == int(self.minutes) == 0:
                    self.running = False
                elif int(self.seconds) > 0:
                    self.seconds = str(int(self.seconds)-1)
                else:
                    self.seconds = str(59)
                    self.minutes = str(int(self.minutes)-1)
                with open("Output/timer_down.txt", "w") as f:
                    f.write("%02d" % (int(self.minutes),)+":"+"%02d" % (int(self.seconds),))
            else:
                if int(self.seconds) < 59:
                    self.seconds = str(1+int(self.seconds))
                else:
                    self.seconds = str(0)
                    self.minutes = str(1+int(self.minutes))
                with open("Output/timer_up.txt", "w") as f:
                    f.write("%02d" % (int(self.minutes),)+":"+"%02d" % (int(self.seconds),))
            self.current_time.set("%02d" % (int(self.minutes),)+":"+"%02d" % (int(self.seconds),))
            self.master.after(1000, self.update_timer)

    def pause(self):
        self.running = False
        self.timer_set.delete(0, END)
        self.timer_set.insert(0, "%02d" % (int(self.minutes),)+":"+"%02d" % (int(self.seconds),))


class Team:
    def __init__(self):
        self.logo = None
        self.name = StringVar()
        self.roster = {}   # Roster will be setup as a Dict with name as key and number as content

    def set(self, team_name, destfile):
        self.logo = team_name+".png"
        self.logo = "Input/Teamlogos/{}.png".format(team_name)
        try:
            shutil.copyfile(self.logo, "Output/"+destfile)
        except FileExistsError:
            os.remove("Output/"+destfile)
            shutil.copyfile(self.logo, "Output/"+destfile)
        with open("Input/Teamrosters/"+team_name+".txt", "r") as roster_file:
            content = roster_file.readline()
            self.name.set(content[0][:-1])
        for line in content[1:]:
            number, name = line.split(":")
            self.roster[name] = int(number)


class Score:

    def __init__(self, master, column, row, label_left, filenumber):
        self.filenumber = filenumber
        try:
            with open("Output/score{}.txt".format(filenumber), "r+") as scorefile:
                self.current = int(scorefile.readline())
        except FileNotFoundError:
            f = open("Output/scores.txt", "w")
            f.write("0")
            f.close()
            self.current = 0

        self.score = StringVar()
        self.score.set(str(self.current))
        self.label = Label(master, textvariable=self.score)

        self.add = Button(master, text="+10",
                          command=lambda: self.addScore("add"))
        self.sub = Button(master, text="-10",
                          command=lambda: self.addScore("subtract"))
        self.res = Button(master, text="reset",
                          command=lambda: self.addScore("reset"))
        if label_left:
            self.label.grid(column=column, row=row)
            self.add.grid(column=column+1, row=row)
            self.sub.grid(column=column+2, row=row)
            self.res.grid(column=column+3, row=row)
        else:
            self.label.grid(column=column+3, row=row)
            self.add.grid(column=column+2, row=row)
            self.sub.grid(column=column+1, row=row)
            self.res.grid(column=column, row=row)

    def addScore(self, method):
        if method == "add":
            self.current = self.current + 10
        if method == "subtract":
            self.current = self.current - 10
        if method == "reset":
            self.current = 0
        self.score.set(str(self.current))
        with open("Output/score{}.txt".format(self.filenumber), 'w') as f:
            f.write(str(self.current))


class MyFirstGUI:

    def __init__(self, master):
        # try Output folder:
        try:
            os.listdir("Output")
        except FileNotFoundError:
            os.makedirs("Output")
        col = 0
        row = 1
        self.team_one = Team()
        self.team_two = Team()
        self.master = master
        master.title("Scoreboard 2.0")

        self.team_one_label = Label(master, textvariable=self.team_one.name)
        self.team_one_label.grid(column=0, columnspan=4, row=row-1)

        self.team_two_label = Label(master, textvariable=self.team_two.name)
        self.team_two_label.grid(column=4, columnspan=4, row=row-1)

        self.scoreone = Score(master, column=col+0, row=row+2, label_left=False, filenumber=0)
        self.scoretwo = Score(master, column=col+4, row=row+2, label_left=True, filenumber=1)

        self.setup_teams()

        self.timer_up = Timer(master=self.master, col=col, row=row+3, countdown=False)
        self.timer_down = Timer(master=self.master, col=col+4, row=row+3, countdown=True)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(columnspan=8, column=col, sticky=E+W)

    def setup_teams(self):
        listofteams = []
        try:
            for team in os.listdir("Input/Teamlogos"):
                if team[-4:] == ".png":
                    listofteams.append(team[:-4])
        except FileNotFoundError:
            listofteams = []

        menubar = Menu(self.master)

        team_menu_one = Menu(menubar, tearoff=0)
        for team in listofteams:
            team_menu_one.add_command(label=team,
                                      command=lambda team=team: self.team_one.set(str(team),
                                                                                  "TeamA.png"))
        menubar.add_cascade(label="Set Team A", menu=team_menu_one)
        
        team_menu_two = Menu(menubar, tearoff=0)
        for team in listofteams:
            team_menu_two.add_command(label=str(team),
                                      command=lambda team=team: self.team_two.set(str(team),
                                                                                  "TeamB.png"))
        menubar.add_cascade(label="Set Team B", menu=team_menu_two)
        self.master.config(menu=menubar)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
root.destroy()  # optional; see description below
