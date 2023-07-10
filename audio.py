from genericpath import exists
from multiprocessing import process
import tkinter as tk
from tkinter import filedialog
import random
from turtle import position
import pydub
import select_file_tk 
from pydub import AudioSegment
from pydub.utils import make_chunks
import select_menu


# Load the MP3 file
mp3_file = AudioSegment.from_file(f"{(select_file_tk.select_file())}", format="mp3")
print("select a file to upload : ")

#menu selection
select_menu.menu()



#select custom clips
def custom_clips():
    customclip1 = AudioSegment.from_mp3(f"{select_file_tk.select_file_tk()}")
    return customclip1

# static audio clips (Fulcrumification)

clip1 = AudioSegment.from_mp3(r"D:\\github\\fulrcumifiaction\\fulcrumification\\mp3\\fulcrum.mp3")
clip2 = AudioSegment.from_mp3(r"D:\\github\\fulrcumifiaction\fulcrumification\\mp3\\codeword.mp3")

# Concatenate the audio clips
# concatenated_clips = clip1.append(clip2, crossfade=0)

# rms = "loudness" aka root means square (RMS) amplitude of the audio samples.


if select_menu.selected_option == "fulcrumization":
    final_audio = mp3_file.overlay(clip2, position= 20000)

if select_menu.selected_option == "customaudio":
    final_audio = mp3_file.overlay(custom_clips(), position= 20000)

# Overlay the audio clips onto the MP3 file
final_audio = mp3_file.overlay(clip2, position= 20000)

path = "D:\\github\\fulrcumifiaction\\fulcrumification\\exportstuff"
# Export the final audio file

export_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
# Export the final audio file to the selected path and filename
def process_video():
    final_audio.export(export_path, format="mp3")
