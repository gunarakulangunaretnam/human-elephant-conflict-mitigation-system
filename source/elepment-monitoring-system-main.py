import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import PIL.Image, PIL.ImageTk

class App:

    def browse_file(self):
        filetypes = (("Video Files", "*.mp4 *.avi"), ("All Files", "*.*"))
        filename = filedialog.askopenfilename(title="Select a File", filetypes=filetypes)
        print(filename)

    def toggle_textbox(self, target):
        if target == "[DEVICE_CAMERA]":

            self.device_camera_text.delete(0, "end")
            self.ip_camera_text.delete(0, "end")
            self.file_path_text.delete(0, "end")

            self.device_camera_text.configure(state="normal")
            self.ip_camera_text.configure(state="disabled")
            self.file_path_text.configure(state="disabled")

            self.browse_button.configure(state="disabled")
            

        elif target == "[IP_CAMERA]":

            self.device_camera_text.delete(0, "end")
            self.ip_camera_text.delete(0, "end")
            self.file_path_text.delete(0, "end")

            self.device_camera_text.configure(state="disabled")
            self.ip_camera_text.configure(state="normal")
            self.file_path_text.configure(state="disabled")

            self.browse_button.configure(state="disabled")

        elif target == "[VIDEO]":

            self.device_camera_text.delete(0, "end")
            self.ip_camera_text.delete(0, "end")
            self.file_path_text.delete(0, "end")

            self.device_camera_text.configure(state="disabled")
            self.ip_camera_text.configure(state="disabled")
            self.file_path_text.configure(state="normal")

            self.browse_button.configure(state="normal")

    def browse_file(self):
        # Ask user to select a video file
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
    
        if file_path:
            # Set the file path in the entry widget
            self.file_path_text.delete(0, "end")
            self.file_path_text.insert(0, file_path)
            print(file_path)

    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)

        self.video_source = video_source
        self.width = 1000
        self.height = 700

        # create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.place(x=30, y=30)

        # set up the main loop
        self.delay = 15 # milliseconds
        self.update()

        # Create a full screen window
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        self.window.geometry("%dx%d" % (width, height))
        self.window.resizable(False, False)
        self.window.state("zoomed")

        # Setup placeholder image
        self.camera_placeholder = tk.PhotoImage(file="assets/camera-placeholder.png")
        self.camera_placeholder_label = tk.Label(window, image=self.camera_placeholder)
        self.camera_placeholder_label.place(x=30, y=30)


        # Create a button for Snapshot
        self.snapshot_button = tk.Button(window, text ="Snapshot", font=("Arial", 12, "bold"))
        self.snapshot_button.configure(bg="dark green", fg="white")
        self.snapshot_button.place(x=925, y=740)

        # Create a label frame for the options
        self.options_frame = tk.LabelFrame(window, text="Options", font=("Arial", 12, "bold"))
        self.options_frame.place(x=1100, y=30, width=790, height=750)

        self.r1_v = tk.IntVar()

        # Create a radio button for Device Camera
        self.device_camera_rb = tk.Radiobutton(self.options_frame, text="Device Camera", font=("Arial", 12, "bold"), command=lambda: self.toggle_textbox("[DEVICE_CAMERA]"),  variable=self.r1_v, value=1)
        self.device_camera_rb.place(x=20, y=40)

        # Create a text box for Device Camera
        self.device_camera_text = tk.Entry(self.options_frame, width=50, state="disabled")
        self.device_camera_text.place(x=250, y=45)

        # Create a radio button for IP Camera
        self.ip_camera_rb = tk.Radiobutton(self.options_frame, text="IP Camera", font=("Arial", 12, "bold"), command=lambda: self.toggle_textbox("[IP_CAMERA]"), variable = self.r1_v, value=2)
        self.ip_camera_rb.place(x=20, y=100)

        # Create a text box for IP Camera
        self.ip_camera_text = tk.Entry(self.options_frame, width=50, state="disabled")
        self.ip_camera_text.place(x=250, y=105)

        # Create a radio button for Pre-Recorded Videos
        self.video_rb = tk.Radiobutton(self.options_frame, text="Video (Testing)", font=("Arial", 12, "bold"), command=lambda: self.toggle_textbox("[VIDEO]"),  variable = self.r1_v, value=3)
        self.video_rb.place(x=20, y=160)

        # Create a text box for the file path
        self.file_path_text = tk.Entry(self.options_frame, width=37, state="disabled")
        self.file_path_text.place(x=250, y=165)

        # Create a browse button for Pre-Recorded Videos
        self.browse_button = tk.Button(self.options_frame, text="Browse", font=("Arial", 12, "bold"), state="disabled", command=lambda: self.browse_file())
        self.browse_button.place(x=567, y=156)

        # Create a horizontal separator
        self.separator = ttk.Separator(self.options_frame, orient='horizontal')
        self.separator.place(x=20, y=250, relwidth=0.96)

        self.threshold_slider_label = tk.Label(self.options_frame, text="Detection Threshold",font=("Arial", 12, "bold"))
        self.threshold_slider_label.place(x=30, y=298)

        self.threshold_slider = tk.Scale(self.options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.threshold_slider.set(60)
        self.threshold_slider.place(x=250, y=270)

        # Create a horizontal separator
        self.separator = ttk.Separator(self.options_frame, orient='horizontal')
        self.separator.place(x=20, y=370, relwidth=0.96)

        self.brightness_slider_label = tk.Label(self.options_frame, text="Brightness",font=("Arial", 12, "bold"))
        self.brightness_slider_label.place(x=30, y=430)

        self.brightness_slider = tk.Scale(self.options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.brightness_slider.set(50)
        self.brightness_slider.place(x=250, y=400)

        self.contrast_slider_label = tk.Label(self.options_frame, text="Contrast",font=("Arial", 12, "bold"))
        self.contrast_slider_label.place(x=30, y=490)

        self.contrast_slider = tk.Scale(self.options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.contrast_slider.set(50)
        self.contrast_slider.place(x=250, y=460)


        self.contrast_slider_label = tk.Label(self.options_frame, text="Gaussian Blur",font=("Arial", 12, "bold"))
        self.contrast_slider_label.place(x=30, y=550)

        self.contrast_slider = tk.Scale(self.options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.contrast_slider.set(50)
        self.contrast_slider.place(x=250, y=520)

        # Create a browse button for Pre-Recorded Videos
        self.start_processing_nutton = tk.Button(self.options_frame, text="Start Processing", font=("Arial", 12, "bold"), command=self.start_processing)
        self.start_processing_nutton.configure(bg="dark green", fg="white")
        self.start_processing_nutton.place(x=576, y=650)

        # Create a browse button for Pre-Recorded Videos
        self.stop_processing_nutton = tk.Button(self.options_frame, text="Stop Processing", font=("Arial", 12, "bold"))
        self.stop_processing_nutton.configure(bg="dark red", fg="white")
        self.stop_processing_nutton.place(x=40, y=650)

        # Start the GUI loop
        self.window.mainloop()

    def start_processing(self):
        # open video source (by default this will try to open the computer webcam)
        self.camera_placeholder_label.place_forget()
        self.vid = cv2.VideoCapture(self.video_source)
        self.window.update()

    def update(self):
        if hasattr(self, 'vid'):
            # Get a frame from the video source
            ret, frame = self.vid.read()

            if ret:
                # Convert the frame to RGB format and resize it to fit the canvas
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (self.width, self.height))

                # Convert the frame to an ImageTk object and display it on the canvas
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # Schedule the next update after a delay
        self.window.after(self.delay, self.update)
        

    def __del__(self):
        # Release the video source when the object is destroyed
        if hasattr(self, 'vid') and self.vid.isOpened():
            self.vid.release()

    
# Create the application window
App(tk.Tk(), "Elephant Monitoring System")
