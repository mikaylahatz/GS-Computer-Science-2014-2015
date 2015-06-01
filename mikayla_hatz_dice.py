#import libraries
from Tkinter import *
import random

def redrawAll():
    canvas.delete(ALL)
    #draw dice
    canvas.create_image(canvas.data.x1,canvas.data.y1,image=canvas.data.images[canvas.data.diceVal[1]])
    canvas.create_image(canvas.data.x1+100,canvas.data.y1,image=canvas.data.images[canvas.data.diceVal[2]])
    canvas.create_image(canvas.data.x1+200,canvas.data.y1,image=canvas.data.images[canvas.data.diceVal[3]])
    canvas.create_image(canvas.data.x1+300,canvas.data.y1,image=canvas.data.images[canvas.data.diceVal[4]])
    canvas.create_image(canvas.data.x1+400,canvas.data.y1,image=canvas.data.images[canvas.data.diceVal[5]])
    canvas.create_text(300,90,text=canvas.data.sumOfDisplayedDice)
    canvas.create_text(canvas.data.width/2,canvas.data.height/2 + 200, text = "Petals Around the Rose", fill = "black")

def close():
    #used to properly handle closing the GUI window
    quit()

def getRandName():
    canvas.data.sumOfDisplayedDice = 0
    for j in canvas.data.diceVal.keys():
        randValue = random.randrange(1,7)
        canvas.data.diceVal[j] = canvas.data.numbers[randValue]
        


def init():
    canvas.data.numbers = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"}
    canvas.data.x1 = 100
    canvas.data.y1 = 250
    canvas.data.height = -300 #text
    canvas.data.width = 600 #text
    
    #holds the currently displayed dice's value in words. Changed by pushing the button labeled "Roll the Dice"
    #the number of elements should change as the number of dice increases

    canvas.data.diceVal = {1:'one',2:'two',3:'three',4:'four',5:'five'}
    
    canvas.data.images = {}
    
    canvas.data.sumOfDisplayedDice = 0
    #load each of the images contained in the dice gifs
    for i in canvas.data.numbers.values():
        canvas.data.images[i] = PhotoImage(file=i+".gif").subsample(4,4)

def rollDice():
    #"roll" dice whenever button referenced by the variable butt1 is pushed
    #1st select a random number and get it's text value
    getRandName()
    
    for i in canvas.data.diceVal.keys():
        if canvas.data.diceVal[i] == "three":
            canvas.data.sumOfDisplayedDice+=2
        if canvas.data.diceVal[i] == "five":
            canvas.data.sumOfDisplayedDice+=4
            
    #redraw the screen
    redrawAll()

def main():
    #the variable root holds a reference to the main window (the one that holds everything else)
    global root
    root = Tk()
    root.geometry("600x500+300+300")

    #canvas variable is a reference to the area we are displaying the dice in
    global canvas
    canvas = Canvas(root,width=1000,height=450)
    canvas.pack()

    global frame
    #frame is a holder for our buttons
    frame = Frame(root,bg="grey",width=100, height=50)
    #fill='x' is used to
    frame.pack(fill='x')

    #butt1 is a button that calls the function rollDice()
    butt1 = Button(frame,text="Roll The Dice",command=rollDice)
    butt1.configure(activebackground = "grey", relief = FLAT)
    butt1.pack(fill='x')

    #canvas.data is a data structure that holds all of our data in one place
    class Struct(): pass
    canvas.data = Struct()

    #initialize all of our different variables (which are mostly contained in canvas.data
    init()
    #add a reference to the close() function which is called whenever the red x button is pushed.
    root.protocol("WM_DELETE_WINDOW", close)
    root.wm_title("Roll The Dice")
    #launch the GUI
    root.mainloop()

main()
