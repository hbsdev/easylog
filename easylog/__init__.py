# -*- coding: utf-8 -*-
LOGGERS = [] # all loggers are registered here when create'd

import logging
LEVELS={
  "CRITICAL": logging.CRITICAL, #  50
  "ERROR": logging.ERROR, # 40
  "WARNING": logging.WARNING, # 30
  "INFO": logging.INFO, #  20
  "DEBUG": logging.DEBUG, # 10
  "NOTSET": logging.NOTSET, # 0
}

def create(
  logger_name,
  level='ERROR',
  path=None, # if given create a file logger
):
  import logging
  if path is None:
    # CONSOLE LOGGER:
    handler = logging.StreamHandler()
  else:
    # FILE LOGGER:
    # Create file handler if filenam given
    handler = logging.FileHandler(path)
  #handler.setLevel(LEVELS[level])
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)
  log = logging.getLogger(logger_name)
  log.setLevel(LEVELS[level])

  # add the handlers to the logger
  log.addHandler(handler)
  LOGGERS.append(logger_name)
  return log

def get(logger_name):
  if not logger_name in LOGGERS:
    return None
  import logging
  return logging.getLogger(logger_name)
  
