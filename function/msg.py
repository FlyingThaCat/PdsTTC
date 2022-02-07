import tkinter.messagebox as msgbox # Import Tkinter MessageBox
import json                         # Import Json for load quote data
import codecs                       # Import codecs to open json file
from random import randint          # Import Random Number in range
import function.start as fs         # Import Start

# Show Quote
def quote():
    f = codecs.open('data/quotedata.json', 'r', 'utf-8-sig') # Opening JSON file
    data = json.load(f)                                      # Returns JSON object as a dictionary
    length = len(data) - 1                                   # Get how many data in JSON
    rand = randint(0, length)                                # Generate random number whithin range of how many data in JSON
    quote = data[rand]                                       # Get random quote based in random number

    # Extract text and author from the quote
    extext = quote.get('text')
    exauthor = quote.get('from')

    msgbox.showinfo("QUOTE OF THE DAY", extext +"\n"+"\n" + exauthor) # Spawn the quote to Tkinter MessageBox With Following format
    f.close()                                                         # Closing file

# Show Message Win
def win_msg(player):
    if player == 1:
        msgbox.showinfo("TIC TAC TOE", "1 Wins !!!") # Spawn new MessageBox
        quote()                                      # Call the quote
        fs.start()                                   # StartOver

    elif player == 0:
        msgbox.showinfo("TIC TAC TOE", "0 Wins !!!") # Spawn new MessageBox
        quote()                                      # Call the quote
        fs.start()                                   # StartOver
    else :
        msgbox.showerror("TIC TAC TOE", "UH OH ..."+"/n"+"Houston we have some problem in here.") # Spawn new MessageBox

# Tie Message
def tie_msg():
    msgbox.showinfo("TIC TAC TOE", "Tie !!!") # Spawn new MessageBox
    quote()                                   # Call the quote
    fs.start()                                # StartOver

# Debug test MessageBox
def debugmsg():
    msgbox.showwarning("BONK", "BONK !!!") # Spawn new MessageBox