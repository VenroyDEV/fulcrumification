from ast import Lambda
import tkinter as tk
from ast import Lambda
import tkinter as tk

# Create the main window
root = tk.Tk()
root.withdraw()
# Create a variable to store the selected option
selected_option = "testest "

# Create the Radiobutton widgets
#Lamda function to change variables
def set_selected_option(option):
    selected_option = option
    return selected_option

def fulcrum_option():
    selected_option = "fulcrumification"
    return selected_option 

def custom_option():
    selected_option = "custom"
    return selected_option


option1_button = tk.Button(root, text="fulcrumification", command=lambda:fulcrum_option()) 
option2_button = tk.Button(root, text="custom", command=lambda:fulcrum_option()) 

# Create a button to accept the selected option
def accept_option(selected_option2):
    global selected_option
    print("Selected option:", selected_option2)

accept_button = tk.Button(root, text="Accept", command=lambda: accept_option(set_selected_option(tton)))

def menu(): # Pack the widgets
    option1_button.pack()
    root.deiconify() 
    accept_button.pack()
    return selected_option
