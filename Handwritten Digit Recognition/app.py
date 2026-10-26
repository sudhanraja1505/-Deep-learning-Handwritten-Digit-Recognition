import os
import uuid
import numpy as np
from flask import Flask, render_template, request
from PIL import Image, ImageOps
import tensorflow as tf
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "digit_model.keras")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = None
if os.path.exists(MODEL_PATH):
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
    except Exception as exc:
        print(f"Could not load model: {exc}")
else:
    print("No trained model found. Run: python train_model.py")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(path):
    image = Image.open(path).convert("L")
    image = ImageOps.fit(image, (28, 28))
    arr = np.asarray(image, dtype=np.float32)
    if arr.mean() > 127:
        arr = 255.0 - arr
    arr = arr / 255.0
    return arr.reshape(1, 28, 28, 1)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_url = None
    error = None
    if request.method == "POST":
        file = request.files.get("digit_image")
        if not file or file.filename == "":
            error = "Please choose an image first."
        elif not allowed_file(file.filename):
            error = "Supported formats: PNG, JPG, JPEG, WEBP, BMP."
        elif model is None:
            error = "The trained model is missing. Run python train_model.py and try again."
        else:
            filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)
            try:
                probabilities = model.predict(preprocess_image(path), verbose=0)[0]
                digit = int(np.argmax(probabilities))
                prediction = {"digit": digit, "confidence": float(probabilities[digit]) * 100}
                image_url = f"/static/uploads/{filename}"
            except Exception as exc:
                error = f"Could not analyze image: {exc}"
    return render_template("index.html", prediction=prediction, image_url=image_url, error=error)

@app.errorhandler(413)
def file_too_large(_error):
    return render_template("index.html", prediction=None, image_url=None,
                           error="Image too large. Maximum upload size is 5 MB."), 413

if __name__ == "__main__":
    app.run(debug=True)
