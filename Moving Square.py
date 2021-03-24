from tkinter import *
import time
gui = Tk()
gui.geometry("1000x800")
gui.title("Moving Square")
canvas = Canvas(gui, width=1000, height=800, bg='white')
canvas.pack()

square1 = canvas.create_rectangle(5,5,60,60, fill='red')
xa=5
ya=5

while True:
    canvas.move(square1, xa, ya)
    pos = canvas.coords(square1)
    if pos[3] >= 800 or pos[1] <= 0:
        ya = -ya
    if pos[2] >= 1000 or pos[0] <= 0:
        xa = -xa
    gui.update()
    time.sleep(.005)

gui.mainloop()