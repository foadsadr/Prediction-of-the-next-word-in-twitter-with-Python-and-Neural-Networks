from helper.file_helper import *
from helper.nn_helper import *
import numpy as np
import heapq


dataset_path = 'files/dataset/twitter_sample_tweets.csv'
LIMIT_DATA = 1000

data = read_csv(dataset_path, LIMIT_DATA)
print('corpus length : ' + str(len(data)))

text = ''
for row in data:
    text += row

token_list = tokenize_text(text)
# unique_token = set(token_list)
unique_token = np.unique(token_list)
unique_token_index = dict((c, i) for i, c in enumerate(unique_token))
print('total token count : ' + str(len(token_list)))
print('unique token count : ' + str(len(unique_token)))

WORD_LENGTH = 5
prev_word = []
next_word = []
for i in range(len(token_list) - WORD_LENGTH):
    prev_word.append(token_list[i:i + WORD_LENGTH])
    next_word.append(token_list[i + WORD_LENGTH])

X = np.zeros((len(prev_word), WORD_LENGTH, len(unique_token)), dtype=bool)
Y = np.zeros((len(next_word), len(unique_token)), dtype=bool)
for i, each_token in enumerate(prev_word):
    for j, token in enumerate(each_token):
        X[i, j, unique_token_index[token]] = 1
        Y[i, unique_token_index[next_word[i]]] = 1

model = build_model(WORD_LENGTH, len(unique_token))
optimizer = otmimizer()
if os.path.exists('files/model/RNN.model'):
    model.load_weights('files/model/RNN.model')
else:
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    history = model.fit(X, Y, validation_split=0.05, batch_size=256, epochs=10, shuffle=True).history
    model.save('files/model/RNN.model')


def prepare_input(input):
    x = np.zeros((1, WORD_LENGTH, len(unique_token)))
    for t, word in enumerate(input.split()):
        print(word)
        x[0, t, unique_token_index[word]] = 1
    return x


def sample(preds, top_n = 3):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    return heapq.nlargest(top_n, range(len(preds)), preds.take)


def predict(input, n=3):
    if input == '':
        return '0'
    x = prepare_input(input)
    preds = model.predict(x, verbose=0)[0]
    next_indicate = sample(preds, n)
    print(next_indicate)
    return [revert_one_hot(unique_token_index, idx) for idx in next_indicate]


def revert_one_hot(dict, value):
    for dic_key, dic_value in dict.items():
        if dic_value == value:
            return dic_key


input_text = input('please enter your choice : ')
try:
    predict_list = predict(input_text, 10)
    print(predict_list)
except:
    print('input words dos not exists in dictionary')
