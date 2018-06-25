import colorama
from colorama import (Style, Fore, Back)

wasInited = False

def ensureInit():
  global wasInited
  if (not wasInited):
    colorama.init()
    wasInited = True

def resetColor():
  ensureInit()
  print(Style.RESET_ALL, end = "")

def resetTextColor():
  ensureInit()

  resetColor()
  print(Style.BRIGHT + Fore.WHITE, end = "")

def internalPrint(str, color, tail = "\n"):
    ensureInit()

    resetColor()
    print(color + str, end = tail)
    resetTextColor()


def printGreen(str = "", end = "\n"):
  internalPrint(str, Fore.GREEN, end)

def printMagenta(str = "", end = "\n"):
  internalPrint(str, Fore.MAGENTA, end)

def printRed(str = "", end = "\n"):
  internalPrint(str, Fore.RED, end)

def printYellow(str = "", end = "\n"):
  internalPrint(str, Fore.YELLOW, end)

