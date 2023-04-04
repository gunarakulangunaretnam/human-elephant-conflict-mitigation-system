import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        self.width = 1000
        self.height = 700

        # create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # add a button to start processing
        self.btn_process = tk.Button(window, text="Start Processing", command=self.start_processing)
        self.btn_process.pack(pady=10)

        # create a label for the fps counter
        self.fps_label = tk.Label(window, text="")
        self.fps_label.pack()

        # set up the main loop
        self.delay = 15 # milliseconds
        self.update()

        self.window.mainloop()

    def start_processing(self):
        # open video source (by default this will try to open the computer webcam)
        self.vid = cv2.VideoCapture(self.video_source)

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

            # Calculate and display the frame rate
            self.fps_label.config(text="FPS: {:.2f}".format(self.vid.get(cv2.CAP_PROP_FPS)))

        # Schedule the next update after a delay
        self.window.after(self.delay, self.update)

    def __del__(self):
        # Release the video source when the object is destroyed
        if hasattr(self, 'vid') and self.vid.isOpened():
            self.vid.release()

# Create the application and start the main loop
App(tk.Tk(), "Tkinter + OpenCV")
