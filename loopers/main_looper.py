import sys
import os.path as fs

sys.path.append(fs.abspath("../utils"))

from looper import (Looper)
from lang_looper import *
from config_looper import *
from fs_utils import *
from config_parser import (PATH_TO_SUBLIME)


mainCommands = ["list", "configure", "choose", "help", "exit"]

MAIN_LOOPER_WELCOME = "Main welcome"
MAIN_LOOPER_GOODBYE = "Main goodbye"

class MainLooper(Looper):
  def __init__(self, config):
    super().__init__(MAIN_LOOPER_WELCOME, MAIN_LOOPER_GOODBYE, None)
    self.config = config

  def list(self):
    files = getFileNamesInDir(self.config[PATH_TO_SUBLIME] + "/Packages")
    for file in files:
      printGreen(file)

  def help(self):
    printGreen("Helping")

  def choose(self, lang):
    files = getFileNamesInDir(self.config[PATH_TO_SUBLIME] + "/Packages")
    if (lang not in files):
      printRed("Language \"" + lang + "\" isn't supported by this sublime version")
      return

    lang = LangLooper(lang, self.config, self)
    lang.runLooper()

  def configure(self):
    conf = ConfigLooper(self.config, self)
    conf.runLooper()

  def getName(self):
    return "Main"

  def exit(self):
    super().exit()   

