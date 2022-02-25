from function.clear import clear            # Import Clear Function
from function.msg import win_msg, tie_msg   # Import Message Function
import function.start as start              # Import Start Function
from function.button import b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16 # Import All button module
from function.cross import *

def wincheck():
    print(start.COUNT) # Debug for Count Tracker
    """
    |-----------|
    |1 |2 |3 |4 |
    |5 |6 |7 |8 |
    |9 |10|11|12|
    |13|14|15|16|
    |-----------|
    """

    if(
        # Check the value of button with horizontal, vertical, diagonal possibility for player 1
        # Horizontal
        b1.get() == '1' and b2.get() == '1' and b3.get() == '1' and b4.get() == '1' or
        b5.get() == '1' and b6.get() == '1' and b7.get() == '1' and b8.get() == '1' or
        b9.get() == '1' and b10.get() == '1' and b11.get() == '1' and b12.get() == '1' or
        b13.get() == '1' and b14.get() == '1' and b15.get() == '1' and b16.get() == '1' or
        # Vertical
        b1.get() == '1' and b5.get() == '1' and b9.get() == '1' and b13.get() == '1' or
        b2.get() == '1' and b6.get() == '1' and b10.get() == '1' and b14.get() == '1' or
        b3.get() == '1' and b7.get() == '1' and b11.get() == '1' and b15.get() == '1' or
        b4.get() == '1' and b8.get() == '1' and b12.get() == '1' and b16.get() == '1' or
        # Diagonal
        b1.get() == '1' and b6.get() == '1' and b11.get() == '1' and b16.get() == '1' or
        b4.get() == '1' and b7.get() == '1' and b10.get() == '1' and b13.get() == '1'
    ):
        cross()
        win_msg(1)          # Show Win Message for player 1
        start.COUNT = 0     # Set COUNT to 0 again
        start.CLICK = True  # Set CLICK to True
        clear()             # Clearing all button value
        

    elif(
        # Check the value of button with horizontal, vertical, diagonal possibility for player 2
        # Horizontal
        b1.get() == '0' and b2.get() == '0' and b3.get() == '0' and b4.get() == '0' or
        b5.get() == '0' and b6.get() == '0' and b7.get() == '0' and b8.get() == '0' or
        b9.get() == '0' and b10.get() == '0' and b11.get() == '0' and b12.get() == '0' or
        b13.get() == '0' and b14.get() == '0' and b15.get() == '0' and b16.get() == '0' or
        # Vertical
        b1.get() == '0' and b5.get() == '0' and b9.get() == '0' and b13.get() == '0' or
        b2.get() == '0' and b6.get() == '0' and b10.get() == '0' and b14.get() == '0' or
        b3.get() == '0' and b7.get() == '0' and b11.get() == '0' and b15.get() == '0' or
        b4.get() == '0' and b8.get() == '0' and b12.get() == '0' and b16.get() == '0' or
        # Diagonal
        b1.get() == '0' and b6.get() == '0' and b11.get() == '0' and b16.get() == '0' or
        b4.get() == '0' and b7.get() == '0' and b10.get() == '0' and b13.get() == '0'
    ):
        cross()
        win_msg(0)          # Show Win Message for player 2
        start.COUNT = 0     # Set COUNT to 0 again
        start.CLICK = True  # Set CLICK to True
        clear()             # Clearing all button value
    
    elif(start.COUNT == 16): # Check if the button already clicked all or not using COUNT
        tie_msg()            # Show Tie Message
        start.COUNT = 0      # Set COUNT to 0 again
        start.CLICK = True   # Set CLICK to True
        clear()              # Clearing all button value