from looper import (Looper)

CONFIG_LOOPER_WELCOME = "Config welcome"
CONFIG_LOOPER_GOODBYE = "Config goodbye"

class ConfigLooper(Looper):
  def __init__(self, config, parent):
    super().__init__(CONFIG_LOOPER_WELCOME, CONFIG_LOOPER_GOODBYE, parent)
    self.config = config

  def exit(self):
    super().exit()

  def getName(self):
    return "Configuring"
