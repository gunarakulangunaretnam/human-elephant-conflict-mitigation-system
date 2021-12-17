import os                                                                  # To Perform OS level works.
import six
import cv2                                                                 # OpenCV for Computer Vision
import labelcolors                                                         # It has a dictionary that contains colors for each label
import argparse                                                            # To get arguments
import collections
import numpy as np
import pyttsx3                                                             # To perform text to speech function
import threading                                                           # To perform multi-threading operations
import playsound                                                           # To play sounds
import tensorflow as tf                                                    # Main Library.
from object_detection.utils import label_map_util                          # To handle label map.
from object_detection.utils import config_util                             # To load model pipeline.
from object_detection.utils import visualization_utils as viz_utils        # To draw rectangles.
from object_detection.builders import model_builder                        # To load & Build models.

ap = argparse.ArgumentParser()                                                                          # Create argparse object
ap.add_argument("-m", "--model_name", required=True, help="Name of the model")                          # Create model_name argument
ap.add_argument("-l", "--labels", required=True, help="Labels that are needed to be detected")          # Create labels argument
ap.add_argument("-a", "--alarm", required=True, help="Alram status")                                    # Alarm required or not argument
ap.add_argument("-t", "--minimum_threshold", required=True, help="Minimum threshold of detection rate") # minimum_threshol
ap.add_argument("-s", "--source", required=True, help="Source of processing")                           # video / webcam
args = vars(ap.parse_args())                                                                            # Build argparse

#Text to speech setup.
engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"  # female
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"  # male
engine.setProperty('voice', en_voice_id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

alarm_text_to_speech_notes = ""

def load_alarm_text_to_speech_notes():
    global alarm_text_to_speech_notes

    if args["alarm"] == "[TRUE]":
        file = open('system-files//alarm-text-to-speech-notes.txt')
        alarm_text_to_speech_notes = file.readline().strip()
        

load_alarm_text_to_speech_notes()

def talk_function(text):               # Text to speech convertion
    print("Computer: {}".format(text))
    engine.say(text)
    engine.runAndWait()

number_of_time_detected = 0

def play_alarm():                     # Function to play sound
    global number_of_time_detected
    number_of_time_detected
    playsound.playsound("system-files//alarm.mp3")
    talk_function(alarm_text_to_speech_notes)
    number_of_time_detected = 0

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


processing_type = ""          		# Store processing type.
labels = []					  		# Store Labels in a list.


model_config_path =  f'data/models/{args["model_name"]}/pipeline.config'        # Store the path of config file
checkpoint_model_path   =  f'data/models/{args["model_name"]}/checkpoint/ckpt-0'      # Store the path of model
label_map_path    =  f'data/mscoco_label_map.pbtxt'                             # Store the path of label_map

if args['labels'] == "all_labels":

    processing_type = "all_labels"	# Change processing_type as all_labels

else:
    processing_type = "labels"      # Change as labels to perform


if processing_type == "labels":
    labels = args['labels'].split(",")    # Store given labels to the labels list.




# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(model_config_path)
model_config = configs['model']
detection_model = model_builder.build(model_config=model_config, is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(checkpoint_model_path).expect_partial()

@tf.function

def detect_fn(image):
    """Detect objects in image."""

    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)

    return detections, prediction_dict, tf.reshape(shapes, [-1])


category_index = label_map_util.create_category_index_from_labelmap(label_map_path,
                                                                    use_display_name=True)

video_source = "";

if str(args["source"]).split("|")[0] == "[WEBCAM]":

    video_source = int(args["source"].split("|")[1])

elif str(args["source"]).split("|")[0] == "[VIDEO]":

    video_source = str(args["source"].split("|")[1])

cap = cv2.VideoCapture(video_source)

while True:
    # Read frame from camera
    ret, image_np = cap.read()

    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)

    # Things to try:
    # Flip horizontally
    # image_np = np.fliplr(image_np).copy()

    # Convert image to grayscale
    # image_np = np.tile(
    #     np.mean(image_np, 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections, predictions_dict, shapes = detect_fn(input_tensor)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()

    min_score_thresh = int(f'{args["minimum_threshold"]}') / 100

    box_to_display_str_map = collections.defaultdict(list)
    box_to_color_map = collections.defaultdict(str)

    number_of_items = 0

    for i in range(detections['detection_boxes'][0].numpy().shape[0]):

    	if detections['detection_scores'][0].numpy() is None or detections['detection_scores'][0].numpy()[i] > min_score_thresh:

            box = tuple(detections['detection_boxes'][0].numpy()[i].tolist())

            display_str = ""

            if(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i] in six.viewkeys(category_index):
                class_name = category_index[(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i]]['name']
                display_str = '{}'.format(class_name)
 

                box_to_display_str_map[box].append(display_str) # Join the number of eleements with label Name



    im_width, im_height = image_np.shape[1::-1]

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

    	if box_to_display_str_map[box][0].replace("_"," ") in labels: # Get only label name not the total number of items


            try: # Getting color from labelcolors.label_with_colors
                r = int(labelcolors.label_with_colors[box_to_display_str_map[box][0]].split(",")[0])
                g = int(labelcolors.label_with_colors[box_to_display_str_map[box][0]].split(",")[1])
                b = int(labelcolors.label_with_colors[box_to_display_str_map[box][0]].split(",")[2])

            except Exception as e:  # If suppose color is not found for the label, it will be assgined as red.
                r = 255
                g = 0
                b = 0


            if args["alarm"] == "[TRUE]":

                number_of_time_detected = number_of_time_detected + 1

                if number_of_time_detected == 20:
                    thread1 = threading.Thread(target = play_alarm)
                    thread1.start()

            cv2.rectangle(image_np_with_detections, (int(x),int(y)), (int(x) + int(w), int(y) + int(h)), (b, g, r), 4)

            (tw, th), _ = cv2.getTextSize(box_to_display_str_map[box][0], cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)

            # Prints the text.
            img = cv2.rectangle(image_np_with_detections, (int(x), int(y) - 30), (int(x) + 20 + tw, int(y)), (b, g, r), -1)
            img = cv2.putText(image_np_with_detections, box_to_display_str_map[box][0].upper(), (int(x)+5, int(y) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)


    # Display output
    cv2.imshow('object detection', cv2.resize(image_np_with_detections, (800, 600)))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
