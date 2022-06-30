import face_recognition as fr

import cv2
import face_recognition
import numpy as np
from time import sleep
import urllib.request




def get_encoded_faces(faces):
    """
    looks through the faces encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}
    for fnames in faces:
	
        response = urllib.request.urlopen(faces[fnames])
        face = fr.load_image_file(response)
        encoding = fr.face_encodings(face)[0]
        encoded[fnames] = encoding
        
    return encoded

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

def classify_face(im, urlFaces):
    """
    will find all of the faces in a given image and label
    them if it knows what they are
    :return: list of face names
    """
    faces = get_encoded_faces(urlFaces)
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())
    # get image from url 
    
    img = url_to_image(im)
 
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
  
    return face_names


