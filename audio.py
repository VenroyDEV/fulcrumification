from tkinter import filedialog

from more_itertools import difference
import select_file_tk 
from pydub import AudioSegment
import random
# import select_menu
from tkinter import filedialog
from pydub import AudioSegment
import random

# Load the MP3 file
mp3_file = AudioSegment.from_file(f"{(select_file_tk.select_file())}", format="mp3")
mp3_file_duration_raw = mp3_file.duration_seconds

print("the video is:", mp3_file_duration_raw, "seconds long")

# Define the clips
clip1 = AudioSegment.from_mp3(r"D:/github/fulrcumifiaction/fulcrumification/mp3/fulcrum.mp3")
clip2 = AudioSegment.from_mp3(r"D:/github/fulrcumifiaction/fulcrumification/mp3/codeword.mp3")
clips = {"fulcrum": clip1, "codeword": clip2}

store_clip_decision = input(f"here are all the current clips you can select \n {clips.keys()} \n enter one of the options: ").lower()

while store_clip_decision not in clips.keys():
    print("your Input does not exist, try again!")
    store_clip_decision = input(f"here are all the current clips you can select \n {clips.keys()} \n enter one of the options: ").lower()

if store_clip_decision in clips.keys():
    producertag_iterations = int(input("give me the number of producer tags in the mp3: "))

# Timestamping works only in milliseconds, therefore we add *1000
mp3_file_duration_in_milliseconds_inputable = int(mp3_file_duration_raw * 1000)

# Generate a list of random positions for producer tags
list_of_positions_from_random_duration = []
for i in range(producertag_iterations):
    random_duration_iteration = random.randint(0, mp3_file_duration_in_milliseconds_inputable)
    list_of_positions_from_random_duration.append(random_duration_iteration)

# Overlay the audio clips onto the MP3 file
for position in list_of_positions_from_random_duration:
    selected_clip = clips.get(store_clip_decision)
    decibel_of_clip1 = selected_clip.max_dBFS
    decibel_of_random_timestamp = mp3_file[position].dBFS

    difference_in_volume = decibel_of_clip1 - decibel_of_random_timestamp
    print("difference_in_volume =", difference_in_volume)

    def gain_decibel():
        global reborn_clip1
        if abs(decibel_of_clip1) < abs(decibel_of_random_timestamp):
            print("the clip is", difference_in_volume, "more loud than the selected video")
            required_amount_for_gain = 15 - difference_in_volume
            reborn_clip1 = selected_clip.apply_gain(required_amount_for_gain)
            print(f"added/subtracted {required_amount_for_gain} of decibels")
        else:
            print("the clip is", difference_in_volume, "more quiet than the selected video")
            required_amount_for_gain = 15 + abs(difference_in_volume)
            reborn_clip1 = selected_clip.apply_gain(required_amount_for_gain)
            print(f"clip is more quiet, I am raising the sound gain by {required_amount_for_gain}")
        return reborn_clip1

    # Overlay the selected clip with gain applied at the given position
    mp3_file = mp3_file.overlay(gain_decibel(), position=position)

# Export the final audio file
export_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])

# Export the final audio file to the selected path and filename
def process_video():
    mp3_file.export(export_path, format="mp3")
