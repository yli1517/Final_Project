import os
import tensorflow as tf
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from keras.preprocessing.image import img_to_array, load_img
import numpy as np


UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads/')

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = tf.keras.models.load_model('sour_patch_vgg16_model.h5')

def allowed_file(filename):
    return ('.' in filename and 
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            prediction = make_prediction('uploads/' + filename)
            return '''
                <!doctype html>
                <title>Prediction Results</title>
                <h1>Result:</h1>
                <h2>{}</h2>
                <img src='uploads/{}' </img>
                </form>
                '''.format(prediction, filename)

             
            
            #return render_template("index.html", user_image = 'uploads/' + filename)
            #return prediction
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))
    return '''
    <!doctype html>
    <title>Pneumonia Prediction</title>
    <h1>X-ray Image Classification for Pneumonia</h1>
    <h2>Upload your x-ray image</h2>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


def make_prediction(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img_tensor = img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    classes = model.predict(img_tensor)
    for img_class in classes:
        if img_class <= 0.6:
            prediction = "Predicted class: Pneumonia"
        else:
            prediction = "Predicted class: Normal"
    return prediction

    

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads/', filename)
