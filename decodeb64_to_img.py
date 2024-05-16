import base64
from PIL import Image
import io
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Take in base64 string and return cv image
def stringToRGB(base64_string):
    #cut off String at ',' and take the second part
    base64_string = base64_string.split(',')[1]

    #convert to image
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return opencv_img