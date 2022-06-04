#import os and io
import os, io
#import type from google.cloud.viosion_v1
from google.cloud.vision_v1 import types
#importing the vision from google.cloud
from google.cloud import vision
#importing pandas as pd
import pandas as pd
# set the enviroment variable 'GOOGLE_APPLICATION_CREDENTIALS' to the file paths of the json file that contain serivice account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'helpful-data-342913-200a20202c91.json'
#creating the client instance for vision.ImageAnnototorClient
client = vision.ImageAnnotatorClient()
# reading the file from in file_name
file_name = 'img_03.jpg'
#storing the image path in variable
image_path = f'.\Images\{file_name}'
#opening image from image path and rename as image_file
with io.open(image_path, 'rb') as image_file:
    #reading the image file and storing it into content variable
    content = image_file.read()
#creating a image object
image = types.Image(content=content)
#creating a object for logo_detection method
response = client.face_detection(image=image)
#calling to face_detection function and stroing the returning value into variable
faceAnnotations = response.face_annotations
# making a touple for result
likehood = ('Unknown', 'Very Unlikely', 'Unlikely', 'Possibly', 'Likely', 'Very Likely')
#printing faces
print('Faces:')
#iterating over FaceAnnotations
for face in faceAnnotations:
    #printing the confidence
    print('Detection Confidence {0}'.format(face.detection_confidence))
    #printing the angryness
    print('Angry likelyhood: {0}'.format(likehood[face.anger_likelihood]))
    # printing the joy value
    print('Joy likelyhood: {0}'.format(likehood[face.joy_likelihood]))
    # printing the sorrow value of face Expression
    print('Sorrow likelyhood: {0}'.format(likehood[face.sorrow_likelihood]))
    #printing the surprised value
    print('Surprised ikelihood: {0}'.format(likehood[face.surprise_likelihood]))
    #printing the Headwear value
    print('Headwear likelyhood: {0}'.format(likehood[face.headwear_likelihood]))
    #printing the face_vertices value
    face_vertices = ['({0},{1})'.format(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
    #printing the face_bound value
    print('Face bound: {0}'.format(', '.join(face_vertices)))
    #printing the space
    print('')