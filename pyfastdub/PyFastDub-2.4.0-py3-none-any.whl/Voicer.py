import hashlib
import os.path

import pyttsx3

from FastDub.Audio import AudioSegment


class UnknownVoice(Exception):
    __slots__ = ()
    pass


_voices = pyttsx3.init().proxy.getProperty('voices')
VOICES_NAMES = {i.name.casefold(): i for i in _voices}
VOICES_ID = {i.id: i for i in _voices}
del _voices


class Voicer:
    __slots__ = ('engine', "cache_dir")

    def __init__(self, cache_dir: str = None):
        self.engine = pyttsx3.init()
        self.cache_dir = cache_dir or os.path.join(os.path.dirname(__file__), '_cached_texts')
        if not os.path.isdir(self.cache_dir):
            os.makedirs(self.cache_dir)

    def cleanup(self):
        for file in os.listdir(self.cache_dir):
            os.remove(os.path.join(self.cache_dir, file))

    def set_voice(self, voice: str):
        voice_name = voice.casefold()
        voice_property = self.engine.proxy.getProperty('voice')
        voice = VOICES_NAMES.get(voice_name)
        if not voice:
            raise UnknownVoice(f'{voice_name} not in {str(tuple(VOICES_NAMES.keys()))}')
        if VOICES_ID.get(voice_property).name.casefold() != voice_name:
            self.engine.proxy.setProperty('voice', voice.id)

    def voice(self, text: str, change_voice: bool = True) -> AudioSegment:
        text = text.strip()
        if not text:
            return AudioSegment.silent(0)

        if change_voice and (lines := text.splitlines())[0].startswith('!:'):
            self.set_voice(lines[0][2:])
            text = '\n'.join(lines[1:])

        cached = os.path.join(self.cache_dir, hashlib.md5(
            f"{text}{self.engine.proxy.getProperty('voice')}".encode('UTF-8')).hexdigest() + '.wav')
        if not os.path.isfile(cached):
            self.engine.proxy.save_to_file(text, cached, None)
            self.engine.runAndWait()
        return AudioSegment.from_file(cached, format='wav')
