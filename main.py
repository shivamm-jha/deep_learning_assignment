import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np


(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()

X_train.shape
X_test.shape

X_train[0].shape

plt.matshow(X_train[0])

y_train[0]
X_train = X_train / 255
X_test = X_test / 255

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10)

model.evaluate(X_test,y_test)

X_train = X_train.reshape(-1,28,28,1)
X_train.shape


X_test = X_test.reshape(-1,28,28,1)
X_test.shape


model = keras.Sequential([
    
    layers.Conv2D(30, (3,3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2,2)),
 
    layers.Flatten(),
    layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5)

y_train[:5]

model.evaluate(X_test,y_test)

