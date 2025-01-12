from PIL import Image
import keras
import numpy as np

# load the models
cnn_model = keras.models.load_model('models/CNN_epoch_25.keras')
ann_model = keras.models.load_model('models/ANN_epoch_8.keras')


# image preprocessing function
def preprocess_image(image, model_selected):
    image = Image.open(image)
    image = image.convert('L')
    image = image.resize((32, 32))
    image = np.array(image)
    image = image / 255.0
    if model_selected == 'ANN':
        image = image.flatten()
    else:
        image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)
    return image


# predictor function
def make_prediction(uploaded_image, model_selected):
    # preprocess
    image = preprocess_image(uploaded_image, model_selected)
    # predict
    if model_selected == 'ANN':
        prediction = ann_model.predict(image)
    else:
        prediction = cnn_model.predict(image)
    # result
    result = np.argmax(prediction, axis=1)
    return result
