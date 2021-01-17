import tkinter

# 1 - Crate a window
window = tkinter.Tk()

# 2 - Set size
window.geometry("600x800")

# 3 - Create a frame
frame = tkinter.Frame()

#  Set the tile
frame.master.title("CREATE BY @SOMPHORS")

# Create the cavas to draw
canvas = tkinter.Canvas(frame)
canvas.create_oval(100, 70, 500, 90, outline="#FACE08", width=4)
canvas.create_oval(100, 100, 500, 500, outline="#FACE08", fill="#FACE08")

canvas.create_oval(190, 230, 230, 270, outline="black", fill="black")
canvas.create_oval(160, 200, 260, 300, outline="black", width=3)

canvas.create_rectangle(260, 250, 320, 253, outline="black", fill="black")
canvas.create_rectangle(230, 380, 360, 400, outline="black", fill="black")

canvas.create_oval(350, 230, 390, 270, outline="black", fill="black")
canvas.create_oval(320, 200, 420, 300, outline="black", width=3)


# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()
