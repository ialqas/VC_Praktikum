import base64
from PIL import Image
import io
import cv2
import numpy as np
import matplotlib.pyplot as plt
from decodeb64_to_img import stringToRGB

# Take in cv image and return base64 string
def rgbToString(img):
    _, im_arr = cv2.imencode('.jpg', img)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    result = "data:image/png;base64," + im_b64.decode("utf-8")
    #could resolve to an error, by using png alwas - maybe fix later
    return result