from mutagen.easyid3 import EasyID3
from glob import glob

from pydub.playback import play
from pydub import AudioSegment

import random
import json
import re

with open("music/data.json") as file:
    data = json.load(file)
print(data)
music = glob("music/*.mp3")
print(music)
for filename in music:
    song = re.search(r"(?<=music\\)[A-Za-z0-9' ]+(?=\.mp3)",filename).group(0)
    print(song)
    if song in data.keys():
        audio = EasyID3()
        audio["title"] = data[song]["title"]
        audio["artist"] = data[song]["artist"]
        audio["date"] = str(data[song]["year"])
        print(audio)
        audio.save(filename)
    
song = random.choice(music)
print(song)
song = AudioSegment.from_mp3(song)
segment = song[:5000].fade_in(1000).fade_out(1000)
play(segment)
play(segment.reverse())