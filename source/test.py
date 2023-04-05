import tkinter as tk
from tkinter import ttk
import cv2

def get_cameras():
    """
    Returns a list of connected cameras with their names and indices
    """
    cameras = []
    for i in range(20):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            camera_name = f"Camera: {i} |({width}x{height}, {fps}fps)"
            cameras.append((camera_name, i))
        cap.release()

def open_camera():
    """
    Opens the camera selected in the combo box
    """
    selected_camera = combo_box.get()
    print(combo_box.getvar("value"))
    camera_index = int(combo_box.getvar("value"))
    cap = cv2.VideoCapture(camera_index)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) == 27:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()

cameras = get_cameras()

combo_box = tk.ttk.Combobox(root, values=cameras, textvariable=tk.StringVar())
combo_box.pack()

open_button = tk.Button(root, text="Open Camera", command=open_camera)
open_button.pack()

root.mainloop()
