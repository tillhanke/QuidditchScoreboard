from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from scores_ui import Ui_main
from timekeeper_ui import Ui_Timekeeper
from setup_ui import Ui_settings
from penalty_ui import Ui_Penalty
#from snitch_catch_ui import Ui_SnitchCatch
from sureBro_ui import Ui_sureBro
import os
import io
import codecs
import shutil
#import websocket
import time
import urllib.request
import json
import math
import threading
import sys
import subprocess
from MainWindow import MainWindow


'''
Check connections in main_ui first!

self.add10_left.clicked.connect(lambda x: main.add_left(10))
self.sub10_left.clicked.connect(lambda x: main.add_left(-10))
self.add10_right.clicked.connect(lambda x: main.add_right(10))
self.sub10_right.clicked.connect(lambda x: main.add_right(-10))

'''


if __name__ == "__main__":
    if(os.path.isdir("./quidditchlive_api/node_modules") == False):
        print("Installing packages for Timekeeper connection")
        os.chdir("./quidditchlive_api")
        os.system("npm install")
        os.chdir("..")
    app = QApplication(sys.argv)
    w = MainWindow()
    
    with open("qsb.stylesheet", "r") as fh:
        app.setStyleSheet(fh.read())
    #w.showMaximized()
    updater = threading.Thread(target=w.update)
    updater.start()
    sys.exit(app.exec_())
