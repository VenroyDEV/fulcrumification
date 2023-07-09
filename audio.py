from genericpath import exists
import random
from turtle import position
import pydub
import select_file_tk 
# from export import  *
from pydub import AudioSegment
from pydub.utils import make_chunks
import os

# Load the MP3 file
mp3_file = AudioSegment.from_file(f"{(select_file_tk.select_file())}", format="mp3")
print("select a file to upload : ")

# Load the audio clips
clip1 = AudioSegment.from_file(r"D:\\github\\fulrcumifiaction\\fulcrumification\\mp3\\codeword.mp3", format="mp3")
clip2 = AudioSegment.from_file(r"D:\\github\\fulrcumifiaction\fulcrumification\\mp3\\codeword.mp3", format="mp3")

# Concatenate the audio clips
concatenated_clips = clip1.append(clip2, crossfade=0)

# Overlay the audio clips onto the MP3 file
final_audio = mp3_file.overlay(concatenated_clips)

# Export the final audio file
if not os.path.exists("D:\\github\\fulrcumifiaction\\fulcrumification\\exportstuff"): 
    os.mkdir("D:\\github\\fulrcumifiaction\\fulcrumification\\exportstuff")
    path = r"D:\\github\\fulrcumifiaction\\fulcrumification\\exportstuff"
    assert os.path.isdir(path), "path doesnt exist"
else:
     final_audio.export("exportstuff", format="mp3")
     print("technically everything went fine")
     with open("test", "w") as f:
        f.write("test")
        print("successful")
        pass