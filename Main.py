from tkinter import *
import os
import shutil
# from PIL import ImageTk
from PIL import Image
import codecs

# import time


def donothing():
    return None


class Timer:
    '''
        sets up a Timer with a span of 4 cols and 4 rows
        takes a master, upper left corner and a boolean to tell it to count up or down
    '''

    def __init__(self, master, col, row, countdown):
        self.update_id = None
        self.master = master
        self.countdown = countdown
        self.running = False
        if countdown:
            self.timer_label = Label(master, text="Down counting timer (set start)")
            self.timer_file = "Output/timer_down.txt"
        else:
            self.timer_label = Label(master, text="Up counting timer (set start)")
            self.timer_file = "Output/timer_up.txt"
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

        self.timer_reset = Button(master, command=self.reset, text="Reset")
        self.timer_reset.grid(columnspan=2, column=col + 4, row=row + 3, sticky=E + W)

    def start(self):
        if self.running:
            self.master.after_cancel(self.update_id)
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
                with open(self.timer_file, "w") as f:
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
            self.update_id = self.master.after(1000, self.update_timer)

    def pause(self):
        self.running = False
        self.master.after_cancel(self.update_id)
        self.timer_set.delete(0, END)
        self.timer_set.insert(0, "%02d" % (int(self.minutes),)+":"+"%02d" % (int(self.seconds),))

    def reset(self):
        self.running = False
        self.master.after_cancel(self.update_id)
        self.timer_set.delete(0, END)
        self.current_time.set("%02d" % (0,) + ":" + "%02d" % (0,))
        with open(self.timer_file, "w") as f:
            f.write("%02d" % (0,) + ":" + "%02d" % (0,))


class Team:
    def __init__(self, team_type):
        self.logo = None
        self.name = StringVar()
        self.roster = {}   # Roster will be setup as a Dict with Number as key and name as element
        self.is_set = False
        self.team_type = team_type

    def set(self, team_name, destfile):
        self.logo = team_name+".png"
        self.logo = "Input/Teamlogos/{}.png".format(team_name)
        try:
            shutil.copyfile(self.logo, "Output/"+destfile)
        except FileExistsError:
            os.remove("Output/"+destfile)
            shutil.copyfile(self.logo, "Output/"+destfile)
        # ---- set National Flag ----
        try:
            shutil.copyfile("Input/TeamFlagsUpright/"+team_name+".png", "Output/"+self.team_type+"FlagUpright.png")
        except FileExistsError:
            os.remove("Output/"+self.team_type+"FlagUpright.png")
            shutil.copyfile("Input/TeamFlagsUpright/"+team_name+".png", "Output/"+self.team_type+"FlagUpright.png")
        try:
            shutil.copyfile("Input/TeamFlags/"+team_name+".png", "Output/"+self.team_type+"Flag.png")
        except FileExistsError:
            os.remove("Output/"+self.team_type+"Flag.png")
            shutil.copyfile("Input/TeamFlags/"+team_name+".png", "Output/"+self.team_type+"Flag.png")
        # ---- Set roster ----
        # with open("Input/Teamrosters/"+team_name+".txt", "r", encoding="utf8") as roster_file:
        with codecs.open("Input/Teamrosters/"+team_name+".txt", "r", 'iso-8859-1') as roster_file:
            content = roster_file.readlines()
            print(content)
            self.name.set(content[0][1:-1])
        for line in content[1:]:
            print(line)
            number, name = line.split(":")
            self.roster[number] = name
        with open("Output/{}.txt".format(self.team_type), "w") as file:
            file.write(self.name.get())
        self.is_set = True

    def set_color(self, colorfile):
        #
        # Setting jersey color for team from colors in Input/Jerseycolors
        # to Output/Team(A/B)jersey.png
        #
        try:
            shutil.copyfile("Input/Jerseycolors/"+colorfile, "Output/"+self.team_type+"jersey.png")
        except FileExistsError:
            os.remove("Output/"+self.team_type+"jersey.png")
            shutil.copyfile("Input/Jerseycolors/"+colorfile, "Output/"+self.team_type+"jersey.png")


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


