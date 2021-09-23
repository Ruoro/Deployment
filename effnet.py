import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.applications import EfficientNetB0
import tensorflow_datasets as tfds


def model():
    model = tf.keras.models.load_model('InceptionV3.h5')
    # prediction = model.predict(X)
    return model