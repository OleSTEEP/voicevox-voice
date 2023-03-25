# -*- coding: utf-8 -*-
import sounddevice as sd
import numpy as np
import configparser
import httpx

config = configparser.ConfigParser()
config.read("config.ini")


async def play_sound(string, voice: int):
    async with httpx.AsyncClient() as http_client:
        query_params = {'speaker': voice, 'text': string}
        response = await http_client.post('http://localhost:50021/audio_query', params=query_params)
        query_json = response.json()
        query_json['speedScale'] = float(config['VOICEVOX']['Speed'])
        query_json['pitchScale'] = float(config['VOICEVOX']['Pitch'])
        query_json['intonationScale'] = float(config['VOICEVOX']['Intonation'])
        query_json['volumeScale'] = float(config['VOICEVOX']['Volume'])
        query_json['prePhonemeLength'] = float(config['VOICEVOX']['StartSilence'])
        query_json['postPhonemeLength'] = float(config['VOICEVOX']['StartSilence'])
        query_json['outputStereo'] = bool(config['VOICEVOX']['Stereo'])
        query_json['outputSamplingRate'] = int(config['VOICEVOX']['SamplingRate'])

        headers = {'Content-Type': 'application/json'}
        synth_params = {'speaker': voice}
        response = await http_client.post('http://localhost:50021/synthesis', headers=headers, params=synth_params,
                                          json=query_json)
        audio_data = response.content

        numpy_audio = np.frombuffer(audio_data, dtype=np.int32)

        sd.default.device = config['VOICEVOX']['AudioDeviceName']
        sd.play(numpy_audio, int(config['VOICEVOX']['SamplingRate']))
