import tkinter
import random

# 1 - Crate a window
window = tkinter.Tk()

# 2 - Set size
window.geometry("900x500")

# 3 - Create a frame
frame = tkinter.Frame()

#  Set the tile
frame.master.title("CREATE BY @SOMPHORS")

# Create the cavas to draw
canvas = tkinter.Canvas(frame)
number = random.randrange(0,10)
for index in range(0,10):
    if index == number:
        fillcolor = "red"
    else:
        fillcolor = "blue"
    canvas.create_oval(index*50, 50, 50+(index*50), 100, outline="orange", fill=fillcolor)

# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()

