import tkinter as tk
from tkinter import Canvas

root = tk.Tk()
root.title("Lipp")

canvas = Canvas(root, width=400, height=260)
canvas.pack()


canvas.create_rectangle(0, 0, 400, 300, fill="green", outline="")
canvas.create_rectangle(0, 100, 400, 150, fill="yellow", outline="")
canvas.create_rectangle(0, 150, 400, 300, fill="blue", outline="")


root.mainloop()
