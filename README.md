we will classify small images cifar10 dataset from tensorflow keras datasets. There are total 10 classes as shown below. We will use CNN for classification

![small_images](https://github.com/shivamm-jha/deep_learning_assignment/assets/77166379/20345f83-ba47-42f6-b69d-3bb6f822067c)


![download (2)](https://github.com/shivamm-jha/deep_learning_assignment/assets/77166379/7c11652d-e1f6-4ade-bfd9-f4631ce6f011)
![download (3)](https://github.com/shivamm-jha/deep_learning_assignment/assets/77166379/7dec6520-fb6b-464e-8754-1d5af8c42b1c)
![download (1)](https://github.com/shivamm-jha/deep_learning_assignment/assets/77166379/37c20d84-05ee-48a6-ba79-4a41af061a26)


Epoch 1/10
1563/1563 [==============================] - 2s 2ms/step - loss: 1.4407 - accuracy: 0.4810
Epoch 2/10
1563/1563 [==============================] - 2s 2ms/step - loss: 1.1084 - accuracy: 0.6109
Epoch 3/10
1563/1563 [==============================] - 2s 2ms/step - loss: 0.9895 - accuracy: 0.6574
Epoch 4/10
1563/1563 [==============================] - 2s 2ms/step - loss: 0.9071 - accuracy: 0.6870
Epoch 5/10
1563/1563 [==============================] - 2s 2ms/step - loss: 0.8416 - accuracy: 0.7097
Epoch 6/10
1563/1563 [==============================] - 2s 2ms/step - loss: 0.7847 - accuracy: 0.7262
Epoch 7/10
1563/1563 [==============================] - 2s 2ms/step - loss: 0.7350 - accuracy: 0.7448
Epoch 8/10
1563/1563 [==============================] - 2s 2ms/step - loss: 0.6941 - accuracy: 0.7574
Epoch 9/10
1563/1563 [==============================] - 2s 1ms/step - loss: 0.6516 - accuracy: 0.7731
Epoch 10/10
1563/1563 [==============================] - 2s 2ms/step - loss: 0.6187 - accuracy: 0.7836


With CNN, at the end 5 epochs, accuracy was at around 70% which is a significant improvement over ANN. CNN's are best for image classification and gives superb accuracy. Also computation is much less compared to simple ANN as maxpooling reduces the image dimensions while still preserving the features
