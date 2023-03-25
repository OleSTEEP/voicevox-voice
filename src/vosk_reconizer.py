# -*- coding: utf-8 -*-
import json
import queue
import romkan
import asyncio
import configparser
import sounddevice as sd

from src import tts
from src import printer
from transliterate import translit
from vosk import Model, KaldiRecognizer

config = configparser.ConfigParser()
config.read("config.ini")

q = queue.Queue()
samplerate = int(config['VOICEVOX']['SamplingRate'])
language = config['VOICEVOX']['RecognitionLanguage']
voice = int(config['VOICEVOX']['VoiceNumber'])


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def speech_recognition():
    model = Model(lang=language)

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype="int16", channels=1, callback=callback):
        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                printer.console_print('INFO', 'Playing audio')
                text = json.loads(rec.Result())
                printer.console_print('TEXT', text["text"])
                romanian = translit(text["text"], language, reversed=True)
                asyncio.run(tts.play_sound(romkan.to_katakana(romanian), voice))


if __name__ == "__main__":
    print(speech_recognition())
