# DigiRec: Hindi Handwritten Digit Recognizer
A machine learning project to recognize Hindi handwritten digits using TensorFlow. This repository includes two models: **Artificial Neural Network (ANN)** and **Convolutional Neural Network (CNN)**, along with a user-friendly **Streamlit** interface for uploading digit images and obtaining predictions.

## Demo

## Features
- **Digit Recognition**: Recognizes digits from 0 to 9 written in Hindi script.
- **Interactive Interface**: Upload an image of a handwritten digit and get predictions in real-time.
- **Dual Model Support**: Choose between ANN and CNN models for predictions.

## Dataset
The **Hindi MNIST** dataset was used for training and testing. It contains thousands of images of handwritten digits in Hindi script. For more details, visit the [Hindi MNIST Dataset](https://www.kaggle.com/datasets/imbikramsaha/hindi-mnist).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/noobpratik10/DigiRec--hindi-digits-recognizer.git
   cd DigiRec--hindi-digits-recognizer
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
