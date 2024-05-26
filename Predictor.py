import tensorflow as tf
import numpy as np

class ImagePredictor:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path, compile=False)
    
    def load_and_preprocess_image(self, image_path):
        image = tf.io.read_file(image_path)
        image = tf.image.decode_image(image, channels=3, expand_animations=False)
        image = tf.image.resize(image, [256, 256])
        image = image / 255.0
        return image
    
    def predict_image(self, image_path):
        input_image = self.load_and_preprocess_image(image_path)
        input_image = tf.expand_dims(input_image, axis=0)
        prediction = self.model.predict(input_image)
        prediction_thresh = (prediction >= 0.5).astype(np.uint8)
        return prediction_thresh[0]
    
    def process_and_save_image(self, image_path, processed_path):
        prediction = self.predict_image(image_path)
        tf.keras.preprocessing.image.save_img(processed_path, prediction)