class ScoreBoardGUI:

    def __init__(self, master):
        self.penalty_set = False
        self.penalty_objects = []
        # try Output folder:
        try:
            os.listdir("Output")
        except FileNotFoundError:
            os.makedirs("Output")
        col = 0
        row = 1
        self.team_one = Team("TeamA")
        self.team_two = Team("TeamB")
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
        self.timer_down = Timer(master=self.master, col=col+6, row=row+3, countdown=True)  # takes 4 rows!

        self.penalty_column = col
        self.penalty_row = row + 7
        self.setup_penalties()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(columnspan=8, column=col, sticky=E+W)

    def setup_teams(self):
        # ---- find participating teams by logos ----
        listofteams = []
        try:
            for team in os.listdir("Input/Teamlogos"):
                if team[-4:] == ".png":
                    listofteams.append(team[:-4])
        except FileNotFoundError:
            listofteams = []

        # ---- Find Jersey Colors -----
        jerseys = []
        try:
            for color in os.listdir("Input/Jerseycolors"):
                jerseys.append(color)
        except FileNotFoundError:
            print("Please Add all jersey colors as png in Folder Input/Jerseycolors")

        # ---- Setup Team Menu ----
        menubar = Menu(self.master)

        team_menu_one = Menu(menubar, tearoff=0)
        for team in listofteams:
            team_menu_one.add_command(label=team,
                                      command=lambda team=team: [self.team_one.set(str(team),
                                                                                  "TeamALogo.png"), self.setup_penalties()])
        menubar.add_cascade(label="Set Team A", menu=team_menu_one)

        jersey_one_menu = Menu(menubar, tearoff=0)
        for color in jerseys:
            pic = Image.open("Input/Jerseycolors/" + color)
            bg_color = "#%02x%02x%02x" % pic.getpixel((pic.size[0] // 2, pic.size[1] // 2))[:3]
            jersey_one_menu.add_command(label=color,
                                        command=lambda color=color, bg_color=bg_color: [self.team_one.set_color(color),
                                                                     self.team_one_label.config(bg=bg_color)])

        menubar.add_cascade(label="Jersey Team A", menu=jersey_one_menu)
        
        team_menu_two = Menu(menubar, tearoff=0)
        for team in listofteams:
            team_menu_two.add_command(label=str(team),
                                      command=lambda team=team: [self.team_two.set(str(team),
                                                                 "TeamBLogo.png"), self.setup_penalties()])
        menubar.add_cascade(label="Set Team B", menu=team_menu_two)

        jersey_two_menu = Menu(menubar, tearoff=0)
        for color in jerseys:
            pic = Image.open("Input/Jerseycolors/"+color)
            bg_color = "#%02x%02x%02x" % pic.getpixel((pic.size[0]//2, pic.size[1]//2))[:3]
            jersey_two_menu.add_command(label=color,
                                        command=lambda color=color, bg_color=bg_color: [self.team_two.set_color(color),
                                                                     self.team_two_label.config(bg=bg_color)])

        menubar.add_cascade(label="Jersey Team B", menu=jersey_two_menu)
        
        self.master.config(menu=menubar)

    def setup_penalties(self):
        # Setup a penalty menu, with Cards, team, number of player and reasons
        col = self.penalty_column
        row = self.penalty_row

        if self.team_one.is_set and self.team_two.is_set:
            if self.penalty_set:
                # print("going to")
                # print(self.penalty_objects)
                self.destroy_penalty()
                self.penalty_objects = []
                # print("destroyed it")
            self.chosen_team_penalty = IntVar()
            self.close_button.destroy()
            # -------------------
            # Setup Penalty area
            # -------------------
            #
            # simple Label and chose button for team
            label_buttons = Label(self.master,
                                  text="Choose a Team:",
                                  justify=LEFT,
                                  padx=20)
            label_buttons.grid(column=col, row=row, columnspan=8)
            self.penalty_objects.append(label_buttons)

            rad_b1 = Radiobutton(self.master,
                        text=self.team_one.name.get(),
                        padx=20,
                        variable=self.chosen_team_penalty,
                        value=1)
            rad_b1.grid(column=col, row=row+1, columnspan=4)
            self.penalty_objects.append(rad_b1)

            rad_b2=Radiobutton(self.master,
                        text=self.team_two.name.get(),
                        padx=20,
                        variable=self.chosen_team_penalty,
                        value=2)
            rad_b2.grid(column=col+4, row=row + 1, columnspan=4)
            self.penalty_objects.append(rad_b2)
            # set number of Player:

            playernumber_label = Label(self.master,
                  text="Jersey number of Player:",
                  justify=LEFT)
            playernumber_label.grid(column=col,
                                     row=row+2,
                                     columnspan=2,
                                     sticky=W)
            self.penalty_objects.append(playernumber_label)

            self.player_num_penalty = Entry(self.master)
            self.penalty_objects.append(self.player_num_penalty)
            self.player_num_penalty.grid(column=col+3, row=row+2, columnspan=5, sticky=E+W)
            # player_num.get()
            # --------------------------------
            # set chose cards radio buttons:
            #       Blue=1 Yellow=2 Yellow/Red=3 Red=4 
            # --------------------------------
            label_cards = Label(self.master,
                  text="Card:",
                  justify=LEFT)
            label_cards.grid(column=col,
                  row=row+3,
                  columnspan=2,
                  sticky=W)
            self.penalty_objects.append(label_cards)
            self.chosen_card = IntVar()
            # ------ Blue -----
            rad1 = Radiobutton(self.master,
                        text="Blue",
                        padx=20,
                        variable=self.chosen_card,
                        value=1)
            rad1.grid(column=col+2, row=row+3, columnspan=2)
            self.penalty_objects.append(rad1)
            # ------ Yellow -----
            rad2 = Radiobutton(self.master,
                               text="Yellow",
                               padx=20,
                               variable=self.chosen_card,
                               value=2)
            rad2.grid(column=col + 4, row=row + 3, columnspan=2)
            self.penalty_objects.append(rad2)
            # ------ Yellow/Red -----
            rad3 = Radiobutton(self.master,
                               text="Yellow/Red",
                               padx=20,
                               variable=self.chosen_card,
                               value=3)
            rad3.grid(column=col + 6, row=row + 3, columnspan=2)
            self.penalty_objects.append(rad3)
            # ------ Red -----
            rad4 = Radiobutton(self.master,
                               text="Red",
                               padx=20,
                               variable=self.chosen_card,
                               value=4)
            rad4.grid(column=col + 8, row=row + 3, columnspan=2)
            self.penalty_objects.append(rad4)

            # -------------------------
            # Reason for Penalty:
            # -------------------------
            label_reason = Label(self.master,
                                              text="Reason:",
                                              justify=LEFT)
            label_reason.grid(column=col,
                              row=row+4,
                              columnspan=2,
                              sticky=W)
            self.penalty_objects.append(label_reason)
            self.penalty_reason = Entry(self.master)
            self.penalty_objects.append(self.penalty_reason)
            self.penalty_reason.grid(column=col+3, row=row+4, columnspan=5, sticky=E+W)
            # -----------------------
            # Execution Button
            # -----------------------
            exec_button = Button(self.master,
                   text="Execute penalty",
                   command=self.penalty_execution)
            exec_button.grid(column=col+1,
                                                        row=row+5,
                                                        columnspan=6,
                                                        sticky=E+W)
            self.penalty_objects.append(exec_button)
            self.penalty_set = True
            # -------------------
            # Reset close button
            # -------------------
            self.close_button = Button(self.master, text="Close", command=self.master.quit)
            self.close_button.grid(columnspan=8, column=col, sticky=E+W)
        # else:
        #     self.master.after(1000, lambda: self.setup_penalties)

    def penalty_execution(self):
        # -------------------------
        # Move Card png to Output
        # -------------------------
        if self.chosen_card.get() == 1:
            try:
                shutil.copyfile("Input/Cards/Blue.png", "Output/card.png")
            except FileExistsError:
                os.remove("Output/card.png")
                shutil.copyfile("Input/Cards/Blue.png", "Output/card.png")
        if self.chosen_card.get() == 2:
            try:
                shutil.copyfile("Input/Cards/Yellow.png", "Output/card.png")
            except FileExistsError:
                os.remove("Output/card.png")
                shutil.copyfile("Input/Cards/Yellow.png", "Output/card.png")
        if self.chosen_card.get() == 3:
            try:
                shutil.copyfile("Input/Cards/YellowRed.png", "Output/card.png")
            except FileExistsError:
                os.remove("Output/card.png")
                shutil.copyfile("Input/Cards/YellowRed.png", "Output/card.png")
        if self.chosen_card.get() == 3:
            try:
                shutil.copyfile("Input/Cards/YellowRed.png", "Output/card.png")
            except FileExistsError:
                os.remove("Output/card.png")
                shutil.copyfile("Input/Cards/YellowRed.png", "Output/card.png")
        # ------------------------------
        # Move Playername and Number:
        # ------------------------------
        with open("Output/penalty_reason.txt", "w") as pen_file:
            pen_file.write(self.penalty_reason.get())
        if self.chosen_team_penalty.get() == 1:
            team = self.team_one
        else:
            team = self.team_two
        with open("Output/penalty_player.txt", "w") as pen_file:
            pen_file.write(self.player_num_penalty.get() + " " + team.roster[self.player_num_penalty.get()])
        with open("Output/penalty_team.txt", "w") as pen_file:
            pen_file.write(team.name.get())
        return None

    def destroy_penalty(self):
        for i in self.penalty_objects:
            i.destroy()


root = Tk()
# root.resizable(False, False)

root.geometry("600x400")
my_gui = ScoreBoardGUI(root)
root.mainloop()
root.destroy()  # optional; see description below
