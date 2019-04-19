#alex  look at this

import pandas as pd 
from keras import models
from keras import layers 
import matplotlib.pyplot as plt


def graph_history(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.figure()
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()

df = pd.read_csv('pbp_reg_2018.csv')
# print(df.head())


#yfeats = ['touchdown','rush_touchdown','pass_touchdown','return_touchdown']
yfeats = ['touchdown']


xfeats = ['half_seconds_remaining', 'game_seconds_remaining', 'drive', 'down', 'ydstogo', 
'score_differential_post', 'down']


def build_model(input_shape, output_shape):
    model = models.Sequential()
    model.add(layers.Dense(100, input_shape=(input_shape), activation='relu'))
    model.add(layers.Dense(50, activation='relu'))
    model.add(layers.Dense(output_shape, activation='sigmoid'))

    return model 



rows = df[xfeats].values 
labels = df[yfeats].values 

#TODO: randomize data Shane! for F$%# SAKE!
# indexes = range(0, len(rows))

# reshape from (, NNNN) -> (, NNNN, 1) 
rows = rows.reshape(rows.shape[0], rows.shape[1])
print(f'data.shape:{rows.shape}')

xtrain = rows[:len(rows) // 2]
ytrain = labels[:len(rows) // 2]

xval = rows[len(rows) // 2:]
yval = labels[len(rows) // 2:]



print(f'xtrain shape: {xtrain.shape}')
print(f'ytrain.shape: {ytrain.shape}')

input_shape = (xtrain.shape[1], )
output_shape = ytrain.shape[1]


m = build_model(input_shape, output_shape)

print(f'm.summary:{m.summary}')

m.compile(loss='binary_crossentropy', 
                    optimizer='adam', 
                    metrics=['acc'])


#randomize the day
#split the datain numpy arrays

history = m.fit(xtrain, ytrain,
             epochs=50,
             batch_size=64,
             validation_data=(xval, yval))


graph_history(history)