import random
from turtle import position
import pydub
import select_file
from export import  *
from pydub import AudioSegment
from pydub.utils import make_chunks
import os

# Load the MP3 file
mp3_file = AudioSegment.from_file(f"{select_file()}", format="mp3")
print("select a file to upload : ")

# Load the audio clips
clip1 = AudioSegment.from_file("fulcrumification\mp3\fulcrum.mp3", format="mp3")
clip2 = AudioSegment.from_file("fulcrumification\mp3\codeword.mp3", format="mp3")

# Concatenate the audio clips
concatenated_clips = clip1.append(clip2, crossfade=0)

# Overlay the audio clips onto the MP3 file
final_audio = mp3_file.overlay(concatenated_clips, position=random)

# Export the final audio file
final_audio.export(f"{export_path}", format="mp3")