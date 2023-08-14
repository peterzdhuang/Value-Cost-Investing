from keras.datasets import imdb
import numpy as np
from keras import models
from keras import layers
#from keras import optimizers
#from keras import losses
#from keras import metrics
import matplotlib.pyplot as plt

(train_data, train_labels), (test_data, test_labels)=imdb.load_data(num_words=10000)


""" Reverse the code back into English
word_index=imdb.get_word_index()
reverse_word_index = dict([(value, key) for (key, value)in word_index.items()])
decoded_review=' '.join([reverse_word_index.get(i-3 , '?') for i in train_data[0]])
print(decoded_review)
"""

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence]=1.
        return results
    
x_train=vectorize_sequences(train_data)
x_test=vectorize_sequences(test_data)

y_train=np.asarray(train_labels).astype("float32")
y_test=np.asarray(test_labels).astype("float32")

model=models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation="relu"))
model.add(layers.Dense(1, activation="sigmoid"))


#model.compile(optimizer=optimizers.RMSprop(lr=0.001), loss=losses.binary_crossentropy, metrics=[metrics.binary_accuracy])

x_val = x_train[:10000]
partial_x_train=x_train[10000:]
y_val=y_train[:10000]
partial_y_train=y_train[10000:]

#model.compile(optimizer='rmsprop',loss ="binary_crossentropy", metrics=['accuracy'])
model.compile(optimizer='rmsprop',loss ="binary_crossentropy", metrics=['acc'])

history = model.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

history_dict=history.history
loss_values = history_dict['loss']
val_loss_values = history_dict["val_loss"]

epochs=range(1,len(loss_values)+1)

plt.plot(epochs, loss_values, "bo", label="Training loss")
plt.plot(epochs, val_loss_values,"b", label="Validation loss")
plt.title ("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

plt.show()

plt.clf()
acc=history_dict["acc"]
val_acc=history_dict["val_acc"]
plt.plot(epochs,acc,"bo", label="Training acc")
plt.plot(epochs, val_acc, 'b', label="validation acc")
plt.title("Training and validation accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.show()





"""=======================================================================
 * TOOK US 1.5 TO FIGURE GITHUB OUT BRUH
========================================================================"""
"""
print("vcghjkl")
print("somehting else")
#wlaterasdjfakdjsf
print("akdsfjh")


def wlater():
    print("walter")

wlater()
def wlater():
    data=12345678
    print(data)
"""
