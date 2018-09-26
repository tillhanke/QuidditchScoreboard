from tkinter import *


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

