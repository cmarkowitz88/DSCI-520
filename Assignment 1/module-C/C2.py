# C1:Function(12/12)

from collections import Counter
import spacy, json, re
import numpy as np

nlp = spacy.load("en")


def count_words(paragraph, pos=True, lemma=True):
    frequency = Counter()
    doc = nlp(paragraph)
    # print(doc)

    for word in doc:
        # print(word)

        text = word.text
        tag = ''

        if lemma:
            text = word.lemma_

        if pos:
            tag = word.pos_

        heading = (text, tag)

        frequency[heading] += 1

    return frequency


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


def book_TDM(book_id, pos=True, lemma=True):

    paragraphs = load_book('84')

    # the 'master' set, keeps track of the words in all documents
    all_words = set()

    # store the word frequencies by book
    all_doc_frequencies = {}

    for text in paragraphs:

        doc = nlp(text)

        # loop over the sentences
        for j, sentence in enumerate(doc.sents):
            frequency = count_words(sentence.text)
            all_doc_frequencies[j] = frequency
            doc_words = set(frequency.keys())
            all_words = all_words.union(doc_words)

    # create a matrix of zeros: (words) x (documents)
    TDM = np.zeros((len(all_words), len(all_doc_frequencies)))

    # fix a word ordering for the rows
    all_words = sorted(list(all_words))

    # loop over the (sorted) document numbers and (ordered) words; fill in matrix
    for j in all_doc_frequencies:
        for i, word in enumerate(all_words):
            TDM[i, j] = all_doc_frequencies[j][word]

    return TDM, all_words


# --- Start Program Here ---

count_words("The quick brown fox dog jumps over the brown quick lazy dog.")

TDM, terms = book_TDM("84", True, True)
