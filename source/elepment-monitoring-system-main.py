import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App:

    def browse_file(self):
        filetypes = (("Video Files", "*.mp4 *.avi"), ("All Files", "*.*"))
        filename = filedialog.askopenfilename(title="Select a File", filetypes=filetypes)
        print(filename)


    def toggle_textbox(self, target, device_camera_text, ip_camera_text, video_text, browse_button):
        if target == "[DEVICE_CAMERA]":
            device_camera_text.configure(state="normal")
            ip_camera_text.configure(state="disabled")
            video_text.configure(state="disabled")
            browse_button.configure(state="disabled")
            

        elif target == "[IP_CAMERA]":
            device_camera_text.configure(state="disabled")
            ip_camera_text.configure(state="normal")
            video_text.configure(state="disabled")
            browse_button.configure(state="disabled")

        elif target == "[VIDEO]":
            device_camera_text.configure(state="disabled")
            ip_camera_text.configure(state="disabled")
            video_text.configure(state="normal")
            browse_button.configure(state="normal")

    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Create a full screen window
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        self.window.geometry("%dx%d" % (width, height))
        self.window.resizable(False, False)
        self.window.state("zoomed")

        # Setup placeholder image
        camera_placeholder = tk.PhotoImage(file="assets/camera-placeholder.png")
        camera_placeholder_label = tk.Label(window, image=camera_placeholder)
        camera_placeholder_label.place(x=30, y=30)


        # Create a button for Snapshot
        snapshot_button = tk.Button(window, text ="Snapshot", font=("Arial", 12, "bold"))
        snapshot_button.configure(bg="dark green", fg="white")
        snapshot_button.place(x=925, y=740)

        # Create a label frame for the options
        options_frame = tk.LabelFrame(window, text="Options", font=("Arial", 12, "bold"))
        options_frame.place(x=1100, y=30, width=790, height=750)

        r1_v = tk.IntVar()

        # Create a radio button for Device Camera
        device_camera_rb = tk.Radiobutton(options_frame, text="Device Camera", font=("Arial", 12, "bold"), command=lambda: self.toggle_textbox("[DEVICE_CAMERA]", device_camera_text, ip_camera_text, file_path_text, browse_button),  variable=r1_v, value=1)
        device_camera_rb.place(x=20, y=40)

        # Create a text box for Device Camera
        device_camera_text = tk.Entry(options_frame, width=50, state="disabled")
        device_camera_text.place(x=250, y=45)

        # Create a radio button for IP Camera
        ip_camera_rb = tk.Radiobutton(options_frame, text="IP Camera", font=("Arial", 12, "bold"), command=lambda: self.toggle_textbox("[IP_CAMERA]", device_camera_text, ip_camera_text, file_path_text, browse_button),  variable=r1_v, value=2)
        ip_camera_rb.place(x=20, y=100)

        # Create a text box for IP Camera
        ip_camera_text = tk.Entry(options_frame, width=50, state="disabled")
        ip_camera_text.place(x=250, y=105)

        # Create a radio button for Pre-Recorded Videos
        video_rb = tk.Radiobutton(options_frame, text="Video (Testing)", font=("Arial", 12, "bold"), command=lambda: self.toggle_textbox("[VIDEO]", device_camera_text, ip_camera_text, file_path_text, browse_button),  variable=r1_v, value=3)
        video_rb.place(x=20, y=160)

        # Create a text box for the file path
        file_path_text = tk.Entry(options_frame, width=37, state="disabled")
        file_path_text.place(x=250, y=165)

        # Create a browse button for Pre-Recorded Videos
        browse_button = tk.Button(options_frame, text="Browse", font=("Arial", 12, "bold"), state="disabled")
        browse_button.place(x=567, y=156)

        # Create a horizontal separator
        separator = ttk.Separator(options_frame, orient='horizontal')
        separator.place(x=20, y=250, relwidth=0.96)

        self.threshold_slider_label = tk.Label(options_frame, text="Detection Threshold",font=("Arial", 12, "bold"))
        self.threshold_slider_label.place(x=30, y=298)

        self.threshold_slider = tk.Scale(options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.threshold_slider.set(60)
        self.threshold_slider.place(x=250, y=270)

        # Create a horizontal separator
        separator = ttk.Separator(options_frame, orient='horizontal')
        separator.place(x=20, y=370, relwidth=0.96)

        self.brightness_slider_label = tk.Label(options_frame, text="Brightness",font=("Arial", 12, "bold"))
        self.brightness_slider_label.place(x=30, y=430)

        self.brightness_slider = tk.Scale(options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.brightness_slider.set(50)
        self.brightness_slider.place(x=250, y=400)

        self.contrast_slider_label = tk.Label(options_frame, text="Contrast",font=("Arial", 12, "bold"))
        self.contrast_slider_label.place(x=30, y=490)

        self.contrast_slider = tk.Scale(options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.contrast_slider.set(50)
        self.contrast_slider.place(x=250, y=460)


        self.contrast_slider_label = tk.Label(options_frame, text="Gaussian Blur",font=("Arial", 12, "bold"))
        self.contrast_slider_label.place(x=30, y=550)

        self.contrast_slider = tk.Scale(options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL)
        self.contrast_slider.set(50)
        self.contrast_slider.place(x=250, y=520)

        # Create a browse button for Pre-Recorded Videos
        start_processing_nutton = tk.Button(options_frame, text="Start Processing", font=("Arial", 12, "bold"))
        start_processing_nutton.configure(bg="dark green", fg="white")
        start_processing_nutton.place(x=576, y=650)

        # Create a browse button for Pre-Recorded Videos
        stop_processing_nutton = tk.Button(options_frame, text="Stop Processing", font=("Arial", 12, "bold"))
        stop_processing_nutton.configure(bg="dark red", fg="white")
        stop_processing_nutton.place(x=40, y=650)

        # Start the GUI loop
        self.window.mainloop()


    
# Create the application window
App(tk.Tk(), "Elephant Monitoring System")
