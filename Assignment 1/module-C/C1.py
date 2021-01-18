# C1:Function(12/12)

from collections import Counter
import spacy, json, re

nlp = spacy.load("en")


def count_words(paragraph, pos=True, lemma=True):

    frequency = Counter()
    doc = nlp(paragraph)
    print(doc)

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


# --- Start Program Here ---

count_words("The quick brown fox dog jumps over the brown quick lazy dog.")
