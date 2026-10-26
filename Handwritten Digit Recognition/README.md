# Handwritten Digit Recognition Using Deep Learning

A beginner-friendly web application that recognizes handwritten digits from 0 to 9 using a Convolutional Neural Network (CNN) trained on the MNIST dataset.

## Features
- Responsive Flask web interface
- Upload an image containing one handwritten digit
- CNN training using the built-in MNIST dataset
- Prediction from 0 to 9 with a confidence score
- Image file type and size validation

## Technologies
Python, Flask, TensorFlow/Keras, NumPy, Pillow, HTML and CSS.

## Project Structure
```text
handwritten_digit_recognition/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── templates/index.html
├── static/style.css
├── static/uploads/
└── model/
```

## Setup on Windows
Use Python 3.11 (64-bit) in a virtual environment.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

For Command Prompt, activate with:
```bat
.venv\Scripts\activate.bat
```

Install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If TensorFlow installation fails, confirm the active Python version and 64-bit architecture:
```bash
python --version
python -c "import struct; print(struct.calcsize('P') * 8)"
```

## Train the Model
```bash
python train_model.py
```
Keras downloads the MNIST dataset on first run. The CNN is trained, evaluated, and saved to `model/digit_model.keras`. Training may take several minutes.

## Run the Website
```bash
python app.py
```
Open http://127.0.0.1:5000 in your browser and upload a clear image containing one handwritten digit.

## Notes
- MNIST contains small grayscale images of handwritten digits. Photos with busy backgrounds, multiple digits, colored writing, or unusual orientations may be misclassified.
- Images with a light digit on a dark background generally work best; preprocessing attempts to invert images with a light background.
- The confidence score is the model's output probability, not a guarantee of correctness.
- The trained model is not included in the ZIP; generate it by running `python train_model.py`.

## Future Enhancements
- Draw a digit directly on a canvas
- Display probabilities for all ten digits
- Improve preprocessing for phone-camera images
- Deploy to a cloud platform
- Add prediction history and downloadable results
