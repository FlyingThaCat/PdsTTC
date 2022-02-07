from function.button import *   # Import All button module

def setcross(h, v, d): # Create new Function
    #Checking value and set cross line
    if h == 1:
        b1.set("-") 
        b2.set("-")
        b3.set("-")
        b4.set("-")
    elif h == 2:
        b5.set("-") 
        b6.set("-")
        b7.set("-")
        b8.set("-")
    elif h == 3:
        b9.set("-") 
        b10.set("-")
        b11.set("-")
        b12.set("-")
    elif h == 4:
        b13.set("-") 
        b14.set("-")
        b15.set("-")
        b16.set("-")
    elif v == 1:
        b1.set("|") 
        b5.set("|") 
        b9.set("|") 
        b13.set("|")
    elif v == 2:
        b2.set("|") 
        b6.set("|") 
        b10.set("|") 
        b14.set("|")
    elif v == 3:
        b3.set("|") 
        b7.set("|") 
        b11.set("|") 
        b15.set("|")
    elif v == 4:
        b4.set("|") 
        b8.set("|") 
        b12.set("|") 
        b16.set("|")
    elif d == 1:
        b1.set("\\") 
        b6.set("\\") 
        b11.set("\\") 
        b16.set("\\")
    elif d == 2:
        b4.set("/") 
        b7.set("/") 
        b10.set("/") 
        b13.set("/")