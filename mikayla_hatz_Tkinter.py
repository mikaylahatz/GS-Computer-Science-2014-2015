from Tkinter import *

def keyPressed(event):
    if event.keysym == "Up" and canvas.data.y1 > 10:
        canvas.data.y1-=10
        canvas.data.y2-=10
    elif event.keysym == "Down" and canvas.data.y2 < 175:
        canvas.data.y1+=10
        canvas.data.y2+=10
    elif event.keysym == "Left" and canvas.data.x1 > 10:
        canvas.data.x1-=10
        canvas.data.x2-=10
    elif event.keysym == "Right" and canvas.data.x2 < 275:
        canvas.data.x1 += 10
        canvas.data.x2 += 10
    elif event.keysym == "space":
        canvas.data.size +=10
    elif event.keysym == "Tab":
        canvas.data.size -=10       
    else:
        pass
    
    print event.keysym

def close():
    quit()
        
   
def redrawALL():
    canvas.delete(ALL)
    canvas.create_rectangle(0, 0, canvas.data.width, canvas.data.height, fill="red")
    canvas.create_rectangle(canvas.data.x1, canvas.data.y1, canvas.data.x1+20, canvas.data.y1+20, fill = canvas.data.color)
    canvas.create_rectangle(canvas.data.blockx1, canvas.data.blocky1, canvas.data.blockx1+20, canvas.data.blocky1+20, fill = "yellow")
    canvas.create_image(canvas.data.x1, canvas.data.y1, image = canvas.photo)
    canvas.create_text(canvas.data.width/2,canvas.data.height/2, text = "Mikayla's computer", fill = "black")
    canvas.create_rectangle(canvas.data.x1, canvas.data.y1, canvas.data.x1+20, canvas.data.y1+20, fill = "black")
    if (canvas.data.x1+20 > 100 and canvas.data.y1+20 > 100):
        canvas.create_text(canvas.data.width/2,canvas.data.height/2 + 200, text = "TOO BIG", fill = "black")
        
def timerFired():
    redrawALL()
    if(canvas.data.x2 >= 150 and canvas.data.y2 >=150):
        canvas.data.color = "blue"
    else:
        canvas.data.color = "black"
    canvas.after(canvas.data.delay, timerFired)
        

def init():
    #Block
    canvas.data.x1 = 140 #top left x
    canvas.data.y1 = 90 #top left y
    canvas.data.x2 = 160 #bottom right x
    canvas.data.y2 = 110 #bottom right y
    canvas.data.color = "black"
    #Other
    canvas.data.width = 300
    canvas.data.height = 200
    canvas.data.delay = 20
    canvas.data.pressed = ""
    canvas.data.size = 20
    #second block
    canvas.data.blockx1 = 140 #top left x
    canvas.data.blocky1 = 90 #top left y
    canvas.data.blockx2 = 160 #bottom right x
    canvas.data.blocky2 = 110 #bottom right y
    canvas.data.board = [x[:] for x in [[0]*30]*20]
    canvas.data.board [4] [4] = 1
    canvas.data.board [2] [2] = 1
    photo = PhotoImage(file = "yoshi.gif")
    canvas.photo = photo

def main():
    global root
    root = Tk()
    global canvas
    canvas = Canvas(root, width = 300, height = 200)
    canvas.pack()
    class Struct(): pass
    canvas.data = Struct()
    init()
    timerFired()
    root.bind("<Key>",keyPressed)
    root.protocol("WM_DELETE_WINDOW", close)
    root.mainloop()

main()
