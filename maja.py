import tkinter as tk

window = tk.Tk()
window.title("Maja")

canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()


canvas.create_polygon(100, 200, 200, 100, 300, 200, fill="brown", outline="black")

canvas.create_rectangle(100, 200, 300, 350, fill="yellow", outline="black")

canvas.create_rectangle(125, 225, 175, 275, fill="blue", outline="black")
canvas.create_rectangle(225, 225, 275, 275, fill="blue", outline="black")


window.mainloop()
