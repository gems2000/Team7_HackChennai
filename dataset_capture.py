# Import OpenCV2 for image processing
import cv2
#Import os for working with files
import os
#define a function
def assure_path_exists(path):
    #gives current working directory
    dir = os.path.dirname(path)   
    if not os.path.exists(dir):
        #create directory if it doesn't exist
        os.makedirs(dir)          
face_id=input('enter your id')
# Start capturing video with computer's inbuilt webcam
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize sample face image
count = 0
#calling function for checking dataset diretory
assure_path_exists("dataset/")

