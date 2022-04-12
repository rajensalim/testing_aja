from time import time
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
"""
#belajar cari pola bilangan
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
"""
mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#You can put between 0 - 59999 here
index = 59932

#set number of characters per row when printing
np.set_printoptions(linewidth=320)

#print the label and image
print(f'LABEL: {train_labels[index]}')
print(f'\nIMAGE PIXEL ARRAY:\n {train_images[index]}')

#visualize the image
plt.imshow(train_images[index], cmap='Greys')

#normalize the pixel values of the train and test images
train_images = train_images/255.0
test_images = test_images/255.0

#build the clasificaion model
model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

#delcare sample inputs and convert to a tensor
inputs = np.array([[1.0, 3.0, 4.0, 2.0]])
inputs = tf.convert_to_tensor(inputs)
print(f'input to softmax function: {inputs.numpy()}')

#feed the inputs to a softmax activation function
outputs = tf.keras.activations.softmax(inputs)
print(f'output of softmax function: {outputs.numpy()}')

#get the sum of all values after the softmax
sum = tf.reduce_sum(outputs)
print(f'sum of outputs: {sum}')

#get the index with highest value
prediction = np.argmax(outputs)
print(f'class with highest probability: {prediction}')

#compile and fit
model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy']
)

model.fit(train_images, train_labels, epochs=5)

#evaluate the model on unseen data
model.evaluate(test_images, test_labels)
