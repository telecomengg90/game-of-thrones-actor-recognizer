# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:29:48 2020

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:49:16 2020

@author: Dell
"""
import os
import cv2

base_dir=os.path.dirname(os.path.abspath('pic_size_changer'))
image_dir=os.path.join(base_dir,"dataset\sohaib")
images = []

for root,directories,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
         path=os.path.join(root,file)
         image=cv2.imread(str(path))
         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
         

         image = cv2.resize(image,(612,816))
         
         cv2.imwrite(os.path.join(root,file),image)
         images.append(image)
        
        
    

