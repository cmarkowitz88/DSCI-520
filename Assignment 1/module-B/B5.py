# B1:Function(3/3)

import re
import sys
from collections import defaultdict
import spacy

nlp = spacy.load("en")


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


# B4:Function(10/10)

def load_book_2(book_id):
    idx_paragraph = 0
    idx_sentence = 0
    idx_word = 0

    document = []
    index = defaultdict(def_value)

    '''
    tst_lst = [['paragraph1', ['sentence1', 'sentence2']], ['paragraph2']]
    print(tst_lst[0])
    print(tst_lst[0][1])
    l = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
    '''

    try:
        with open("./data/books/" + book_id + ".txt") as file:
            book_data = file.read()
            trimmed_book_data = book_data.strip()
            paragraphs = re.split('\n{2,}', trimmed_book_data)

            for para in paragraphs:
                para_list = []
                doc = nlp(para)
                para_list.append(doc.text)
                document.append(para_list)

                # sent_list = []
                for sent in doc.sents:
                    sent_list = []
                    sent_list.append(sent.text)
                    # doc_list[idx_paragraph].append(sent_list)

                    word_list = []
                    idx_word = 0

                    for token in sent:
                        word_list.append(token.text)

                        indicies_list = [idx_paragraph, idx_sentence, idx_word]
                        index[token.text].append(indicies_list)

                        idx_word += 1

                    sent_list.append(word_list)
                    document[idx_paragraph].append(sent_list)

                    idx_sentence += 1

                idx_paragraph += 1
                idx_sentence = 0



    except FileNotFoundError:
        print("Error, file not found.")
        sys.exit()

    return document, index


# B2:Function(10/10)


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


def fast_kwic(document, index, search_terms={}):
    data = defaultdict(def_value)

    for term in search_terms:

        if term in index:
            print('found it')
            lst_word_indicies = index[term]
            if len(lst_word_indicies) > 0:
                for occurence in lst_word_indicies:
                    i = occurence[0]
                    j = occurence[1]
                    k = occurence[2]
                    sentence_words = document[i][j+1][1]
                    tmp_lst = [occurence, sentence_words]
                    data[term].append(tmp_lst)

    return data


# --- Program Starts Here ---
document, index = load_book_2('84')
print(document[9][5])

search_terms = {'Frankenstein', 'monster'}
output = fast_kwic(document, index, {'Frankenstein'})
print(output)
