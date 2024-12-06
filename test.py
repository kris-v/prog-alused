import tkinter as tk

# Loome akna
window = tk.Tk()
window.title("Raudteeülesõidukoha märk")

# Määrame akna suuruse
window.geometry("400x400")

# Loome kanva
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

# Joonistame märgi
# Tõkkepuu
canvas.create_rectangle(100, 200, 300, 300, fill="brown")
canvas.create_rectangle(150, 250, 250, 350, fill="brown")

# Raudteeülesõidukoha märk
canvas.create_rectangle(50, 50, 350, 150, fill="white")
canvas.create_text(200, 100, text="RAUDTEEÜLESÕIDUKOHT", font=("Arial", 20))

# Käivitame akna
window.mainloop()
