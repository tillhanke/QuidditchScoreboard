from Timer import *
from Team import *
from Score import *
import os
import shutil
from PIL import Image
from tkinter import filedialog
# compiled with https://pyinstaller.readthedocs.io/en/stable/usage.html


def donothing():
    return None


class ScoreBoardGUI:

    def __init__(self, master):
        self.path_main = StringVar()
        self.path_main.set("")
        self.penalty_set = False
        self.penalty_objects = []
        # try Output folder:
        try:
            os.listdir(self.path_main.get() + "Output")
        except FileNotFoundError:
            os.makedirs(self.path_main.get() + "Output")
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

        lbl1 = Label(master=root, textvariable=self.path_main)
        lbl1.grid(columnspan=8, column=col)
        button2 = Button(text="Choose main folder containing Input", command=self.browse_button)
        button2.grid(columnspan=8, column=col)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(columnspan=8, column=col, sticky=E+W)

    def setup_teams(self):
        # ---- find participating teams by logos ----
        listofteams = []
        try:
            for team in os.listdir(self.path_main.get() + "Input/Teamlogos"):
                if team[-4:] == ".png":
                    listofteams.append(team[:-4])
        except FileNotFoundError:
            listofteams = []

        # ---- Find Jersey Colors -----
        jerseys = []
        try:
            for color in os.listdir(self.path_main.get() + "Input/Jerseycolors"):
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
            pic = Image.open(self.path_main.get() + "Input/Jerseycolors/" + color)
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
            pic = Image.open(self.path_main.get() + "Input/Jerseycolors/"+color)
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
                shutil.copyfile(self.path_main.get() + "Input/Cards/Blue.png", self.path_main.get() + "Output/card.png")
            except FileExistsError:
                os.remove(self.path_main.get() + "Output/card.png")
                shutil.copyfile(self.path_main.get() + "Input/Cards/Blue.png", self.path_main.get() + "Output/card.png")
        if self.chosen_card.get() == 2:
            try:
                shutil.copyfile(self.path_main.get() + "Input/Cards/Yellow.png", self.path_main.get() + "Output/card.png")
            except FileExistsError:
                os.remove(self.path_main.get() + "Output/card.png")
                shutil.copyfile(self.path_main.get() + "Input/Cards/Yellow.png", self.path_main.get() + "Output/card.png")
        if self.chosen_card.get() == 3:
            try:
                shutil.copyfile(self.path_main.get() + "Input/Cards/YellowRed.png", self.path_main.get() + "Output/card.png")
            except FileExistsError:
                os.remove(self.path_main.get() + "Output/card.png")
                shutil.copyfile(self.path_main.get() + "Input/Cards/YellowRed.png", self.path_main.get() + "Output/card.png")
        if self.chosen_card.get() == 3:
            try:
                shutil.copyfile(self.path_main.get() + "Input/Cards/YellowRed.png", self.path_main.get() + "Output/card.png")
            except FileExistsError:
                os.remove(self.path_main.get() + "Output/card.png")
                shutil.copyfile(self.path_main.get() + "Input/Cards/YellowRed.png", self.path_main.get() + "Output/card.png")
        if self.chosen_card.get() == 4:
            try:
                shutil.copyfile(self.path_main.get() + "Input/Cards/Red.png", self.path_main.get() + "Output/card.png")
            except FileExistsError:
                os.remove(self.path_main.get() + "Output/card.png")
                shutil.copyfile(self.path_main.get() + "Input/Cards/Red.png", self.path_main.get() + "Output/card.png")
        # ------------------------------
        # Move Playername and Number:
        # ------------------------------
        with open(self.path_main.get() + "Output/penalty_reason.txt", "w") as pen_file:
            pen_file.write(self.penalty_reason.get())
        if self.chosen_team_penalty.get() == 1:
            team = self.team_one
        else:
            team = self.team_two
        with open(self.path_main.get() + "Output/penalty_player.txt", "w") as pen_file:
            pen_file.write(self.player_num_penalty.get() + " " + team.roster[self.player_num_penalty.get()])
        with open(self.path_main.get() + "Output/penalty_team.txt", "w") as pen_file:
            pen_file.write(team.name.get())
        return None

    def destroy_penalty(self):
        for i in self.penalty_objects:
            i.destroy()

    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        filename = filedialog.askdirectory()
        self.path_main.set(filename+"/")
        try:
            os.listdir(self.path_main.get() + "Input")
        except FileNotFoundError:
            print("Input folder not found error. Please select a main folder containing your Input folder.\n" +
                  "Main Directory reset to ./")
            self.path_main.set("")
        if self.path_main.get()!="":
            self.setup_teams()
        print(filename)


root = Tk()
# root.resizable(False, False)

root.geometry("600x400")

my_gui = ScoreBoardGUI(root)
root.mainloop()
root.destroy()  # optional; see description below
