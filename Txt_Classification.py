# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:51:35 2020

@author: Troy
"""


import tensorflow as tf
from tensorflow import keras
import numpy as np


data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)

word_index = data.get_word_index()

word_index = {k:(v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])


train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post",maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post",maxlen=250)

print(len(train_data), len(test_data))

def decode_review(text):
    return " ".join([reverse_word_index.get(i,"?") for i in text])

print(decode_review(test_data[0]))

print(len(test_data[0]), len(test_data[1]))       

 
# model

model = keras.Sequential()
model.add(keras.layers.Embedding(88000,16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.summary()  # prints a summary of the model


model.save("model.h5")