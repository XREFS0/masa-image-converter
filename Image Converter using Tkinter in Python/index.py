"""
MASA 08_Image Converter using Tkinter in Python with Source Code
Developer: MASA
"""

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from pdf2image import convert_from_path

root = Tk()
root.geometry("600x250")
root.title("MASA PixelConvert Pro")
Label(root, text="Image Converter", font="arial 24").place(x=200, y=10)


def browse():
    global img
    filename = filedialog.askopenfilename(title="Select a File")
    img = Image.open(filename)


Button(root, text="Browse an Image", command=browse, fg="blue", font="arial 18").place(x=220, y=65)


def png_to_jpg():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    img.save(export_file_path)


def jpg_to_png():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension=".png")
    img.save(export_file_path)


Button(root, text="Png To Jpg", command=png_to_jpg, fg="red", font="arial 14").place(x=70, y=155)
Button(root, text="Jpg To Png", command=jpg_to_png, fg="red", font="arial 14").place(x=430, y=155)

root.mainloop()
