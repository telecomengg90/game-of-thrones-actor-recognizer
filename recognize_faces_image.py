# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:04:26 2020

@author: Dell
"""

# USAGE

import face_recognition
import pickle
import cv2



# load the known faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open('encodings2.pickle', "rb").read())

# load the input image and convert it from BGR to RGB
image = cv2.imread(r'path\to\picture') 
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb,
	model='cnn')
encodings = face_recognition.face_encodings(rgb, boxes)

# initialize the list of names for each face detected
names = []

# loop over the facial embeddings
for encoding in encodings:
	# attempt to match each face in the input image to our known
	# encodings
	matches = face_recognition.compare_faces(data["encodings"],
		encoding)
	name = "Unknown"

	# check to see if we have found a match
	if True in matches:
		
		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts = {}

		
		for i in matchedIdxs:
			name = data["names"][i]
			counts[name] = counts.get(name, 0) + 1


		name = max(counts, key=counts.get)
	
	names.append(name)

# loop over the recognized faces
for ((top, right, bottom, left), name) in zip(boxes, names):
	
	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	y = top - 15 if top - 15 > 15 else top + 15
	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.75, (0, 255, 0), 2)


cv2.imshow("Image", image)
cv2.waitKey(0)