#import os and io
import os, io
#importing the vision from google.cloud
from google.cloud import vision
#import type from google.cloud.viosion_v1
from google.cloud.vision_v1 import types
#importing pandas as pd
import pandas as pd
#importing draw vertices
from draw_vertices import drawVertices
# set the enviroment variable 'GOOGLE_APPLICATION_CREDENTIALS' to the file paths of the json file that contain serivice account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'helpful-data-342913-200a20202c91.json'
#creating the client instance for vision.ImageAnnototorClient
client = vision.ImageAnnotatorClient()
# reading the file from in file_name
file_name = 'img_01.png'
#reading the image
image_folder = './images/'
#variable to store image_path
image_path = os.path.join(image_folder, file_name)
#opening image from image path and rename as image_file
with io.open(image_path, 'rb') as image_file:
    #reading the image file and storing it into content variable
    content = image_file.read()
#creating a image object
image = types.Image(content=content)
#creating a object for logo_detection method
response = client.logo_detection(image=image)
#creating a object for logo_annotations
logos = response.logo_annotations
# iterating over the logos
for logo in logos:
    #printing the logo description
    print('Logo Description:', logo.description)
    #printing the confidence score
    print('Confidence Score:', logo.score)
    #printinf the *50
    print('-'*50)
    # print the boundary for logo with the help of draw vertices
    vertices = logo.bounding_poly.vertices
    #printing the vertices value
    print('Vertices Values {0}'.format(vertices))
    #calling to draw_vertices function
    drawVertices(content, vertices, logo.description)