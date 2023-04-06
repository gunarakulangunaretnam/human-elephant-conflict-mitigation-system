import re
import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import PIL.Image, PIL.ImageTk
from PIL import ImageGrab
import os  
import sys
import six
import cv2   
import uuid  
import json
import pygame                                                                                                                            # OpenCV for Computer Vision                                                        # It has a dictionary that contains colors for each label
import argparse                                                            
import collections
import numpy as np
import pyttsx3                                                            
import threading                                                          
import playsound                                                          
import tensorflow as tf 
from datetime import datetime
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append('assets')                                                  
from object_detection.utils import label_map_util                         
from object_detection.utils import config_util                             
from object_detection.utils import visualization_utils as viz_utils      
from object_detection.builders import model_builder                       


number_of_time_detected = 0
alaram_threshold = 6

selected_model = "SSD M-Net V2 Keras 320x320 (Medium Speed | High Accuracy)"

is_processing = False
is_sound_effect_changed = False
is_audio_playing = False

pygame.mixer.init()

global_variable_snapshot_frame = ""

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)



global_configs = ""
global_model_config = ""
global_detection_model = ""
global_ckpt = ""
global_category_index = ""

def load_model_function(model_config_path, checkpoint_model_path, label_map_path):
    global global_configs, global_model_config, global_detection_model, global_ckpt, global_category_index, global_category_index
                                         
    # Load pipeline config and build a detection model
    global_configs = config_util.get_configs_from_pipeline_file(model_config_path)
    global_model_config = global_configs['model']
    global_detection_model = model_builder.build(model_config=global_model_config, is_training=False)

    # Restore checkpoint
    global_ckpt = tf.compat.v2.train.Checkpoint(model=global_detection_model)
    global_ckpt.restore(checkpoint_model_path).expect_partial()

    global_category_index = label_map_util.create_category_index_from_labelmap(label_map_path,use_display_name=True)


