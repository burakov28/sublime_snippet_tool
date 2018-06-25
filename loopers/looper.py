import sys
import os.path as fs

sys.path.append(fs.abspath("../utils"))

from colored_printer import *

class Looper(object):
  def __init__(self, welcome, goodbye, parent):
    self.isEnd = False
    self.welcome = welcome
    self.goodbye = goodbye
    self.parent = parent

  def runLooper(self):
    printYellow(self.welcome)
    while(True):  
      cl = input().split()
      command = cl[0]
      args = cl[1:]
      
      method = None
      try:
        method = getattr(self, command)
      except AttributeError:
        printRed("Incorrect command: \"" + command + "\"")
        continue

      method(*args)
      print()
      if (self.isEnd):
        break

    printMagenta(self.goodbye)

  def exit(self):
    self.isEnd = True

  def getName(self):
    return "Undefined"

  def whereis(self):
    self.whereisInternal([])

  def whereisInternal(self, lst = []):
    if (self.parent == None):
      lst.append(self.getName())
      lst = list(reversed(lst))

      printGreen("Stack: ", end = "")
      for i in range(len(lst)):
        if (i != 0):
          printGreen(" -> ", end = "")
        printGreen(lst[i], end = "")
      printGreen()
    else:
      lst.append(self.getName())
      self.parent.whereisInternal(lst)

