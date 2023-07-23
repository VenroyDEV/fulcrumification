from tkinter import filedialog

from more_itertools import difference
import select_file_tk 
from pydub import AudioSegment
import random
# import select_menu

# Load the MP3 file
mp3_file = AudioSegment.from_file(f"{(select_file_tk.select_file())}", format="mp3")

mp3_file_duration_raw = mp3_file.duration_seconds
print("the video is : " ,mp3_file_duration_raw, "seconds long")
mp3_file_duration_in_milliseconds_inputable= int(mp3_file_duration_raw) * 1000
random_duration = random.randint(0, mp3_file_duration_in_milliseconds_inputable)
position_of_random_timestamp = random_duration / 1000
print("the clip happends at : ", abs(position_of_random_timestamp))

decibel_of_random_timestamp = mp3_file[random_duration].dBFS
print("the decibles of the random timestamp is : ",decibel_of_random_timestamp)




# menu selection
# while select_menu.menu() is None: 
#    select_menu.menu.wait_window()
#    if select_menu.menu() is not None: 
#       break 

    
#select custom clips
def custom_clips():
    customclip1 = AudioSegment.from_mp3(f"{select_file_tk.select_file_tk()}")
    return customclip1

# static audio clips (Fulcrumification)

clip1 = AudioSegment.from_mp3(r"D:\\github\\fulrcumifiaction\\fulcrumification\\mp3\\fulcrum.mp3")  # noqa: E501
clip2 = AudioSegment.from_mp3(r"D:\\github\\fulrcumifiaction\fulcrumification\\mp3\\codeword.mp3")  # noqa: E501

decible_of_clip1 = clip1.max_dBFS
print("the overlay clip is : ", decible_of_clip1, "loud")

difference_in_volume= decible_of_clip1 - decibel_of_random_timestamp
print("difference_in_volume = ", difference_in_volume)


def gain_decibel():
    global reborn_clip1
    if abs(decible_of_clip1) < abs(decibel_of_random_timestamp):
        print("the clip is ", difference_in_volume, "more loud than the selected video" )  # noqa: E501
        required_amount_for_gain = 15 - difference_in_volume                       #magic number = the decimal range you want to be +above the mp3, so that the clip stand out, you can make it dynamic at somepoint.
        reborn_clip1= clip1.apply_gain(required_amount_for_gain)
        print(f"added/subtracted {required_amount_for_gain} of decibel")  # noqa: E501
    else:
            print("the clip is ", difference_in_volume, "more quite than the selected video")  # noqa: E501
            required_amount_for_gain = 15 + abs(difference_in_volume)
            reborn_clip1= clip1.apply_gain(+required_amount_for_gain)
            print(f"clip is more quite, I am raising the sound gain by {required_amount_for_gain}")  # noqa: E501
    return reborn_clip1





# Concatenate the audio clips
# concatenated_clips = clip1.append(clip2, crossfade=0)
# if select_menu.selected_option == "fulcrumization":
#     final_audio = mp3_file.overlay(clip2, position= 20000)

# if select_menu.selected_option == "customaudio":
#     final_audio = mp3_file.overlay(custom_clips(), position= 20000)

# rms = "loudness" aka root means square (RMS) amplitude of the audio samples.


# Overlay the audio clips onto the MP3 file
final_audio = mp3_file.overlay(gain_decibel(), position= random_duration)

path = "D:\\github\\fulrcumifiaction\\fulcrumification\\exportstuff"
# Export the final audio file

export_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])  # noqa: E501
# Export the final audio file to the selected path and filename
def process_video():
    final_audio.export(export_path, format="mp3")
