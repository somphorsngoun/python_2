import tkinter


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

for index1 in range(0,9):
    for index2 in range(0,9):
        if index1 == index2:
            fillcolor = "orange"
        else:
            fillcolor = "#0C2261"

        canvas.create_oval(5+(index2*50), 5+(50*index1), 50+(index2*50), 50+(index1*50), outline=fillcolor, fill=fillcolor)

# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()

