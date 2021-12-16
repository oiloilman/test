from PIL import Image
import cv2
import numpy as np
import requests
image=Image.open(requests.get("https://previews.123rf.com/images/darrenwhi/darrenwhi1310/darrenwhi131000024/24022179-photo-of-many-cars-with-one-a-different-color.jpg", stream=True).raw)
#image =resize((420,250))

image_array=np.array(image)
image 
