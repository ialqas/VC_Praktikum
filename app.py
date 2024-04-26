
from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from PIL import Image, ExifTags


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])

def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename('analyseFile.jpg'))) # Then save the file
        exif_data, analyzed_image = analyse()
        return render_template('index.html', form=form, exif_data=exif_data, image_path=analyzed_image)
    return render_template('index.html', form=form)

def analyse():
    # Perform your analysis on the image here
    # For example, you can use OpenCV or PIL to analyze the image
    # extract EXIF data
    
    img = Image.open('static/files/analyseFile.jpg')
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    
    exportString = ""
    
    for i in exif.keys():
            exportString += f"{i}: {exif[i]}\n "
            
    
    img_black_white = img.convert('1')
    
    
    img_black_white.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/files/analyseFile.jpg'))

    return exportString, 'static/files/analyseFile.jpg'

#Method to get the image, is used in the index.html file
@app.route('/get-image/<path:image_path>')
def get_image(image_path):
    return send_file(image_path)
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
