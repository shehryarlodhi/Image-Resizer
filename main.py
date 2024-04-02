import cv2
import tkinter as tk
from tkinter import filedialog

#taking image input
root = tk.Tk()
root.withdraw()
source = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
#setting modified file
destination = "modified-img.png"
scale_percent = input("Enter the percentage you want to scale the image: ")

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)

new_width=int(src.shape[1]*int(scale_percent)/100)
new_height=int(src.shape[0]*int(scale_percent)/100)

output=cv2.resize(src,(new_width,new_height))

cv2.imwrite(destination,output)
cv2.waitKey(0)