import os.path as fs
import sys

sys.path.append(fs.abspath("../utils"))

from config_parser import *
from looper import (Looper)

CONFIG_LOOPER_WELCOME = "Config welcome"
CONFIG_LOOPER_GOODBYE = "Config goodbye"

configCommand = ["mainpath", "exit", "setzip", "setunzip"]

class ConfigLooper(Looper):
  def __init__(self, config, parent):
    super().__init__(CONFIG_LOOPER_WELCOME, CONFIG_LOOPER_GOODBYE, parent)
    self.config = config

  def exit(self):
    super().exit()

  def mainpath(self, path):
    self.config[PATH_TO_SUBLIME] = path
    dumpConfig(self.config)

  def setzip(self, *args):
    self.config[ZIP_COMMAND] = args
    dumpConfig(self.config)

  def getzip(self):
    printGreen("Zip command: \"" + " ".join(self.config[ZIP_COMMAND]) + " [archive] [list of files to pack]\"")

  def setunzip(self, *args):
    self.config[UNZIP_COMMAND] = args
    dumpConfig(self.config)

  def getunzip(self):
    printGreen("Unzip command: \"" + " ".join(self.config[UNZIP_COMMAND]) + " [path to put extracted files] [archive]\"")

  def help(self):
    printGreen("Configure helping")

  def getName(self):
    return "Configuring"
