from tkinter import filedialog
from tkinter import *

root = Tk()

def select_file():
    file_path = filedialog.askopenfilename(title="Select file", filetypes=[("Video files", "*.mp4")])
    if file_path:
        print(f"Selected file: {file_path}")
        # do something with the file path here

button = Button(root, text="Select file", command=select_file)
button.pack()

root.mainloop()