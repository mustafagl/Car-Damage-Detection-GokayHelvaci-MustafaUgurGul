from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import os
from Predictor import ImagePredictor

image_predictor = ImagePredictor("models/keras.model")

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def resize_image(image_path):
    with Image.open(image_path) as img:
        img_resized = img.resize((256, 256))
        img.save(image_path)

def process_image(image_path, processed_path):
    image_predictor.process_and_save_image(image_path, processed_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        resize_image(file_path)
        processed_filename = 'processed_' + filename
        processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        process_image(file_path, processed_path)
        return render_template('index.html', filename=filename, processed_filename=processed_filename)
    return redirect(request.url)

@app.route('/uploads/display/<filename>')
def display_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host="0.0.0.0",port=80,debug=True)
