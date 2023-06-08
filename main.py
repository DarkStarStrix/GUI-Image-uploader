# create a graphical user interface for the program where you can upload a file and add a watermark to it

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import watermark

# create a window
window = Tk()
window.title("Watermark")
window.geometry("500x500")
window.config(bg="white")

# create a canvas
canvas = Canvas(window, width=300, height=300, bg="white", highlightthickness=0)
canvas.place(x=100, y=100)

# create a label
label = Label(window, text="Watermark", font=("Arial", 28, "bold"), bg="white", fg="black")
label.place(x=140, y=50)

# create a function to upload a file
global im, img, filename


def upload():
    global im, img, filename
    try:
        # open a file dialog
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a file")
        # open an image
        im = Image.open(filename)
        # resize the image
        im = im.resize((300, 300))
        # convert the image to tkinter format
        img = ImageTk.PhotoImage(im)
        # display the image
        canvas.create_image(150, 150, image=img)
    except:
        # display an error message
        messagebox.showerror("Error", "File not found")


# create a function to add a watermark
def add_watermark():
    global im, img, filename
    try:
        # add a watermark to the image
        im = watermark.watermark(im, "watermark.png")
        # convert the image to tkinter format
        img = ImageTk.PhotoImage(im)
        # display the image
        canvas.create_image(150, 150, image=img)
    except:
        # display an error message
        messagebox.showerror("Error", "File not found")


# create a button to upload a file
upload_button = Button(window, text="Upload", font=("Arial", 20, "bold"), bg="white", fg="black", command=upload)
upload_button.place(x=100, y=420)

# create a button to add a watermark
add_button = Button(window, text="Add Watermark", font=("Arial", 20, "bold"), bg="white", fg="black",
                    command=add_watermark)
add_button.place(x=250, y=420)

window.mainloop()
