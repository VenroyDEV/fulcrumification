from pydub import AudioSegment
from tkinter import filedialog
import tkinter

root = tkinter.Tk()
root.withdraw()

def select_file():
    root.filename = filedialog.askopenfilename(title="Select file", 
    filetypes=(("MPEG-1 Audio Layer 3", "*.mp3"), ("All files", "*.*")))

    if root.filename :
        print(f"the path is : {root.filename}")
    return root.filename

def get_file_info(input):
   mp3_file = AudioSegment.from_file(input, format="mp3")
   song_length = len(mp3_file)
   return song_length 


