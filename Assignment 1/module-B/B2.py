# B1:Function(3/3)

import re
import sys
from collections import defaultdict
import spacy


def load_book(book_id):
    paragraphs = []

    try:
        with open("./data/books/" + book_id + ".txt") as file:
            book_data = file.read()
            trimmed_book_data = book_data.strip()
            paragraphs = re.split('\n{2,}', trimmed_book_data)
            print(trimmed_book_data)

    except FileNotFoundError:
        print("Error, file not found.")
        sys.exit()

    return paragraphs


# B2:Function(10/10)
nlp = spacy.load("en")


def def_value():
    tmp_list = []
    return tmp_list


def kwic(paragraphs, search_terms={}):

    data = defaultdict(def_value)
    idx_paragraph = 0
    idx_sentence = 0

    for para in paragraphs:
        idx_paragraph += 1
        doc = nlp(para)

        for sent in doc.sents:
            idx_sentence += 1
            # print(sent)

            word_list = []
            for token in sent:
                word_list.append(token.text)

            for token in sent:
                # print(token)

                if token.text in search_terms:
                    # print('found it')
                    tmp_list = [[idx_paragraph, idx_sentence, token.idx], word_list]
                    data[token.text].append(tmp_list)


    return data


# --- Program Starts Here ---
paragraphs = load_book('84')
print(len(paragraphs))
print(paragraphs[10])

words = kwic(paragraphs, {'Frankenstein', 'monster'})
for k, v in words.items():
    print('Word ' + k)
    print('Values ')
    print(v)