#!/bin/python3
# -*- coding: utf-8 -*-

from src import printer
from src import vosk_reconizer


if __name__ == "__main__":
    printer.console_print('INFO', 'Recognition started')
    vosk_reconizer.speech_recognition()
