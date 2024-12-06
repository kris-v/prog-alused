import tkinter as tk

def create_lipp():
    root = tk.Tk()
    root.title("Lipp")

    width = 400
    height = 300
    root.geometry(f"{width}x{height}")

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()


    canvas.create_rectangle(0, 0, width, height//3, fill="blue", outline="")


    canvas.create_rectangle(0, height//3, width, 2*height//3, fill="black", outline="")


    canvas.create_rectangle(0, 2*height//3, width, height, fill="white", outline="")


    root.mainloop()

create_lipp()
