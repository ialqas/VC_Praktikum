from flask import Flask, render_template, request
import cv2
import numpy as np
from PIL import Image, ExifTags


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'picture' not in request.files:
        return "No picture uploaded", 400

    picture = request.files['picture']
    nparr = np.frombuffer(picture.read(), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Perform your analysis on the image here
    # For example, you can use OpenCV or PIL to analyze the image
    # extract EXIF data
    img = Image.open('image0.jpeg')
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    
    exportString = ""
    
    for i in exif.keys():
            exportString += f"{i}: {exif[i]}\n "

    # For demonstration, let's just return the dimensions of the image
    height, width, _ = image.shape
    analysis_result = f"Image dimensions: {width}x{height}"
    result = exportString + ", " + analysis_result

    return result

if __name__ == '__main__':
    app.run(debug=True)
