from function.button import b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16  # Import All button module
from function.setcross import setcross  # Import setcross function

def cross():
    """
    |-----------|
    |1 |2 |3 |4 |
    |5 |6 |7 |8 |
    |9 |10|11|12|
    |13|14|15|16|
    |-----------|
    """
    # Check the value of button with horizontal, vertical, diagonal possibility for player 1
    # Horizontal
    if (b1.get() == '1' and b2.get() == '1' and b3.get() == '1' and b4.get() == '1'):       # Checking button position
        setcross(1, 0, 0)                                                                   # Calling function command
    elif (b5.get() == '1' and b6.get() == '1' and b7.get() == '1' and b8.get() == '1'):
        setcross(2, 0, 0)
    elif (b9.get() == '1' and b10.get() == '1' and b11.get() == '1' and b12.get() == '1'):
        setcross(3, 0, 0)
    elif (b13.get() == '1' and b14.get() == '1' and b15.get() == '1' and b16.get() == '1'):
        setcross(4, 0, 0)
    
    # Vertical
    elif (b1.get() == '1' and b5.get() == '1' and b9.get() == '1' and b13.get() == '1'):
        setcross(0, 1, 0)
    elif (b2.get() == '1' and b6.get() == '1' and b10.get() == '1' and b14.get() == '1'):
        setcross(0, 2, 0)
    elif (b3.get() == '1' and b7.get() == '1' and b11.get() == '1' and b15.get() == '1'):
        setcross(0, 3, 0)
    elif (b4.get() == '1' and b8.get() == '1' and b12.get() == '1' and b16.get() == '1'):
        setcross(0, 4, 0)
    
    # Diagonal
    elif (b1.get() == '1' and b6.get() == '1' and b11.get() == '1' and b16.get() == '1'):
        setcross(0, 0, 1)
    elif (b4.get() == '1' and b7.get() == '1' and b10.get() == '1' and b13.get() == '1'):
        setcross(0, 0, 2)


    # Check the value of button with horizontal, vertical, diagonal possibility for player 2
    # Horizontal
    elif (b1.get() == '0' and b2.get() == '0' and b3.get() == '0' and b4.get() == '0'):
        setcross(1, 0, 0)
    elif (b5.get() == '0' and b6.get() == '0' and b7.get() == '0' and b8.get() == '0'):
        setcross(2, 0, 0)
    elif (b9.get() == '0' and b10.get() == '0' and b11.get() == '0' and b12.get() == '0'):
        setcross(3, 0, 0)
    elif (b13.get() == '0' and b14.get() == '0' and b15.get() == '0' and b16.get() == '0'):
        setcross(4, 0, 0)
    
    # Vertical
    elif (b1.get() == '0' and b5.get() == '0' and b9.get() == '0' and b13.get() == '0'):
        setcross(0, 1, 0)
    elif (b2.get() == '0' and b6.get() == '0' and b10.get() == '0' and b14.get() == '0'):
        setcross(0, 2, 0)
    elif (b3.get() == '0' and b7.get() == '0' and b11.get() == '0' and b15.get() == '0'):
        setcross(0, 3, 0)
    elif (b4.get() == '0' and b8.get() == '0' and b12.get() == '0' and b16.get() == '0'):
        setcross(0, 4, 0)
    
    # Diagonal
    elif (b1.get() == '0' and b6.get() == '0' and b11.get() == '0' and b16.get() == '0'):
        setcross(0, 0, 1)
    elif (b4.get() == '0' and b7.get() == '0' and b10.get() == '0' and b13.get() == '0'):
        setcross(0, 0, 2)