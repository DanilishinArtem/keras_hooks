import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Generate random data
x_train = np.random.random((1000, 100))
y_train = np.random.randint(2, size=(1000, 10))

# Create a Sequential model
model = Sequential()

# Add layers to the model
model.add(Dense(units=64, activation='relu', input_shape=(100,)))
model.add(Dense(units=10, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=1, batch_size=32)
