import cv2 as cv
import tkinter as tk
from tkinter import *
from tkinter import filedialog

def process_and_show(image_path):
    flarePhoto = cv.imread(image_path)

    # Convert to gray
    grayPhoto = cv.cvtColor(flarePhoto, cv.COLOR_BGR2GRAY)

    # Threshold
    _, thresh = cv.threshold(grayPhoto, 200, 255, cv.THRESH_BINARY)

    # Find contours
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #red rectangles
    for c in contours:
        x, y, w, h = cv.boundingRect(c)
        if w > 2 and h > 2:  # ignore tiny noise
            cv.rectangle(flarePhoto, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show image with rectangles
    cv.imshow("Light Sources Detected", flarePhoto)
    cv.waitKey(0)
    cv.destroyAllWindows()

def button1_action():
    process_and_show("images/C130 flares.jpg")

def button2_action():
    process_and_show("images/raptor flares.jpg")

def button3_action():
    process_and_show("images/four_flares.jpg")

def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if file_path:
        process_and_show(file_path)

# Create main window
root = tk.Tk()
root.title("File Path Buttons")
w = Label(root, text='Pre Packaged Flare Pictures Process Them Now!')
w.pack()
root.geometry("300x250")

# Buttons
btn1 = tk.Button(root, text="C130 processed", command=button1_action, width=20)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Raptor processed", command=button2_action, width=20)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Other Jet processed", command=button3_action, width=20)
btn3.pack(pady=10)

w = Label(root, text='Or upload your own to be processed...')
w.pack()

# Upload button
btn_upload = tk.Button(root, text="Upload Image", command=upload_image, width=25)
btn_upload.pack(pady=10)

root.mainloop()