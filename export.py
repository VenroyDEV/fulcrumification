import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window (if one doesn't already exist)
root = tk.Tk()

# Hide the root window
root.withdraw()

# Prompt the user to select the export path and filename
export_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])

# Export the final audio file to the selected path and filename
final_audio.export(export_path, format="mp3")