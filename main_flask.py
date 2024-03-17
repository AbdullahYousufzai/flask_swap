from flask import Flask, request, jsonify, render_template
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_photo_collage(image1_path, image2_path, output_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    image1 = cv2.resize(image1, (300, 300))
    image2 = cv2.resize(image2, (300, 300))

    collage = cv2.vconcat([image1, image2])

    cv2.imwrite(output_path, collage)

@app.route('/upload', methods=['POST'])
def upload_images():
    try:
        if 'image1' not in request.files or 'image2' not in request.files:
            return jsonify({"error": "No images found"}), 400

        image1 = request.files['image1']
        image2 = request.files['image2']

        if image1.filename == '' or image2.filename == '':
            return jsonify({"error": "No images selected for uploading"}), 400

        image1_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image1.filename))
        image2_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image2.filename))
        collage_path = os.path.join(app.config['UPLOAD_FOLDER'], 'collage.jpg')

        image1.save(image1_path)
        image2.save(image2_path)

        create_photo_collage(image1_path, image2_path, collage_path)

        # jsonify({"collage_url": collage_path}), 200
        return render_template('swap_page.html')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
