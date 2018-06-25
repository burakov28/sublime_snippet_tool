import subprocess
import os
import os.path as fs
import sys
import shutil

from config_parser import (PATH_TO_SUBLIME)

def getFileNamesInDir(path):
  files = list(map(lambda s: fs.splitext(s)[0], filter(lambda s: fs.isfile(path + "/" + s), os.listdir(path))))
  files.sort()
  return files 

def unpackPackage(lang, config):
  pathFrom = config[PATH_TO_SUBLIME] + "/Packages/" + lang + ".sublime-package"
  pathTo = "temp"
  if (not fs.exists(pathTo)):
    os.makedirs(pathTo)

  pathTo += "/" + lang + ".zip"
  shutil.copyfile(pathFrom, pathTo)
  command = ["unzip", fs.abspath(pathTo), "-d", fs.abspath("temp")]
  FNULL = open(os.devnull, "w")
  retCode = subprocess.call(command, stdout = FNULL, stderr = subprocess.STDOUT)
  FNULL.close()
  return True

def packPackage(lang, config):
  os.remove("temp/" + lang + ".zip")
  FNULL = open(os.devnull, "w")
  command = ["zip", "-r", "-m", lang + "Temp.zip"] + list(map(lambda s: fs.basename(s), os.listdir("temp")))
  retCode = subprocess.call(command, stdout = FNULL, stderr = subprocess.STDOUT, cwd = "temp")
  pathFrom = "temp/" + lang + "Temp.zip"
  pathTo = config[PATH_TO_SUBLIME] + "/Packages/" + lang + ".sublime-package"
  shutil.copyfile(pathFrom, pathTo)

def removeTempDir():
  shutil.rmtree("temp", ignore_errors = True)
