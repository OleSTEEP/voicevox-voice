#!/bin/python3
# -*- coding: utf-8 -*-

import os

from src import printer
from src import vosk_reconizer


def cache_create():
    try:
        os.mkdir("cache")
        print("OK")
    except FileExistsError:
        print("Exist")


if __name__ == "__main__":
    printer.console_print('INFO', 'Trying to create cache folder', '')
    cache_create()

    printer.console_print('INFO', 'Recognition started')
    vosk_reconizer.speech_recognition()




