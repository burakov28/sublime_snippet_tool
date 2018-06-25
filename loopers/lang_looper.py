import os.path as fs
import os
import sys
import shutil
import subprocess

sys.path.append(fs.abspath("../utils"))

from looper import (Looper)
from colored_printer import *
from fs_utils import (getFileNamesInDir, unpackPackage, packPackage, removeTempDir)
from config_parser import (PATH_TO_SUBLIME)

LANG_LOOPER_WELCOME = "Lang welcome"
LANG_LOOPER_GOODBYE = "Lang goodbye"

langCommands = ["snippets", "remove", "add", "create", "modify", "exit"]

class LangLooper(Looper):
  def __init__(self, lang, config, parent):
    super().__init__(LANG_LOOPER_WELCOME, LANG_LOOPER_GOODBYE, parent)
    self.config = config
    self.lang = lang

  def getName(self):
    return "Choosed Language: \"" + self.lang + "\"" 

  def exit(self):
    super().exit()

  def snippets(self):
    unpackPackage(self.lang, self.config)

    snippets = getFileNamesInDir("temp/Snippets")
    for file in snippets:
      printGreen(file)

    removeTempDir()

  def remove(self, name):
      if (not unpackPackage(self.lang, self.config)):
        return

      snippetsNames = getFileNamesInDir("temp/Snippets")
      if (name not in snippetsNames):
        printRed("Snippet \"" + name + "\" for language \"" + self.lang + "\" doesn't exist")
        removeTempDir()
        return

      os.remove("temp/Snippets/" + name + ".sublime-snippet")
      packPackage(self.lang, self.config)

      removeTempDir()

  def add(self, file):
    if (not unpackPackage(self.lang, self.config)):
      return

    snippetsNames = getFileNamesInDir("temp/Snippets")
    if (fs.splitext(file)[0] in snippetsNames):
      printRed("Snippet \"" + name + "\" for language \"" + self.lang + "\" already exists")
      removeTempDir()
      return

    pathFrom = file
    pathTo = "temp/Snippets/" + fs.splitext(file)[0] + ".sublime-snippet"
    shutil.copyfile(pathFrom, pathTo)

    packPackage(self.lang, self.config)

    removeTempDir()

  def modify(self, name):
    if (not unpackPackage(self.lang, self.config)):
      return

    snippetsNames = getFileNamesInDir("temp/Snippets")
    if (name not in snippetsNames):
      printRed("Snippet \"" + name + "\" for language \"" + self.lang + "\" doesn't exist")
      removeTempDir()
      return

    snippet = "temp/Snippets/" + name + ".sublime-snippet"
    subprocess.call([self.config[PATH_TO_SUBLIME] + "/sublime_text", "-n", "-w", fs.abspath(snippet)])
    packPackage(self.lang, self.config);

    removeTempDir()

  def create(self, name):
    if (not unpackPackage(self.lang, self.config)):
      return

    snippetsNames = getFileNamesInDir("temp/Snippets")
    if (name in snippetsNames):
      printRed("Snippet \"" + name + "\" for language \"" + self.lang + "\" already exists")
      removeTempDir()
      return

    snippet = "temp/Snippets/" + name + ".sublime-snippet"
    subprocess.call([self.config[PATH_TO_SUBLIME] + "/sublime_text", "-n", "-w", fs.abspath(snippet)])
    packPackage(self.lang, self.config);

    removeTempDir()
