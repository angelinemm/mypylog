#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from enum import IntEnum
import sys
from datetime import datetime

CALLS = 10000


class Level(IntEnum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

    def __str__(self):
        return {
            Level.DEBUG: 'DEBUG',
            Level.INFO: 'INFO',
            Level.WARNING: 'WARNING',
            Level.ERROR: 'ERROR',
        }[self]


class Logger(object):
    def __init__(self, logfile=None, log_level=Level.DEBUG, buffer_size=None):
        if logfile:
            self._log = open(logfile, 'a', buffer_size)
        else:
            self._log = sys.stdout
        self._loglevel = log_level

    def debug(self, message):
        if(self._loglevel <= Level.DEBUG):
            self._write(message, Level.DEBUG)

    def info(self, message):
        if(self._loglevel <= Level.INFO):
            self._write(message, Level.INFO)

    def warning(self, message):
        if(self._loglevel <= Level.WARNING):
            self._write(message, Level.WARNING)

    def error(self, message):
        if(self._loglevel <= Level.ERROR):
            self._write(message, Level.ERROR)

    def _write(self, message, level):
        self._log.write("[%s]%s: %s\n" % (datetime.now(), level, message,))

    def timed_call(self, func, args):
        before = datetime.now()
        results = func(*args)
        self.info(
            "Called function %s in %sμs" % (func.__name__, (datetime.now() - before).microseconds)
        )
        return results

    def mean_time(self, func, args):
        time = 0
        for i in range(1, CALLS):
            before = datetime.now()
            func(*args)
            time += (datetime.now() - before).microseconds
        time /= CALLS
        self.info("Function %s called in %sμs on average" % (func.__name__, time))
        return time
