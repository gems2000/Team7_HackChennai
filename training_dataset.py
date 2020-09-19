# Import OpenCV2 for image processing
import cv2
# Import os for working with files
import os
# Importing numpy for working with multi-dimensional arrays and matrices
import numpy as np 
#Importing image for opening, manipulating and saving images in different formats
from PIL import Image

#Using the LBPH algorithm
recognizer = cv2.face.LBPHFaceRecognizer_create()

#Using the haarcascade frontalface classifier
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    #getting the path of all files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #creating a empty list for
    faceSamples=[]
    #creating a empty list for ID
    Ids=[]
    #looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    #returning the faceSamples and Ids
    return faceSamples,Ids

