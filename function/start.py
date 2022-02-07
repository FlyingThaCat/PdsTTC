from tkinter import Button, DISABLED                                                    # Import Tkinter Module To Make Button and Disabled Button
from function.init import root                                                          # Import Tkinter Initiater
from function.button import *                                                           # Import All button module
import function.check as check                                                          # Import Check module
from config import DISABLEDFGCOLOR, HEIGHT, WIDTH, FONT, RELIEF, BGCOLOR, PADX, PADY    # Import configuration from config.py

#If set to true player 1 move first otherwise the player 2 playing first 
CLICK = True

#Save Progress Of Player
COUNT = 0

# Start Function
def start():  
    # Row AND Column Configuration
    ## EX : top left button is 0,0
    """
    0 1 2 3
    1
    2
    3
    """
    # Create button with Initiater and config and call push command to mark progress and set disabled color button as config
    ## s1 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b1, command = lambda: push(1), disabledforeground = DISABLEDFGCOLOR)

    # Show the button from cords and setting padding from config
    ## s1.grid(row = 0, column = 0, padx = PADX, pady = PADY)

    s1 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b1, command = lambda: push(1), disabledforeground = DISABLEDFGCOLOR)
    s1.grid(row = 0, column = 0, padx = PADX, pady = PADY)
    s2 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b2, command = lambda: push(2), disabledforeground = DISABLEDFGCOLOR)
    s2.grid(row = 0, column = 1, padx = PADX, pady = PADY)
    s3 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b3, command = lambda: push(3), disabledforeground = DISABLEDFGCOLOR)
    s3.grid(row = 0, column = 2, padx = PADX, pady = PADY)
    s4 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b4, command = lambda: push(4), disabledforeground = DISABLEDFGCOLOR)
    s4.grid(row = 0, column = 3, padx = PADX, pady = PADY)
    s5 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b5, command = lambda: push(5), disabledforeground = DISABLEDFGCOLOR)
    s5.grid(row = 1, column = 0, padx = PADX, pady = PADY)
    s6 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b6, command = lambda: push(6), disabledforeground = DISABLEDFGCOLOR)
    s6.grid(row = 1, column = 1, padx = PADX, pady = PADY)
    s7 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b7, command = lambda: push(7), disabledforeground = DISABLEDFGCOLOR)
    s7.grid(row = 1, column = 2, padx = PADX, pady = PADY)
    s8 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b8, command = lambda: push(8), disabledforeground = DISABLEDFGCOLOR)
    s8.grid(row = 1, column = 3, padx = PADX, pady = PADY)
    s9 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b9, command = lambda: push(9), disabledforeground = DISABLEDFGCOLOR)
    s9.grid(row = 2, column = 0, padx = PADX, pady = PADY)
    s10 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b10, command = lambda: push(10), disabledforeground = DISABLEDFGCOLOR)
    s10.grid(row = 2, column = 1, padx = PADX, pady = PADY)
    s11 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b11, command = lambda: push(11), disabledforeground = DISABLEDFGCOLOR)
    s11.grid(row = 2, column = 2, padx = PADX, pady = PADY)
    s12 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b12, command = lambda: push(12), disabledforeground = DISABLEDFGCOLOR)
    s12.grid(row = 2, column = 3, padx = PADX, pady = PADY)
    s13 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b13, command = lambda: push(13), disabledforeground = DISABLEDFGCOLOR)
    s13.grid(row = 3, column = 0, padx = PADX, pady = PADY)
    s14 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b14, command = lambda: push(14), disabledforeground = DISABLEDFGCOLOR)
    s14.grid(row = 3, column = 1, padx = PADX, pady = PADY)
    s15 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b15, command = lambda: push(15), disabledforeground = DISABLEDFGCOLOR)
    s15.grid(row = 3, column = 2, padx = PADX, pady = PADY)
    s16 = Button(root, height = HEIGHT, width = WIDTH, font = FONT, relief = RELIEF, bg = BGCOLOR, textvariable = b16, command = lambda: push(16), disabledforeground = DISABLEDFGCOLOR)
    s16.grid(row = 3, column = 3, padx = PADX, pady = PADY)

    # Function to mark progress
    def push(n):
            global CLICK, COUNT # Set click and count value as global
            if CLICK == True:
                if n == 1:                  # If BTN N is clicked do
                    b1.set("1")             # Set value of button to 1
                    s1['state'] = DISABLED  # Set button to be 1 time clicked only
                elif n == 2:
                    b2.set("1")
                    s2['state'] = DISABLED
                elif n == 3:
                    b3.set("1")
                    s3['state'] = DISABLED
                elif n == 4:
                    b4.set("1")
                    s4['state'] = DISABLED
                elif n == 5:
                    b5.set("1")
                    s5['state'] = DISABLED
                elif n == 6:
                    b6.set("1")
                    s6['state'] = DISABLED
                elif n == 7:
                    b7.set("1")
                    s7['state'] = DISABLED
                elif n == 8:
                    b8.set("1")
                    s8['state'] = DISABLED
                elif n == 9:
                    b9.set("1")
                    s9['state'] = DISABLED
                elif n == 10:
                    b10.set("1")
                    s10['state'] = DISABLED
                elif n == 11:
                    b11.set("1")
                    s11['state'] = DISABLED
                elif n == 12:
                    b12.set("1")
                    s12['state'] = DISABLED
                elif n == 13:
                    b13.set("1")
                    s13['state'] = DISABLED
                elif n == 14:
                    b14.set("1")
                    s14['state'] = DISABLED
                elif n == 15:
                    b15.set("1")
                    s15['state'] = DISABLED
                elif n == 16:
                    b16.set("1")
                    s16['state'] = DISABLED
                COUNT += 1         # Add Count as button pressed to find progress limit
                CLICK = False      # Set to false so player 2 / 0 can play the game
                check.wincheck()   # Calling Wincheck Function

            else: # If Click is False
                if n == 1:                  # If BTN N is clicked do
                    b1.set("0")             # Set value of button to 1
                    s1['state'] = DISABLED  # Set button to be 1 time clicked only
                elif n == 2:
                    b2.set("0")
                    s2['state'] = DISABLED
                elif n == 3:
                    b3.set("0")
                    s3['state'] = DISABLED
                elif n == 4:
                    b4.set("0")
                    s4['state'] = DISABLED
                elif n == 5:
                    b5.set("0")
                    s5['state'] = DISABLED
                elif n == 6:
                    b6.set("0")
                    s6['state'] = DISABLED
                elif n == 7:
                    b7.set("0")
                    s7['state'] = DISABLED
                elif n == 8:
                    b8.set("0")
                    s8['state'] = DISABLED
                elif n == 9:
                    b9.set("0")
                    s9['state'] = DISABLED
                elif n == 10:
                    b10.set("0")
                    s10['state'] = DISABLED
                elif n == 11:
                    b11.set("0")
                    s11['state'] = DISABLED
                elif n == 12:
                    b12.set("0")
                    s12['state'] = DISABLED
                elif n == 13:
                    b13.set("0")
                    s13['state'] = DISABLED
                elif n == 14:
                    b14.set("0")
                    s14['state'] = DISABLED
                elif n == 15:
                    b15.set("0")
                    s15['state'] = DISABLED
                elif n == 16:
                    b16.set("0")
                    s16['state'] = DISABLED
                COUNT += 1         # Add Count as button pressed to find progress limit
                CLICK = True       # Set to false so player 1 / 1 can continue the flow
                check.wincheck()   # Calling Wincheck Function