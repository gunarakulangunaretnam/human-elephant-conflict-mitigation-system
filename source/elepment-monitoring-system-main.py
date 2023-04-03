import tkinter as tk
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Create a full screen window
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))
        self.window.resizable(False, False)
        self.window.state("zoomed")

        # Create a label to display the processed image
        self.lbl_image = tk.Label(self.window)
        self.lbl_image.pack(padx=10, pady=10)
        
        # Open the camera
        self.capture = cv2.VideoCapture(0)
        
        # Start the GUI loop
        self.window.mainloop()
    
# Create the application window
App(tk.Tk(), "Elephant Monitoring System")
