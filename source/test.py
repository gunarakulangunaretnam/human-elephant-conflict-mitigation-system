import cv2

# set IP address and port number of depth camera server
ip_address = "192.168.8.171"
port = "5000"

# set video stream URL
url = "http://{}:{}/stream.mjpg".format(ip_address, port)

# create VideoCapture object
cap = cv2.VideoCapture(url)

# check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

# read frames from the camera
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # display the resulting frame
        cv2.imshow('iVCAM Stream', frame)

        # press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
