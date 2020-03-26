from tensorflow import keras
import os
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], 28,28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

model = keras.models.Sequential([
keras.layers.Conv2D(64, (2, 2), padding = 'same' , activation = 'elu', input_shape = [28, 28, 1]),
keras.layers.MaxPooling2D(2),
keras.layers.Conv2D(128, (3, 3), padding = "same", activation = "elu"),
keras.layers.Conv2D(256, (4, 4), padding = "same", activation = "elu"),
keras.layers.Dropout(0.5),
keras.layers.MaxPooling2D(2),
keras.layers.Flatten(),
keras.layers.Dense(128, activation = "elu"),
keras.layers.Dropout(0.25),
keras.layers.Dense(10, activation = "softmax")
])

model.compile(loss = "sparse_categorical_crossentropy", metrics = ["accuracy"], optimizer = keras.optimizers.SGD(lr = 0.08))
print(model.summary())
model.fit(x_train, y_train, epochs = 5)
model.evaluate(x_test, y_test)
model.save('model.h5')
print('Model Saved')