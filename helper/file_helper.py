import os
import csv


# read data from csv file and return it
def read_csv(path, DATA_READER_LIMIT):
    with open(path, newline='\n', encoding='utf8') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        rows = []
        counter = 0
        for row in data:
            if counter > DATA_READER_LIMIT:
                break
            rows.append(row[1])
            counter += 1
    return rows


# read data from text file and return it
def read_text(path):
    with open(path, encoding='utf8') as text_file:
        data = text_file.readlines()
    return data


# get all directories in path
def get_all_directory(path):
    return os.listdir(path)
