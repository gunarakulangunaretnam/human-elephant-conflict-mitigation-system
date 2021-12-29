import os
import tarfile
import threading
import urllib.request
import six
from playsound import playsound
import collections
import smtplib, ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


PATH_TO_LABELS = os.path.join("inference_graph/labelmap.pbtxt")


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import config_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file("inference_graph/pipeline.config")
model_config = configs['model']
detection_model = model_builder.build(model_config=model_config, is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join('inference_graph/checkpoint/', 'ckpt-0')).expect_partial()

@tf.function
def detect_fn(image):
    """Detect objects in image."""

    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)

    return detections, prediction_dict, tf.reshape(shapes, [-1])



def send_mail_function(date, time, number_of_elephant):

	try:
		sender_email = "sender_email@gmail.com"
		receiver_email = "receiver_email@gmail.com"
		password = "sender_email_passwrod"

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




category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)


import cv2

cap = cv2.VideoCapture("test-video.mp4")


import numpy as np


number_of_time_detected = 0
alaram_threshold = 2


def PlayAlarm():
	global alaram_threshold, number_of_time_detected
	playsound("warning_alarm.mp3")
	number_of_time_detected = 0


while True:
    # Read frame from camera
    ret, image_np = cap.read()

    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections, predictions_dict, shapes = detect_fn(input_tensor)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()

    min_score_thresh = 0.40


    box_to_display_str_map = collections.defaultdict(list)
    box_to_color_map = collections.defaultdict(str)

    number_of_items = 0
    
    for i in range(detections['detection_boxes'][0].numpy().shape[0]):
    	
    	if detections['detection_scores'][0].numpy() is None or detections['detection_scores'][0].numpy()[i] > min_score_thresh:
    		
    		box = tuple(detections['detection_boxes'][0].numpy()[i].tolist())
    		
    		display_str = ''

    		

    		if (detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i] in six.viewkeys(category_index):
    			class_name = category_index[(detections['detection_classes'][0].numpy() + label_id_offset).astype(int)[i]]['name']
    			display_str = str(class_name)
    			display_str = '{}: {}%'.format(display_str, round(100*detections['detection_scores'][0].numpy()[i]))

    			box_to_display_str_map[box].append(display_str)
	
    			box_to_color_map[box] = "Red"

    			if "Elephant" in box_to_display_str_map[box][0]:
    				number_of_items = number_of_items + 1

    
    im_width, im_height = image_np.shape[1::-1]

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

    	box_color = (0,0,0)

    	if color == "Red":
    		box_color = (0, 0, 255)

    	
    	cv2.rectangle(image_np_with_detections, (int(x),int(y)), (int(x) + int(w), int(y) + int(h)), box_color, 4)
    	cv2.putText(image_np_with_detections, 'Elephant', (int(x), int(y)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

    	number_of_time_detected = number_of_time_detected + 1

    	if number_of_time_detected == alaram_threshold:

    		thread1 = threading.Thread(target = PlayAlarm)
    		thread1.start()

    		date = datetime.today().strftime('%Y-%m-%d')
    		now = datetime.now()
    		time = now.strftime('%I:%M:%S')

    		if number_of_items != 0:
    			send_mail_function(date, time, str(number_of_items))
    	
	# Display output
    cv2.imshow('object detection', cv2.resize(image_np_with_detections, (800, 600)))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()