from __future__ import unicode_literals
import youtube_dl
import os
from pydub import AudioSegment


def wav2mp3(src, dst):
    sound = AudioSegment.from_wav(src)
    sound.export(dst, format="mp3")


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    youtube_url = input("URL://")
    ydl.download([youtube_url])

for file in os.listdir():
    if ".wav" in file:
        src = file
        dst = file[:-3]+"mp3"
        wav2mp3(src, dst)
        os.remove(src)
