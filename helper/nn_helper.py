from nltk import word_tokenize
from keras.layers import Dense, LSTM, Activation
from keras.models import Sequential
from keras.optimizers import RMSprop


def tokenize_text(text):
    token_list = word_tokenize(text)
    return token_list


def build_model(word_length, unique_token_length):
    model = Sequential()
    model.add(LSTM(128, input_shape=(word_length, unique_token_length)))
    model.add(Dense(unique_token_length))
    model.add(Activation('softmax'))
    return model


def otmimizer():
    return RMSprop(0.01)