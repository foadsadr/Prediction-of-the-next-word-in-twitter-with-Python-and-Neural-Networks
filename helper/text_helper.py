from nltk import word_tokenize
from helper.file_helper import read_text, get_all_directory


# tokenize sentences to words and remove stop words and clean it
def tokenize(text, stopword_path):
    stopword_list = get_stop_words(stopword_path)
    token_list = [(token.replace('\u200c', '').replace('\u200d', '').strip()) for token in word_tokenize(text) if token not in stopword_list]
    return token_list


# get all stopwords in the persian language
def get_stop_words(path):
    directory_list = get_all_directory(path)
    stopword_set = set()
    for directory in directory_list:
        data = read_text(path + directory)
    for line in data:
        stopword_set.add(line.replace('\n', '').strip())
    return stopword_set


# get chars
def get_text_chars(text):
    bad_char = get_bad_char()
    for char in bad_char:
        text = text.replace(char, '')
    return sorted(list(set(text)))


# get bad character
def get_bad_char():
    return ['!', '"', '#', '&', "'", '(', ')', '*', '+', '-', '.', '/', ':', ';', '=', '?', '.', ',', '_', '-'
            , '#', '@', '*', '\u200c', '\ufeff', '\u200d', '\u2066', '\u2067', '\u2069', '|', '«', '»'
            , '–', '’', '“', '”', '…', '↫', '؛', '؟', 'ء', '🌐', '🌷', '🌹', '🌺', '🍁', '🍃', '🎙', '🎤', '🎧', '🎶'
            , '🏴', '🏻', '🏾', '👇', '👊', '👌', '👍', '👑', '💃', '💋', '💕', '💛', '💜', '💝', '💞', '💠', '💢', '💩'
            , '💪', '💫', '🔔', '🔥', '🔴', '🔵', '🔹', '🔻', '🗡', '😀', '😁', '😂', '😃', '😄', '😅', '😇', '😉', '😊'
            , '😋', '😌', '😍', '😎', '😏', '😐', '😑', '😒', '😔', '😕', '😖', '😘', '😚', '😝', '😞', '😢', '😫', '😬'
            , '😭', '😰', '😳', '😻', '🙂', '🙃', '🙄', '🙈', '🙉', '🙊', '🙋', '🙏', '🚬', '🚶', '🤔', '🤣', '🤦', '🤷'
            , '[', ']', '^'
            , '☀', '☘', '☹', '♀', '♂', '♻', '✅', '✊', '✌', '✔', '✨', '❤', '➖', '➿', '⬅', '《', '》']


def clean_text(text):
    bad_char = get_bad_char()
    for char in bad_char:
        text = text.replace(char, '')
    return text
