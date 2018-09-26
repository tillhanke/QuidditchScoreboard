from tkinter import *


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

