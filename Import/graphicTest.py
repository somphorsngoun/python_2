import tkinter

# 1 - Crate a window
window = tkinter.Tk()

# 2 - Set size
window.geometry("10000x20000")

# 3 - Create a frame
frame = tkinter.Frame()

#  Set the tile
frame.master.title("CREATE BY @SOMPHORS")

# Create the cavas to draw
canvas = tkinter.Canvas(frame)
canvas.create_oval(385, 20, 505, 240,  outline="#E59866", fill="#E59866")
canvas.create_oval(830, 20, 950, 240, outline="#E59866", fill="#E59866")

canvas.create_oval(80, 60, 1250, 1000, outline="#EDBB99", fill="#EDBB99")

canvas.create_oval(355, 170, 505, 240,  outline="gray")
canvas.create_oval(385, 170, 475, 240,  outline="black", fill="black")
canvas.create_oval(820, 170, 980, 240, outline="gray")
canvas.create_oval(850, 170, 950, 240, outline="black", fill="black")

canvas.create_oval(600, 320, 720, 380, outline="#808B96", fill="#808B96")
canvas.create_oval(357, 390, 963, 685, outline="#EAEDED", fill="#EAEDED")
canvas.create_oval(380, 430, 940, 600, outline="red", fill="red")
canvas.create_oval(370, 410, 950, 590, outline="#EAEDED", fill="#EAEDED")


# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()
