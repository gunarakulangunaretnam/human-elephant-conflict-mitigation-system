import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import PIL.Image, PIL.ImageTk
import os  
import sys
import six
import cv2   
import uuid  
import pygame                                                                                                                            # OpenCV for Computer Vision                                                        # It has a dictionary that contains colors for each label
import argparse                                                            
import collections
import numpy as np
import pyttsx3                                                            
import threading                                                          
import playsound                                                          
import tensorflow as tf 

sys.path.append('assets')                                                  
from object_detection.utils import label_map_util                         
from object_detection.utils import config_util                             
from object_detection.utils import visualization_utils as viz_utils      
from object_detection.builders import model_builder                       


number_of_time_detected = 0
alaram_threshold = 5

is_audio_playing = False
pygame.mixer.init()

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

model_config_path =  f'assets/model-data/models/ssd_mobilenet_v2_320x320_coco17_tpu-8/pipeline.config'        # Store the path of config file
checkpoint_model_path   =  f'assets/model-data/models/ssd_mobilenet_v2_320x320_coco17_tpu-8/checkpoint/ckpt-0'      # Store the path of model
label_map_path    =  f'assets/model-data/mscoco_label_map.pbtxt'                             # Store the path of label_map

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(model_config_path)
model_config = configs['model']
detection_model = model_builder.build(model_config=model_config, is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(checkpoint_model_path).expect_partial()

category_index = label_map_util.create_category_index_from_labelmap(label_map_path,use_display_name=True)


class App:

    def __init__(self, window, window_title, video_source='test-video.m4v'):
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

    def detect_fn(self, image):
        image, shapes = detection_model.preprocess(image)
        prediction_dict = detection_model.predict(image, shapes)
        detections = detection_model.postprocess(prediction_dict, shapes)

        return detections, prediction_dict, tf.reshape(shapes, [-1])


    def bees_sound_effect_function(self):
        global is_audio_playing

        pygame.mixer.music.load('assets\\bees-sound-effect.mp3')
        pygame.mixer.music.play()


        while pygame.mixer.music.get_busy():
            pass
        
        is_audio_playing = False

        print("dd")


    def update(self):
        global number_of_time_detected, alaram_threshold, is_audio_playing

        if hasattr(self, 'vid'):
            # Get a frame from the video source
            ret, frame = self.vid.read()

            if ret:
                image_np_expanded = np.expand_dims(frame, axis=0)
                input_tensor = tf.convert_to_tensor(np.expand_dims(frame, 0), dtype=tf.float32)
                detections, predictions_dict, shapes = self.detect_fn(input_tensor)

                label_id_offset = 1
                image_np_with_detections = frame.copy()

                min_score_thresh = 0.50

                box_to_display_str_map = collections.defaultdict(list)
                box_to_color_map = collections.defaultdict(str)

                number_of_elephants = 0

                for i in range(detections['detection_boxes'][0].numpy().shape[0]):

                    if detections['detection_scores'][0].numpy() is None or detections['detection_scores'][0].numpy()[i] > min_score_thresh:

                        box = tuple(detections['detection_boxes'][0].numpy()[i].tolist())

                        display_str = ""

                        if(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i] in six.viewkeys(category_index):
                            class_name = category_index[(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i]]['name']
                            display_str = '{}'.format(class_name)

                            box_to_display_str_map[box].append(display_str) # Join the number of eleements with label Name
                            
                            if "elephant" in box_to_display_str_map[box][0]:
                                number_of_elephants = number_of_elephants + 1

                im_width, im_height = frame.shape[1::-1]

                for box, color in box_to_display_str_map.items():
                    ymin, xmin, ymax, xmax = box

                    ymin = ymin * im_height
                    xmin = xmin * im_width
                    ymax = ymax * im_height
                    xmax = xmax * im_width

                    x = xmin
                    y = ymin
                    w = xmax - xmin
                    h = ymax - ymin

                    if box_to_display_str_map[box][0].replace("_"," ") == "elephant": # Get only label name not the total number of items

                        cv2.rectangle(image_np_with_detections, (int(x),int(y)), (int(x) + int(w), int(y) + int(h)), (0, 0, 255), 4)
                        (tw, th), _ = cv2.getTextSize(box_to_display_str_map[box][0], cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)

                        # Prints the text.
                        img = cv2.rectangle(image_np_with_detections, (int(x), int(y) - 30), (int(x) + 20 + tw, int(y)), (0, 0, 255), -1)
                        img = cv2.putText(image_np_with_detections, box_to_display_str_map[box][0].upper(), (int(x)+5, int(y) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)

                        number_of_time_detected = number_of_time_detected + 1

                        if number_of_time_detected == alaram_threshold:

                            if is_audio_playing == False:
                                is_audio_playing = True
                                bees_sound_effect_function = threading.Thread(target = self.bees_sound_effect_function, args=(), daemon=True)
                                bees_sound_effect_function.start()
                            
                            cv2.imwrite(f"predictions/{uuid.uuid1()}.jpg", image_np_with_detections)
                            number_of_time_detected = 0

                final_frame = cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB)
                final_frame = cv2.resize(final_frame, (self.width, self.height))

                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(final_frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

                           
        # Schedule the next update after a delay
        self.window.after(self.delay, self.update)
        

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

    def __del__(self):
        # Release the video source when the object is destroyed
        if hasattr(self, 'vid') and self.vid.isOpened():
            self.vid.release()

    
# Create the application window
App(tk.Tk(), "Elephant Monitoring System")
