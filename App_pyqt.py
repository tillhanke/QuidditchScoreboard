from PyQt5.QtWidgets import QApplication
import os
import csv
import threading
import sys
import subprocess
from MainWindow import MainWindow


if __name__ == "__main__":
    x = subprocess.check_output("node -v", shell=True).decode('utf-8').rstrip()
    if(x != "v21.6.0"):
        print("Please use node version v21.6.0 (nvm install 21.6.0).")
        exit()
    if(os.path.isdir("./quadballlive_api/node_modules") == False):
        print("Installing packages for Timekeeper connection")
        os.chdir("./quadballlive_api")
        os.system("npm install")
        os.chdir("..")

    open("Output/LeftPath.txt", "w").write("")
    open("Output/RightPath.txt", "w").write("")
    open("Output/ScoreLeft.txt", "w").write("0")
    open("Output/ScoreRight.txt", "w").write("0")
    open("Output/Gametime.txt", "w").write("00:00")
    open("Output/Gametime.csv", "w").write("Gametime\n00:00")
    open("Output/Gameinfo.csv", "w").write("Team Left,Score Left,Team Right,Score Right,Overtime Setscore\nTeam A,0,Team B,0,-")
    open("Output/OvertimeSetscore.txt", "w").write("-")
    open("quadballlive_api/new_penalty.txt", "w").write("0")
    open("quadballlive_api/gameidstonames.txt", "w").write("0")
    open("quadballlive_api/gameids_scorecrawl.txt", "w").write("0")
    with open("Output/Penalty.csv","w") as file:
        fieldnames = ["Name", "Team", "Reason"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n", delimiter=",")
        writer.writeheader()
    open("Output/ScoreCrawl.csv", "w").write("Scorecrawl\n")

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.settings_w.show()
    with open("qsb.stylesheet", "r") as fh:
        app.setStyleSheet(fh.read())
    updater = threading.Thread(target=w.update)
    updater.start()
    app.setQuitOnLastWindowClosed(True)
    sys.exit(app.exec_())