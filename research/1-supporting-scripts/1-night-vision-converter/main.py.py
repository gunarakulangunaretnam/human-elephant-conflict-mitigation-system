import os
import cv2
import numpy as np

folder_path = 'input-dataset/' 

index = 0

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    if img_gray is None:
        continue

    current_brightness = np.mean(img_gray)

    divider_value = 0

    if current_brightness <=70:
        divider_value = 1
    elif current_brightness >= 71 and current_brightness <=100:
        divider_value = 1.3
    elif current_brightness >= 101 and current_brightness <=150:
        divider_value = 2
    elif current_brightness >= 151 and current_brightness <=200:
        divider_value = 3
    elif current_brightness >= 201 and current_brightness <=250:
        divider_value = 4
    elif current_brightness >= 251 and current_brightness <=300:
        divider_value = 4.5
    elif current_brightness >= 301 and current_brightness <=350:
        divider_value = 5.3
    elif current_brightness >= 351 and current_brightness <=400:
        divider_value = 6.3
    elif current_brightness >= 401 and current_brightness <=450:
        divider_value = 7.1
    elif current_brightness >= 451 and current_brightness <=500:
        divider_value = 8.0
    elif current_brightness >= 501:
        divider_value = 10

    img = img_gray // divider_value

    print(f"{filename}: {index}")
    cv2.imwrite(f"output-data/{filename}", img)
    index = index + 1
