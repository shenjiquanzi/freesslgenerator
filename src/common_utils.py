#coding=utf8
import uuid

import sys, os
import uuid
# from Crypto.Cipher import AES
import logging
import datetime
import subprocess

import re
import threading
from threading import Timer

__strCurrentDir__ = os.path.abspath(os.path.dirname(__file__))
__strModuleDir__ = os.path.dirname(__strCurrentDir__)

def InitLogger(logFile, logLevel):
    logger = logging.getLogger()
    fileHandler = logging.FileHandler(logFile)
    formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(lineno)s \
      %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logLevel)
    return logger

logger = InitLogger(
    f"%s/freessl-%s_%s_%s.log"
    % (
        __strModuleDir__,
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
    ),
    logging.INFO,
)


class Cmd:
    def __init__(self, cmd, isPrint=False):
        self.cmd = cmd
        self.isPrint = isPrint

    def execute_cmd(self):
        # if self.isPrint:
        #     ColorPrint("CMD: %s" % self.cmd)
        code, output = subprocess.getstatusoutput(self.cmd)
        if code != 0:
            logger.error("Excute:%s code= %s  \n output= %s" % (self.cmd, code, output))
            return False, output
        else:
            logger.info("Excute:%s success \n output= %s" % (self.cmd, output))
            return True, output

class RepeatingTimer(Timer): 
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


def gen_uuid():
    s_uuid=str(uuid.uuid4())
    l_uuid=s_uuid.split('-')
    s_uuid=''.join(l_uuid)

    return s_uuid


if __name__ == '__main__':
   
   '''
   email = 'dsdssdsddsdsds'
   print(IsValidEmail(email)) 
   print(IsValidEmail('wwewewewe@163.com'))   
   '''
