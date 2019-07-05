import sys
from moviepy.editor import *
from glob import glob

#Loop through every file in folder audio that ends with .wmv
for entry in glob('./audio/*.mp4'):
    video = VideoFileClip(entry)
    #extract audio from video
    audio = video.audio
    #write audio file with specified ending .wav
    audio.write_audiofile(entry + '.wav')

#Sources: (adapted from)
## Title: MoviePy
## URL: https://zulko.github.io/moviepy/
## Last accessed: 05/07/2019

## Title: How to extract audio from the video with python
## URL: https://medium.com/@steadylearner/how-to-extract-audio-from-the-video-with-python-aea325f434b6
## Last accessed: 19/06/2019
