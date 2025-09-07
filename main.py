import cv2 as cv
import tkinter as tk

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
    cv.waitKey(10000)
    cv.destroyAllWindows()

def button1_action():
    process_and_show("images/C130 flares.jpg")

def button2_action():
    process_and_show("images/raptor flares.jpg")

def button3_action():
    process_and_show("images/four_flares.jpg")

# Create main window
root = tk.Tk()
root.title("File Path Buttons")
root.geometry("300x200")

# Buttons
btn1 = tk.Button(root, text="C130 processed", command=button1_action, width=20)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Raptor processed", command=button2_action, width=20)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Other Jet processed", command=button3_action, width=20)
btn3.pack(pady=10)

root.mainloop()