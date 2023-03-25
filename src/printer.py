# -*- coding: utf-8 -*-
from datetime import datetime


def console_print(level: str, message: str, end="\n"):
    time = datetime.now().strftime("%H:%M:%S")
    print(f'[{time}][{level}] {message}...', end=end)
