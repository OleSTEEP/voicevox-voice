# VoiceVOX-voice
Simple VoiceVOX sinetizer for fun (for Discord for example) on multiple languages

## Installing
* Install Python 3.10
* Install [VoiceVOX Server](https://voicevox.hiroshiba.jp/)
* Type `pip install -r requirement.txt` in your console in project folder

## Configuration
* Speed (Default = `1.75`) - Speed of voice
 * Pitch (Default = `0.0`) - Pitch of voice
* Intonation (Default = `1.0`) - Intonation of Voice
* Volume (Default = `3.0`) - Output volume
* StartSilence (Default = `0.05`) - Silence before words
* Stereo (Default = `True`) - Stereo support
* SamplingRate (Default = `48000`) - Audio device sampling rate
* RecognitionLanguage (Default = `ru`) - Language of your speech
* VoiceNumber (Default = `1`) - VoiceVOX voice number (characters)
* AudioDeviceName (Example = `CABLE Input (VB-Audio Virtual Cable), Windows WASAPI` (VB-Audio Virtual Cable)) - Name of your audio device and API (Can be obtained from an error in the console on invalid input)