import cv2
import os

folder_path = "input-videos/"
folder_path_output = "outputs/"

index = 0
for file_name in os.listdir(folder_path):
    if file_name.endswith((".mp4", ".avi", ".mov")):
        file_path = os.path.join(folder_path, file_name)
        cap = cv2.VideoCapture(file_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        time_counter = 0
    
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            time_counter += 1

            if time_counter == 3 * fps:

                cv2.imwrite(f"{folder_path_output}/image-{index}.jpg", frame)
                index = index +1
                print(f"image-{index} Saved!")

                time_counter = 0
        
        cap.release()
