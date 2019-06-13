from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf

import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
from tensorflow.keras import layers
import time

# from IPython import display

# train_datagen = ImageDataGenerator(rescale=1./255)

# train_generator = train_datagen.flow_from_directory(
#         train_path,
#         target_size=(224, 224),
#         batch_size=batch_size,
#         class_mode='binary') 

# (train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()