#File: catchaudiolength.py for archimob files

from glob import glob
import wave
import contextlib
import datetime
import time

sec = 0
z = 0
try:
    for entry in glob('./merged/*.wav'):
        with contextlib.closing(wave.open(entry,'rb')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            z = z + 1
            duration = frames / float(rate)
            print(z, ' file duration is: ', duration)
            sec = sec + duration
except EOFError:
    data = list()  # or whatever you want

length_of_audio = str(datetime.timedelta(seconds=sec))

print('Audio Files from Archimob')
print('Total Seconds: ', sec)
print('Length of Audio: ', length_of_audio)

#Sources: (adapted from)
## Title: Get .wav file length or duration
## URL: https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration
## Last accessed: 05/07/2019
