import tkinter as tk

window = tk.Tk()
window.title("LameLaud)

canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            color = "white"
        else:
            color = "black"
        canvas.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill=color, outline="")


canvas.create_oval(50, 50, 100, 100, fill="black", outline="black")
canvas.create_oval(150, 150, 200, 200, fill="black", outline="black")

canvas.create_oval(50, 350, 100, 400, fill="white", outline="black")
canvas.create_oval(150, 250, 200, 300, fill="white", outline="black")


window.mainloop()
