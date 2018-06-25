import os
import os.path as fs
import sys

sys.path.append(fs.abspath("utils"))
sys.path.append(fs.abspath("loopers"))

from config_parser import *
from colored_printer import (printRed, printGreen, resetTextColor)
from main_looper import (MainLooper)


config = getConfig()

mainLooper = MainLooper(config)
mainLooper.runLooper()
