# Handwritten Digit Recognition Using Deep Learning

## 1. Project Overview

Handwritten Digit Recognition is a deep learning project that identifies handwritten digits from 0 to 9 using a Convolutional Neural Network (CNN). The system allows users to upload an image of a handwritten digit and predicts the corresponding number.

This project uses the MNIST dataset to train the CNN model and Flask to develop a simple web application.

## 2. Objectives

- To recognize handwritten digits automatically.
- To build a CNN model for image classification.
- To train the model using the MNIST dataset.
- To create a user-friendly web interface using Flask.
- To display the predicted digit for an uploaded image.

## 3. Technologies Used

- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow and Keras
- **Model:** Convolutional Neural Network (CNN)
- **Dataset:** MNIST Handwritten Digit Dataset
- **Web Framework:** Flask
- **Image Processing:** Pillow (PIL)
- **Frontend:** HTML and CSS

## 4. Project Structure

```text
Handwritten Digit Recognition/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── digit_model.keras
│   └── README.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── uploads/
```

*Note: The trained model file `digit_model.keras` is generated after running `train_model.py`.*

## 5. Dataset

This project uses the MNIST dataset, which contains 70,000 grayscale images of handwritten digits from 0 to 9.

- Training images: 60,000
- Testing images: 10,000
- Image size: 28 × 28 pixels
- Number of classes: 10

The dataset is loaded automatically through TensorFlow and Keras.

## 6. Methodology

1. **Dataset Loading:** Load the MNIST dataset.
2. **Preprocessing:** Normalize pixel values and prepare the images.
3. **Model Building:** Create a CNN model for digit classification.
4. **Model Training:** Train the CNN using the training dataset.
5. **Model Saving:** Save the trained model for future predictions.
6. **Image Upload:** Allow users to upload a handwritten digit image.
7. **Prediction:** Process the image and predict the digit.
8. **Result Display:** Display the predicted number on the webpage.

## 7. Installation and Execution

### Step 1: Open the Project Folder

Open the project folder in VS Code and open the terminal.

### Step 2: Create a Virtual Environment

```bash
py -3.11 -m venv .venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Train the Model

```bash
python train_model.py
```

This downloads the MNIST dataset if needed, trains the CNN model, and saves the trained model.

### Step 6: Run the Web Application

```bash
python app.py
```

### Step 7: Open the Application

Open the local URL displayed in the terminal, usually:

```text
http://127.0.0.1:5000
```

Upload an image containing a handwritten digit to view the prediction.

## 8. Expected Output

The web application displays an interface where users can upload a handwritten digit image. After submission, the trained CNN model analyzes the image and displays the predicted digit from 0 to 9.

<img width="1723" height="892" alt="Screenshot 2026-10-26 194315" src="https://github.com/user-attachments/assets/781e1440-afb1-485d-881f-e9aebd243ac0" />

<img width="1890" height="895" alt="Screenshot 2026-10-26 194426" src="https://github.com/user-attachments/assets/14db0b23-203d-4c69-8de7-a14cf92935a7" />

The prediction depends on the quality, alignment, and clarity of the uploaded image.

## 9. Advantages

- Simple and user-friendly interface.
- Automatic handwritten digit classification.
- Uses a well-known dataset for model training.
- Demonstrates practical applications of deep learning.
- Can be executed on a local computer.

## 10. Applications

- Digit recognition in handwritten documents.
- Postal code recognition.
- Form and document processing.
- Educational demonstrations of image classification.
- Optical character recognition research.

## 11. Limitations

- The model is primarily trained on the MNIST dataset.
- Unclear or poorly aligned images may produce incorrect predictions.
- The current application is designed for recognizing a single digit at a time.
- It may not accurately recognize multiple digits in one image.

## 12. Future Enhancements

- Support recognition of multiple digits in one image.
- Improve image preprocessing for real-world handwriting.
- Deploy the application to a cloud platform.
- Add prediction confidence scores.
- Develop a mobile-friendly interface.

## 13. Conclusion

The Handwritten Digit Recognition project demonstrates how deep learning can be used to classify handwritten digits. By combining a CNN model, the MNIST dataset, and a Flask web application, the system provides a simple way to upload an image and obtain a digit prediction. This project provides practical experience in deep learning, image processing, and web application development.


**Project Name:** Handwritten Digit Recognition Using Deep Learning

**Domain:** Deep Learning

**Language:** Python
