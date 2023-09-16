import cv2
import joblib
import numpy as np
from utils import w2d
import json
# import face_recognition

__class_name_to_number = {}
__class_number_to_name = {}
__model = None




## Retriving Saved Model::
def load_artifacts():
    print("Loading Artifacts....... Start ")
    global __class_name_to_number
    global __class_number_to_name
    # will convert name to its corresponding number
    with open("./artifacts/class_dictionary.json","r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}

    global __model
    if __model is None:
        with open('./artifacts/saved_model.pkl','rb') as f:
            __model = joblib.load(f)
    print("Loading  saved artifacts.....!!! DONE..")


if __name__ == "__main__":
    load_artifacts()

    # Get a reference to webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        # These Files are haarcascade OPENCV to recognize face and eyes
        face_cascade = cv2.CascadeClassifier('./opencv/haarcascade/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('./opencv/haarcascade/haarcascade_eye.xml')
        if frame is None:
            pass
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x,y,w,h) in faces:

            roi_color = frame[y:y + h, x:x + w]
            scalled_raw_img = cv2.resize(roi_color, (32, 32))
            img_har = w2d(roi_color,'db1',5)
            scalled_img_har = cv2.resize(img_har, (32, 32))
            combined_img = np.vstack((scalled_raw_img.reshape(32*32*3,1),scalled_img_har.reshape(32*32,1)))
            combined_img = np.array(combined_img).reshape(len(combined_img),).astype(float)
            out = int(__model.predict([combined_img]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,__class_number_to_name[out],(x+5,y-5), font, 1, (255,255,255), 2)
            cv2.rectangle(frame,  (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()