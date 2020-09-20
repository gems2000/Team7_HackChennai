# Import OpenCV2 for image processing
import cv2
#Import os for working with files
import os
#importing writer from csv to write into csv file
from csv import writer
#define a function
def assure_path_exists(path):
    #gives current working directory
    dir = os.path.dirname(path)   
    if not os.path.exists(dir):
        #create directory if it doesn't exist
        os.makedirs(dir)          

#Taking the id of the user
face_id=input('enter your id')

#Taking the name of the user
name=input('enter your name')

#Values to be provided in the rows
rows = [face_id,name]

# Name of the file
filename = "data.csv"

#Opening the csv file to write upon
with open('data.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(rows)


# Start capturing video with computer's inbuilt webcam
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize sample face image
count = 0
#calling function for checking dataset diretory
assure_path_exists("dataset/")
# Start looping
while(True):

    # start Capturing video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale for better accuracy
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle of face's size
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Increment sample face image
        count += 1

        # Save the captured image into the datasets folder with unique id
        cv2.imwrite("dataset/user." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms or press ctrl+c
    if cv2.waitKey(100) & 0xFF == ord('q'):
        #will end the loop
        break

    # If image taken reach 30, stop taking video
    elif count>=30:
        print("Successfully Captured")
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()

