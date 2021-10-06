import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height = 600,bg="#ECF1F4")

logo = Image.open('arrow_down.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, fill="")
logo_label.image = logo
canvas.place(x=0,y=0)
logo_label.place(x=0,y=0)

root.mainloop()