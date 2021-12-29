# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:23:16 2020

@author: hp
"""

import numpy as np
import tensorflow as tf
import cv2
import object_detection.visualization_utils as vis_util
import collections
import six
import smtplib, ssl
from playsound import playsound
import threading
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


number_of_time_detected = 0
alaram_threshold = 2


def PlayAlarm():
    global alaram_threshold, number_of_time_detected
    playsound("warning_alarm.mp3")
    number_of_time_detected = 0



STANDARD_COLORS = [
    'AliceBlue', 'Chartreuse', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque',
    'BlanchedAlmond', 'BlueViolet', 'BurlyWood', 'CadetBlue', 'AntiqueWhite',
    'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan',
    'DarkCyan', 'DarkGoldenRod', 'DarkGrey', 'DarkKhaki', 'DarkOrange',
    'DarkOrchid', 'DarkSalmon', 'DarkSeaGreen', 'DarkTurquoise', 'DarkViolet',
    'DeepPink', 'DeepSkyBlue', 'DodgerBlue', 'FireBrick', 'FloralWhite',
    'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod',
    'Salmon', 'Tan', 'HoneyDew', 'HotPink', 'IndianRed', 'Ivory', 'Khaki',
    'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue',
    'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey',
    'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue',
    'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime',
    'LimeGreen', 'Linen', 'Magenta', 'MediumAquaMarine', 'MediumOrchid',
    'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen',
    'MediumTurquoise', 'MediumVioletRed', 'MintCream', 'MistyRose', 'Moccasin',
    'NavajoWhite', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed',
    'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed',
    'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple',
    'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Green', 'SandyBrown',
    'SeaGreen', 'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue',
    'SlateGray', 'SlateGrey', 'Snow', 'SpringGreen', 'SteelBlue', 'GreenYellow',
    'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
    'WhiteSmoke', 'Yellow', 'YellowGreen'
]


def send_mail_function(date, time, number_of_elephant):

    try:
        sender_email = "machinealpha9@gmail.com"
        receiver_email = "gunarakulan@gmail.com"
        password = "machinealpha123456789"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Wraning Alram"
        message["From"] = sender_email
        message["To"] = receiver_email

        last_sentance = ""

        if int(number_of_elephant) == 1:
            last_sentance = "There is <span style='color:red; font-weight:bold;'> only one elephant </span> was found."

        else:
            last_sentance = "There are <span style='color:red; font-weight:bold;'> {} elephants </span> were found.".format(number_of_elephant)

        subject_text = """
                <html>
                <title>Web Page Design</title>
                <head>
                </head>
                <body>

                    <h1 style='color:red; text-align:center;'>Warning!.. Warning!..</h1>
                    <h2 style='text-align:center;'>Elephant Intrusion Detected</h2>
                    
                    <h3>Date:- {}</h3>
                    <h3>Time:- {}</h3>
                    
                    <p>This alert message was reported by automatic elephant intrusion detection system. The device ID is 124HHG. The alert message was received from [Place_Name] area. {} Try to protect the area before the incident take place.</p>
                    
                    <p>Thank you!</p>
                    
                    <p style='text-align:center;color:blue;'>Developed by GR-Technologies</p>

                </body>
                </html>
            """.format(date, time, last_sentance)

        subject_text = MIMEText(subject_text, "html")
        message.attach(subject_text)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print("Wraning message was sent successfully!") 

    except Exception as e:
        print(e)





def create_category_index(label_path='coco_ssd_mobilenet/labelmap.txt'):
    """
    To create dictionary of label map

    Parameters
    ----------
    label_path : string, optional
        Path to labelmap.txt. The default is 'coco_ssd_mobilenet/labelmap.txt'.

    Returns
    -------
    category_index : dict
        nested dictionary of labels.

    """
    f = open(label_path)
    category_index = {}
    for i, val in enumerate(f):
        if i != 0:
            val = val[:-1]
            if val != '???':
                category_index.update({(i-1): {'id': (i-1), 'name': val}})
            
    f.close()
    return category_index
def get_output_dict(image, interpreter, output_details, nms=True, iou_thresh=0.5, score_thresh=0.6):
    """
    Function to make predictions and generate dictionary of output

    Parameters
    ----------
    image : Array of uint8
        Preprocessed Image to perform prediction on
    interpreter : tensorflow.lite.python.interpreter.Interpreter
        tflite model interpreter
    input_details : list
        input details of interpreter
    output_details : list
    nms : bool, optional
        To perform non-maximum suppression or not. The default is True.
    iou_thresh : int, optional
        Intersection Over Union Threshold. The default is 0.5.
    score_thresh : int, optional
        score above predicted class is accepted. The default is 0.6.

    Returns
    -------
    output_dict : dict
        Dictionary containing bounding boxes, classes and scores.

    """
    output_dict = {
                   'detection_boxes' : interpreter.get_tensor(output_details[0]['index'])[0],
                   'detection_classes' : interpreter.get_tensor(output_details[1]['index'])[0],
                   'detection_scores' : interpreter.get_tensor(output_details[2]['index'])[0],
                   'num_detections' : interpreter.get_tensor(output_details[3]['index'])[0]
                   }

    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    if nms:
        output_dict = apply_nms(output_dict, iou_thresh, score_thresh)
    return output_dict

def apply_nms(output_dict, iou_thresh=0.5, score_thresh=0.6):
    """
    Function to apply non-maximum suppression on different classes

    Parameters
    ----------
    output_dict : dictionary
        dictionary containing:
            'detection_boxes' : Bounding boxes coordinates. Shape (N, 4)
            'detection_classes' : Class indices detected. Shape (N)
            'detection_scores' : Shape (N)
            'num_detections' : Total number of detections i.e. N. Shape (1)
    iou_thresh : int, optional
        Intersection Over Union threshold value. The default is 0.5.
    score_thresh : int, optional
        Score threshold value below which to ignore. The default is 0.6.

    Returns
    -------
    output_dict : dictionary
        dictionary containing only scores and IOU greater than threshold.
            'detection_boxes' : Bounding boxes coordinates. Shape (N2, 4)
            'detection_classes' : Class indices detected. Shape (N2)
            'detection_scores' : Shape (N2)
            where N2 is the number of valid predictions after those conditions.

    """
    q = 90 # no of classes
    num = int(output_dict['num_detections'])
    boxes = np.zeros([1, num, q, 4])
    scores = np.zeros([1, num, q])
    # val = [0]*q
    for i in range(num):
        # indices = np.where(classes == output_dict['detection_classes'][i])[0][0]
        boxes[0, i, output_dict['detection_classes'][i], :] = output_dict['detection_boxes'][i]
        scores[0, i, output_dict['detection_classes'][i]] = output_dict['detection_scores'][i]
    nmsd = tf.image.combined_non_max_suppression(boxes=boxes,
                                                 scores=scores,
                                                 max_output_size_per_class=num,
                                                 max_total_size=num,
                                                 iou_threshold=iou_thresh,
                                                 score_threshold=score_thresh,
                                                 pad_per_class=False,
                                                 clip_boxes=False)
    valid = nmsd.valid_detections[0].numpy()
    output_dict = {
                   'detection_boxes' : nmsd.nmsed_boxes[0].numpy()[:valid],
                   'detection_classes' : nmsd.nmsed_classes[0].numpy().astype(np.int64)[:valid],
                   'detection_scores' : nmsd.nmsed_scores[0].numpy()[:valid],
                   }
    return output_dict

def make_and_show_inference(img, interpreter, input_details, output_details, category_index, nms=True, score_thresh=0.6, iou_thresh=0.5):
    global number_of_time_detected
    """
    Generate and draw inference on image

    Parameters
    ----------
    img : Array of uint8
        Original Image to find predictions on.
    interpreter : tensorflow.lite.python.interpreter.Interpreter
        tflite model interpreter
    input_details : list
        input details of interpreter
    output_details : list
        output details of interpreter
    category_index : dict
        dictionary of labels
    nms : bool, optional
        To perform non-maximum suppression or not. The default is True.
    score_thresh : int, optional
        score above predicted class is accepted. The default is 0.6.
    iou_thresh : int, optional
        Intersection Over Union Threshold. The default is 0.5.

    Returns
    -------
    NONE
    """
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.resize(img_rgb, (300, 300), cv2.INTER_AREA)
    img_rgb = img_rgb.reshape([1, 300, 300, 3])

    interpreter.set_tensor(input_details[0]['index'], img_rgb)
    interpreter.invoke()
    
    output_dict = get_output_dict(img_rgb, interpreter, output_details, nms, iou_thresh, score_thresh)
    # Visualization of the results of a detection.

    min_score_thresh = 0.50

    box_to_display_str_map = collections.defaultdict(list)
    box_to_color_map = collections.defaultdict(str)

    number_of_items = 0

    for i in range(output_dict['detection_boxes'].shape[0]):

        if output_dict['detection_scores'] is None or output_dict['detection_scores'][i] > min_score_thresh:
            box = tuple(output_dict['detection_boxes'][i].tolist())
            
            display_str = ''

            if (output_dict['detection_classes']).astype(int)[i] in six.viewkeys(category_index):

                class_name = category_index[(output_dict['detection_classes']).astype(int)[i]]['name']
                display_str = str(class_name)
                display_str = '{}: {}%'.format(display_str, round(100*output_dict['detection_scores'][i]))

                box_to_display_str_map[box].append(display_str)

                box_to_color_map[box] = STANDARD_COLORS[(output_dict['detection_classes']).astype(int)[i] % len(STANDARD_COLORS)]

                if "elephant" in box_to_display_str_map[box][0]:
                    number_of_items = number_of_items + 1




    im_width, im_height = img.shape[1::-1]


    for box, color in box_to_color_map.items():
        
        ymin, xmin, ymax, xmax = box

        ymin = ymin * im_height
        xmin = xmin * im_width
        ymax = ymax * im_height
        xmax = xmax * im_width

        x = xmin
        y = ymin
        w = xmax - xmin
        h = ymax - ymin

        if "elephant" in box_to_display_str_map[box][0]:

            cv2.rectangle(img, (int(x),int(y)), (int(x) + int(w), int(y) + int(h)), (0,0,255), 4)
            cv2.putText(img, "Elephant", (int(x) + int(w), int(y) + int(h)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1, cv2.LINE_AA)

            number_of_time_detected = number_of_time_detected + 1

            if number_of_time_detected == alaram_threshold:

                thread1 = threading.Thread(target = PlayAlarm)
                thread1.start()
            
                date = datetime.today().strftime('%Y-%m-%d')
                now = datetime.now()
                time = now.strftime('%I:%M:%S')

                if number_of_items != 0:
                    send_mail_function(date, time, str(number_of_items))


    '''
    vis_util.visualize_boxes_and_labels_on_image_array(
    img,
    output_dict['detection_boxes'],
    output_dict['detection_classes'],
    output_dict['detection_scores'],
    category_index,
    use_normalized_coordinates=True,
    min_score_thresh=score_thresh,
    line_thickness=3)

    '''

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="coco_ssd_mobilenet/detect_2.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

category_index = create_category_index()
input_shape = input_details[0]['shape']
cap = cv2.VideoCapture("test-video.mp4")

while(True):
    ret, img = cap.read()
    if ret:
        make_and_show_inference(img, interpreter, input_details, output_details, category_index)
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
