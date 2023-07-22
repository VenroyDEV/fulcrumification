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

clip1 = AudioSegment.from_mp3(r"D:\\github\\fulrcumifiaction\\fulcrumification\\mp3\\fulcrum.mp3")
clip2 = AudioSegment.from_mp3(r"D:\\github\\fulrcumifiaction\fulcrumification\\mp3\\codeword.mp3")

decible_of_clip1 = clip1.max_dBFS
print("the overlay clip is : ", decible_of_clip1, "loud")

difference_in_volume= decible_of_clip1 - decibel_of_random_timestamp
print("difference_in_volume = ", difference_in_volume)

if abs(decible_of_clip1) < abs(decibel_of_random_timestamp):
    print("the clip is ", difference_in_volume, "more loud than the selected video" )
    if difference_in_volume > 10:
        reborn_clip1= clip1.apply_gain(-5)
        print("video is too loud, I am reducing the sound gain by *not sure yet*")
else:
        print("the clip is ", difference_in_volume, "more quite than the selected video")
        if difference_in_volume < 10:
            reborn_clip1= clip1.apply_gain(+10) #I think I would have to do at least +25, if the video clip is -10, and we raise it +10, then it would be the same db as the selected mp3.
            print("video is more quite, I am raising the sound gain by *not sure yet*")


reborn_clip1= clip1.apply_gain(+15)



# Concatenate the audio clips
# concatenated_clips = clip1.append(clip2, crossfade=0)
# if select_menu.selected_option == "fulcrumization":
#     final_audio = mp3_file.overlay(clip2, position= 20000)

# if select_menu.selected_option == "customaudio":
#     final_audio = mp3_file.overlay(custom_clips(), position= 20000)

# rms = "loudness" aka root means square (RMS) amplitude of the audio samples.


# Overlay the audio clips onto the MP3 file
final_audio = mp3_file.overlay(reborn_clip1, position= random_duration)

path = "D:\\github\\fulrcumifiaction\\fulcrumification\\exportstuff"
# Export the final audio file

export_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
# Export the final audio file to the selected path and filename
def process_video():
    final_audio.export(export_path, format="mp3")
