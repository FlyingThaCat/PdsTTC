from tkinter import Tk       # Import Tk from Tkinter
from config import BGWINDOW, TITLE     # Import title from config file
 
root = Tk()                  # Define Tk as root
root.title(TITLE)            # Set title for the window
root.resizable(False, False) # Set window cannot be resizable
root.configure(bg = BGWINDOW)# Set window background color