import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a variable to store the selected option
selected_option = tk.StringVar()

# Create the Radiobutton widgets
option2 = tk.Radiobutton(root, text="fulcrumification", variable=selected_option, value="fulcrumification")
option3 = tk.Radiobutton(root, text="Custom Audio", variable=selected_option, value="customaudio")

# Create a button to accept the selected option
def accept_option():
    print("Selected option:", selected_option.get())

accept_button = tk.Button(root, text="Accept", command=accept_option)

def menu(): # Pack the widgets
    option2.pack()
    option3.pack()
    accept_button.pack()

# Start the main loop
root.mainloop()
