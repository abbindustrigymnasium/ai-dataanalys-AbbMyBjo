import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential
from keras.models import load_model
import csv

x_train = []  # träningsdata
y_train = []  # träningssvar
x_test = []  # testdata
y_test = []  # testsvar

with open('AI_values.csv', mode='r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    counter = 0
    for row in reader:
        if counter <= 150000:
            x_train.append([row[0], row[1], row[2], row[3], row[4], row[5]])
            y_train.append(row[6])
            counter += 1
        else:
            x_test.append([row[0], row[1], row[2], row[3], row[4], row[5]])
            y_test.append(row[6])

# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# x_train = x_train/255.0
# x_test = x_test/255.0

model = Sequential()

model.add(LSTM(150000, input_shape=(x_train, 6), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)

model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))

model.save('my_model.h5')