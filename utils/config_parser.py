import json
import os.path as fs

from colored_printer import *

CONFIG_FILE_NAME = r".config_file"
CONFIG_FILE_INDENT = 2

# config keys
PATH_TO_SUBLIME = "path_to_sublime"
ZIP_COMMAND = "zip_command"
UNZIP_COMMAND = "unzip_command"

def checkPathToSublime(path):
  if (not fs.exists(path)):
    printRed("Path : \"" + path + "\" doesn't exist!")
    return False

  if (not fs.isdir(path)):
    printRed("Path : \"" + path + "\" isn't a directory")
    return False

  return True

def initConfig():
  resetTextColor()

  config = {}
  while (True):
    if (PATH_TO_SUBLIME not in config):
      printGreen("Specify path to sublime text editor")
      path = input()
      if (not checkPathToSublime(path)):
        continue
      
      config[PATH_TO_SUBLIME] = fs.abspath(path)
      config[ZIP_COMMAND] = ["zip", "-r", "-m"]
      config[UNZIP_COMMAND] = ["unzip", "-d"]
      dumpConfig(config)
      break
    break

def getConfig():
  if (not fs.exists(CONFIG_FILE_NAME)):
    initConfig()

  handler = open(CONFIG_FILE_NAME, "r")
  obj = json.load(handler)
  handler.close()
  return obj

def dumpConfig(obj):
  handler = open(CONFIG_FILE_NAME, "w")
  json.dump(obj, fp = handler, indent = CONFIG_FILE_INDENT, sort_keys = True)
  handler.close()

def printConfig(obj):
  print(json.dumps(obj, indent = CONFIG_FILE_INDENT, sort_keys = True))