class App:

    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.width = 1000
        self.height = 700
        self.detection_threshold = 60

        self.brightness = 50
        self.contrast = 50
        self.blur = 0

        # Create a canvas that can fit the above video source size
        self.camera_window = tk.Canvas(window, width=self.width, height=self.height)
        self.camera_window.place(x=30, y=30)
        self.camera_window.place_forget()

        # Create a full screen window
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()

        self.window.geometry("%dx%d" % (width, height))
        self.window.resizable(False, False)
        self.window.state("zoomed")

        # Setup placeholder image
        self.camera_placeholder = tk.PhotoImage(file="assets/styles/camera-placeholder.png")
        self.camera_placeholder_label = tk.Label(window, image=self.camera_placeholder)
        self.camera_placeholder_label.place(x=30, y=30)

        # Create a button for Snapshot
        self.snapshot_button = tk.Button(window, text ="Snapshot", font=("Arial", 12, "bold"), command=lambda: self.take_snapshots())
        self.snapshot_button.configure(bg="dark green", fg="white")
        self.snapshot_button.place(x=925, y=740)

        # Create a label frame for the options
        self.options_frame = tk.LabelFrame(window, text="Options", font=("Arial", 12, "bold"))
        self.options_frame.place(x=1100, y=20, width=790, height=940)

        self.r1_v = tk.IntVar()

        # Create a radio button for Device Camera
        self.device_camera_rb = tk.Radiobutton(self.options_frame, text="Device Camera", font=("Arial", 12, "bold"), command=lambda: self.toggle_textbox("[DEVICE_CAMERA]"),  variable=self.r1_v, value=1)
        self.device_camera_rb.place(x=20, y=40)

        self.device_camera_combo = ttk.Combobox(self.options_frame, state="disabled", width=47)
        self.device_camera_combo.place(x=250, y=45)
        self.get_all_cameras()

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
        self.threshold_slider.set(self.detection_threshold)
        self.threshold_slider.bind("<ButtonRelease-1>", lambda event: self.on_threshold_change(self.threshold_slider.get()))
        self.threshold_slider.place(x=250, y=270)

        self.alarm_label = tk.Label(self.options_frame, text="Alarm", font=("Arial", 12, "bold"))
        self.alarm_label.place(x=30, y=370)

        self.switch_status = True
        self.on_button_image = tk.PhotoImage(file = "assets/styles/switch-button/on.png")
        self.off_button_image = tk.PhotoImage(file = "assets/styles/switch-button/off.png")
        self.on_button = tk.Button(self.options_frame, image = self.on_button_image, bd = 0, command = self.switch_on_off_function)
        self.on_button.place(x=250, y=360)

        self.sound_effect_label = tk.Label(self.options_frame, text="Sound Effect:", font=("Arial", 12, "bold"))
        self.sound_effect_label.place(x=30, y=440)

        self.sound_effects_combobox_options = ["Buzzing Bees Sound", "Firecrackers Sound" ,  "Warning Alarm Sound"]
        self.sound_effects_combobox = ttk.Combobox(self.options_frame, values=self.sound_effects_combobox_options, font=("Arial", 10), width=30, state="readonly")
        self.sound_effects_combobox.current(0)
        self.sound_effects_combobox.bind("<<ComboboxSelected>>", self.on_sound_effect_change)
        self.sound_effects_combobox.place(x=250, y=440)

        self.sound_effect_label = tk.Label(self.options_frame, text="Model Architecture:", font=("Arial", 12, "bold"))
        self.sound_effect_label.place(x=30, y=500)

        self.model_architecture_combobox_options = ["SSD M-Net V2 FPN Keras 320x320 (High Speed | Low Accuracy)", "SSD M-Net V2 Keras 320x320 (Medium Speed | Medium Accuracy)", "SSD M-Net V2 FPN LITE 320x320 (Medium Speed | High Accuracy)", "SSD M-Net V2 FPN LITE 640x640 (Low Speed | High Accuracy)", "SSD M-Net V1 FPN 640x640 (Low Speed | High Accuracy)"]
        self.model_architecture_combobox = ttk.Combobox(self.options_frame, values=self.model_architecture_combobox_options, font=("Arial", 10), width=52, state="readonly")
        self.model_architecture_combobox.current(4)
        self.model_architecture_combobox.bind("<<ComboboxSelected>>", self.on_model_architecture_change)
        self.model_architecture_combobox.place(x=250, y=500)

        # Create a horizontal separator
        self.separator = ttk.Separator(self.options_frame, orient='horizontal')
        self.separator.place(x=20, y=570, relwidth=0.96)

        self.brightness_slider_label = tk.Label(self.options_frame, text="Brightness",font=("Arial", 12, "bold"))
        self.brightness_slider_label.place(x=30, y=620)

        self.brightness_slider = tk.Scale(self.options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL, command=self.set_brightness)
        self.brightness_slider.set(self.brightness)
        self.brightness_slider.place(x=250, y=590)

        self.contrast_slider_label = tk.Label(self.options_frame, text="Contrast",font=("Arial", 12, "bold"))
        self.contrast_slider_label.place(x=30, y=690)

        self.contrast_slider = tk.Scale(self.options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL, command=self.set_contrast)
        self.contrast_slider.set(self.contrast)
        self.contrast_slider.place(x=250, y=660)

        self.gaussian_blur_slider_label = tk.Label(self.options_frame, text="Gaussian Blur",font=("Arial", 12, "bold"))
        self.gaussian_blur_slider_label.place(x=30, y=760)

        self.gaussian_blur_slider = tk.Scale(self.options_frame, from_=0, to=100, width=30,length=500, orient=tk.HORIZONTAL, command=self.set_blur)
        self.gaussian_blur_slider.set(self.blur)
        self.gaussian_blur_slider.place(x=250, y=730)

        # Create a browse button for Pre-Recorded Videos
        self.start_processing_nutton = tk.Button(self.options_frame, text="Restore Default Settings", font=("Arial", 12, "bold"), command=self.restore_default_settings)
        self.start_processing_nutton.configure(bg="dark blue", fg="white")
        self.start_processing_nutton.place(x=272, y=835)

        # Create a browse button for Pre-Recorded Videos
        self.start_processing_nutton = tk.Button(self.options_frame, text="Start Processing", font=("Arial", 12, "bold"), command=self.start_processing)
        self.start_processing_nutton.configure(bg="dark green", fg="white")
        self.start_processing_nutton.place(x=576, y=835)

        # Create a browse button for Pre-Recorded Videos
        self.stop_processing_nutton = tk.Button(self.options_frame, text="Stop Processing", font=("Arial", 12, "bold"), command=self.stop_processing)
        self.stop_processing_nutton.configure(bg="dark red", fg="white")
        self.stop_processing_nutton.place(x=38, y=835)

        # Start the GUI loop
        self.window.mainloop()

    def start_processing(self):
       
        global is_processing, selected_model, model_config_path, checkpoint_model_path, label_map_path
        
        if is_processing == False:
        
            selected_model_architecture = self.model_architecture_combobox.get()

            if selected_model_architecture == "SSD M-Net V2 FPN Keras 320x320 (High Speed | Low Accuracy)":

                model_config_path =  f'assets/models/ssd-m-net-v2-fpn-keras-320x320-(high-speed-low-accuracy)/pipeline.config'                
                checkpoint_model_path   =  f'assets/models/ssd-m-net-v2-fpn-keras-320x320-(high-speed-low-accuracy)/checkpoint/ckpt-0'     
                label_map_path    =  f'assets/label-maps/custom-label-map.pbtxt'

            elif selected_model_architecture == "SSD M-Net V2 Keras 320x320 (Medium Speed | Medium Accuracy)":

                model_config_path =  f'assets/models/ssd-m-net-v2-keras-320x320-(medium-speed -medium-accuracy)/pipeline.config'                
                checkpoint_model_path   =  f'assets/models/ssd-m-net-v2-keras-320x320-(medium-speed -medium-accuracy)/checkpoint/ckpt-0'     
                label_map_path    =  f'assets/label-maps/mscoco-label-map.pbtxt'
            
            elif selected_model_architecture == "SSD M-Net V2 FPN LITE 320x320 (Medium Speed | High Accuracy)": 
                
                model_config_path =  f'assets/models/ssd-m-net-v2-fpn-lite-320x320-(medium-speed-high-accuracy)/pipeline.config'                
                checkpoint_model_path   =  f'assets/models/ssd-m-net-v2-fpn-lite-320x320-(medium-speed-high-accuracy)/checkpoint/ckpt-0'     
                label_map_path    =  f'assets/label-maps/mscoco-label-map.pbtxt' 

            elif selected_model_architecture == "SSD M-Net V2 FPN LITE 640x640 (Low Speed | High Accuracy)":
                
                model_config_path =  f'assets/models/ssd-m-net-v2-fpn-lite-640x640-(low-speed-high-accuracy)/pipeline.config'                
                checkpoint_model_path   =  f'assets/models/ssd-m-net-v2-fpn-lite-640x640-(low-speed-high-accuracy)/checkpoint/ckpt-0'     
                label_map_path    =  f'assets/label-maps/mscoco-label-map.pbtxt'
            
            elif selected_model_architecture == "SSD M-Net V1 FPN 640x640 (Low Speed | High Accuracy)": 
                
                model_config_path =  f'assets/models/ssd-m-net-v1-fpn-640x640-(low-speed-high-accuracy)/pipeline.config'                
                checkpoint_model_path   =  f'assets/models/ssd-m-net-v1-fpn-640x640-(low-speed-high-accuracy)/checkpoint/ckpt-0'     
                label_map_path    =  f'assets/label-maps/mscoco-label-map.pbtxt'


            input_source = ""
            input_source_testing_passed = False

            print(self.device_camera_combo["state"]) # It is a bug, If I don't print it, it does not work in the if condition.

            if self.device_camera_combo["state"] == "readonly":
                
                selected_value= self.device_camera_combo.get()

                if selected_value != "":
                    first_part = selected_value.split(":")[0].strip()
                    input_source = re.findall(r'\d+', first_part)[0]
                     
                else:
                    messagebox.showerror("Error", "Please choose a camera")

            elif self.ip_camera_text['state'] == "normal":

                selected_value= self.ip_camera_text.get()

                if selected_value != "":
                    input_source = selected_value
                else:
                    messagebox.showerror("Error", "Please provide an IP address")

            elif self.file_path_text['state'] == "normal":

                selected_value= self.file_path_text.get()

                if selected_value != "":
                    input_source = selected_value
                else:
                    messagebox.showerror("Error", "Please choose a video file")


            if self.device_camera_combo["state"] == "readonly":

                test_cap = cv2.VideoCapture(int(input_source))

                if not test_cap.isOpened():
                    messagebox.showerror("Error", "The target webcam camera failed to open.")
                    input_source_testing_passed = False
                else:
                    self.vid = cv2.VideoCapture(int(input_source))
                    input_source_testing_passed = True

            elif self.ip_camera_text["state"] == "normal":
                test_cap = cv2.VideoCapture(input_source)

                if not test_cap.isOpened():
                    messagebox.showerror("Error", "The target IP camera failed to open.")
                    input_source_testing_passed = False
                else:
                    self.vid = cv2.VideoCapture(input_source)
                    input_source_testing_passed = True

            elif self.file_path_text["state"] == "normal":
                test_cap = cv2.VideoCapture(input_source)

                if not test_cap.isOpened():
                    messagebox.showerror("Error", "The chosen file failed to open.")
                    input_source_testing_passed = False
                else:
                    self.vid = cv2.VideoCapture(input_source)
                    input_source_testing_passed = True
            

            if input_source_testing_passed == True:

                is_processing = True

                load_model_function(model_config_path, checkpoint_model_path, label_map_path)
                self.camera_window.place(x=30, y=30)
                self.model_architecture_combobox.configure(state="disabled")
                self.camera_placeholder_label.place_forget()
                self.delay = 15 # milliseconds
                self.update()
                self.job_id = ""
            else:
                messagebox.showerror("Error", "Invalid input source. Please provide a valid image or video file to proceed.")  
        else:
             messagebox.showerror("Process Initialization Failed ", "A processing function is currently active. Please stop the current process to initiate a new process.")

    def stop_processing(self):
        global is_processing, number_of_time_detected

        if is_processing == True:

             is_processing = False

             number_of_time_detected = 0 # Set it to count from 0
             self.camera_window.place_forget()
             self.model_architecture_combobox.configure(state="normal")
             self.camera_placeholder_label.place(x=30, y=30)
             self.window.after_cancel(self.job_id)
         
             if self.vid.isOpened():
                self.vid.release()
                
    def switch_on_off_function(self):

        if self.switch_status == True:
            self.switch_status = False 
            self.sound_effects_combobox.config(state='disabled')
            self.on_button.config(image = self.off_button_image)            
        else:
            self.switch_status = True 
            self.sound_effects_combobox.config(state='normal')
            self.on_button.config(image = self.on_button_image) 

    def detect_fn(self, image):
        global global_detection_model

        image, shapes = global_detection_model.preprocess(image)
        prediction_dict = global_detection_model.predict(image, shapes)
        detections = global_detection_model.postprocess(prediction_dict, shapes)

        return detections, prediction_dict, tf.reshape(shapes, [-1])

    def alarm_sound_effect_function(self):
        global is_audio_playing, is_processing, is_sound_effect_changed

        selected_sound_effect = self.sound_effects_combobox.get()
        sound_effect_path = ""

        if selected_sound_effect == "Buzzing Bees Sound":
           sound_effect_path = 'assets\\music\\alarm-sound-effects\\0-bees-sound-effect.mp3'

        elif selected_sound_effect == "Firecrackers Sound":
            sound_effect_path = 'assets\\music\\alarm-sound-effects\\1-firecrackers-sound-effect.mp3'

        elif selected_sound_effect == "Warning Alarm Sound":
            sound_effect_path = 'assets\\music\\alarm-sound-effects\\2-warning-alarm.mp3'

        pygame.mixer.music.load(sound_effect_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            if is_processing == True:

                if is_sound_effect_changed == False:

                    if self.switch_status == True:
                        pygame.mixer.music.set_volume(1.0) 
                    else:
                        pygame.mixer.music.set_volume(0.0) # Mute
                else:
                    break
            else:
                pygame.mixer.music.stop()
                break

        if is_processing == False and is_sound_effect_changed == False:
            is_audio_playing = False

        elif is_processing == True and is_sound_effect_changed == False:
            is_audio_playing = False

        elif is_processing == True and is_sound_effect_changed == True: # On Audio Change
            is_audio_playing = True

    def on_sound_effect_change(self, event):
        global is_sound_effect_changed, is_processing, is_audio_playing

        if is_processing == True and is_audio_playing == True:
            if is_sound_effect_changed == False:
                is_sound_effect_changed = True
                alarm_sound_effect_function = threading.Thread(target = self.alarm_sound_effect_function, args=(), daemon=True)
                alarm_sound_effect_function.start()
                is_sound_effect_changed = False

    def on_threshold_change(self, val):
        self.detection_threshold =  val

    def set_brightness(self, val):
        self.brightness = int(val)
        
    def set_contrast(self, val):
        self.contrast = int(val)
        
    def set_blur(self, val):
        self.blur = int(val) 

    def restore_default_settings(self):
        self.brightness = 50
        self.contrast = 50
        self.blur = 0
        self.detection_threshold = 60
        self.switch_status = True 
        
        self.sound_effects_combobox.config(state='normal')
        self.on_button.config(image = self.on_button_image) 
        self.model_architecture_combobox.current(4)
        self.threshold_slider.set(60)
        self.brightness_slider.set(50)
        self.contrast_slider.set(50)
        self.gaussian_blur_slider.set(0)
        self.sound_effects_combobox.current(0)

        self.ip_camera_text.delete(0, "end")
        self.file_path_text.delete(0, "end")

        self.device_camera_combo.configure(state="disabled")
        self.ip_camera_text.configure(state="disabled")
        self.file_path_text.configure(state="disabled")
        self.browse_button.configure(state="disabled")

    def on_model_architecture_change(self, event):

        selected_model_architecture = self.model_architecture_combobox.get()

        if selected_model_architecture == "SSD M-Net V2 FPN Keras 320x320 (High Speed | Low Accuracy)":
            self.threshold_slider.set(40)
            self.detection_threshold = 40

        elif selected_model_architecture == "SSD M-Net V2 Keras 320x320 (Medium Speed | Medium Accuracy)":
            self.threshold_slider.set(45)
            self.detection_threshold = 45
        
        elif selected_model_architecture == "SSD M-Net V2 FPN LITE 320x320 (Medium Speed | High Accuracy)":   
            self.threshold_slider.set(50)
            self.detection_threshold = 50

        elif selected_model_architecture == "SSD M-Net V2 FPN LITE 640x640 (Low Speed | High Accuracy)":    
            self.threshold_slider.set(55)
            self.detection_threshold = 55
        
        elif selected_model_architecture == "SSD M-Net V1 FPN 640x640 (Low Speed | High Accuracy)":     
            self.threshold_slider.set(60)
            self.detection_threshold = 60

    def snapshot_sound_effect_function(self):
        snap_sound = pygame.mixer.Sound('assets\\music\\system-sound-effects\\0-camera-shutter-click.mp3')
        snap_sound.play()

    def take_snapshots(self):
        global is_processing, global_variable_snapshot_frame

        if is_processing == True:

            snapshot_sound_effect_function = threading.Thread(target = self.snapshot_sound_effect_function, args=(), daemon=True)
            snapshot_sound_effect_function.start()

            current_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]
            cv2.imwrite(f"snapshots/{current_time_str}.jpg", global_variable_snapshot_frame)
        else:
            messagebox.showerror("Snapshot Capture Failed", "The processing function is not active. Please initiate the processing before taking a snapshot.")

    def get_all_cameras(self):
        i = 0
        while True:
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = int(cap.get(cv2.CAP_PROP_FPS))
                camera_name = f"Camera {i}: ({width}x{height}, {fps}fps)"
                self.device_camera_combo["values"] = (*self.device_camera_combo["values"], camera_name)
                cap.release()
                i += 1
            else:
                cap.release()
                break

    def update(self):

        global number_of_time_detected, alaram_threshold, is_audio_playing, global_variable_snapshot_frame

        if hasattr(self, 'vid'):
            # Get a frame from the video source
            ret, frame = self.vid.read()

            if ret:
                image_np_expanded = np.expand_dims(frame, axis=0)

                frame = cv2.convertScaleAbs(frame, alpha=(self.contrast / 50), beta=(self.brightness - 50))
                frame = cv2.GaussianBlur(frame, (self.blur*2+1, self.blur*2+1), 0)

                input_tensor = tf.convert_to_tensor(np.expand_dims(frame, 0), dtype=tf.float32)
                detections, predictions_dict, shapes = self.detect_fn(input_tensor)

                label_id_offset = 1
                image_np_with_detections = frame.copy()

                min_score_thresh = self.detection_threshold / 100.0 

                box_to_display_str_map = collections.defaultdict(list)
                box_to_color_map = collections.defaultdict(str)

                number_of_elephants = 0

                current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

                cv2.putText(image_np_with_detections, f'{current_time} ', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                for i in range(detections['detection_boxes'][0].numpy().shape[0]):

                    if detections['detection_scores'][0].numpy() is None or detections['detection_scores'][0].numpy()[i] > min_score_thresh:

                        box = tuple(detections['detection_boxes'][0].numpy()[i].tolist())

                        display_str = ""

                        if(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i] in six.viewkeys(global_category_index):
                            class_name = global_category_index[(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i]]['name']
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
                                alarm_sound_effect_function = threading.Thread(target = self.alarm_sound_effect_function, args=(), daemon=True)
                                alarm_sound_effect_function.start()

                                current_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]
                                cv2.imwrite(f"predictions/{current_time_str}.jpg", image_np_with_detections)
                                email_thread = threading.Thread(target=self.send_email, args=(("gunarakulan@gmail.com", "1234", "Batticaloa", "Loca", number_of_elephants)))
                                email_thread.start()
                                # Send SMS HERE

                            number_of_time_detected = 0


                global_variable_snapshot_frame = image_np_with_detections
                            

                final_frame = cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB)
                final_frame = cv2.resize(final_frame, (self.width, self.height))

                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(final_frame))
                self.camera_window.create_image(0, 0, image=self.photo, anchor=tk.NW)

                           
        self.job_id = self.window.after(self.delay, self.update)
        

    def browse_file(self):
        filetypes = (("Video Files", "*.mp4 *.avi"), ("All Files", "*.*"))
        filename = filedialog.askopenfilename(title="Select a File", filetypes=filetypes)

    def toggle_textbox(self, target):
        if target == "[DEVICE_CAMERA]":
          
            self.ip_camera_text.delete(0, "end")
            self.file_path_text.delete(0, "end")

            self.device_camera_combo.configure(state="readonly")
            self.ip_camera_text.configure(state="disabled")
            self.file_path_text.configure(state="disabled")
            self.browse_button.configure(state="disabled")

        elif target == "[IP_CAMERA]":
      
            self.ip_camera_text.delete(0, "end")
            self.file_path_text.delete(0, "end")

            self.device_camera_combo.configure(state="disabled")
            self.ip_camera_text.configure(state="normal")
            self.file_path_text.configure(state="disabled")
            self.browse_button.configure(state="disabled")

        elif target == "[VIDEO]":
    
            self.ip_camera_text.delete(0, "end")
            self.file_path_text.delete(0, "end")

            self.device_camera_combo.configure(state="disabled")
            self.ip_camera_text.configure(state="disabled")
            self.file_path_text.configure(state="normal")
            self.browse_button.configure(state="normal")

    def send_email(self,recipient_email, device_id, device_name, location, number_of_elephants):
        
        # Read the contents of the JSON file
        with open('assets/credentials/credentials.json', 'r') as file:
            contents = file.read()

        # Parse the JSON contents into a dictionary
        credentials = json.loads(contents)

        # Access the values of the 'google_smtp_server' key
        email = credentials['google_smtp_server']['email']
        password = credentials['google_smtp_server']['password']

        # email details
        email_sender = email
        email_password = password
        email_receiver = recipient_email
        email_subject = f'Warning: Human-Elephant Conflict Detected at {location}'

        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        email_body = f"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Human Element Conflict Early Warning</title>
            <style>
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    max-width: 600px;
                    margin: 20px auto;
                    font-family: Arial, sans-serif;
                    border: 2px solid #999;
                }}
                th, td {{
                    padding: 10px;
                    text-align: left;
                    border-bottom: 1px solid #999;
                }}
                th {{
                    background-color: #ddd;
                    font-weight: bold;
                    border-right: 1px solid #999;
                }}
            </style>
        </head>
        <body>
            <h1 style="text-align:center;">HECMS</h1>
            <hr>
            <h1>Human Element Conflict Early Warning</h1>
            <p>Dear Recipient Name,</p>
            <p>We are writing to inform you of a human element conflict incident that occurred on <span style='font-weight:bold; color:red;'>{current_date}</span> at <span style='font-weight:bold; color:red;'>{current_time}</span>. Our system detected a conflict at the following location:</p>
            <table>
                <tr>
                    <th>Device ID:</th>
                    <td>{device_id}</td>
                </tr>
                <tr>
                    <th>Device Name:</th>
                    <td>{device_name}</td>
                </tr>
                <tr>
                    <th>Location:</th>
                    <td>{location}</td>
                </tr>
                <tr>
                    <th>Number of Elephants:</th>
                    <td>{number_of_elephants}</td>
                </tr>
            </table>
            <p>Please review this information and take any necessary action to prevent future conflicts.</p>
            <p>Thank you,</p>
            <p>HECMS</p>
        </body>
        </html>
        """

        # create message object
        message = MIMEMultipart()
        message['From'] = email_sender
        message['To'] = email_receiver
        message['Subject'] = email_subject
        message.attach(MIMEText(email_body, 'html'))

        # create SMTP session
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        session = smtplib.SMTP(smtp_server, smtp_port)
        session.starttls()

        # login to email account
        session.login(email_sender, email_password)

        # send email
        text = message.as_string()
        session.sendmail(email_sender, email_receiver, text)
        session.quit()

        print('Email sent successfully')


    def browse_file(self):
        # Ask user to select a video file
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv;*.m4v;*.flv;*.mov;*.wmv;*.webm;*.mpg;*.mpeg;*.m2ts;*.mts;*.ts;*.vob;*.3gp;*.3g2;")])
    
        if file_path:
            # Set the file path in the entry widget
            self.file_path_text.delete(0, "end")
            self.file_path_text.insert(0, file_path)

    def __del__(self):
        # Release the video source when the object is destroyed
        if hasattr(self, 'vid') and self.vid.isOpened():
            self.vid.release()

    
# Create the application window
App(tk.Tk(), "HECMS - Monitoring System")
