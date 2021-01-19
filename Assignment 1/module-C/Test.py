from collections import Counter
import spacy, json, re
import numpy as np


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

nlp = spacy.load("en")

text = '''Lost and weary, Catelyn Stark gave herself over to her gods. 
She knelt before the Smith, who fixed things that were broken, 
and asked that he give her sweet Bran his protection. 
She went to the Maid and beseeched her to lend her courage to Arya and Sansa, 
to guard them in their innocence. 
To the Father, she prayed for justice, the strength to seek it and the wisdom to know it, 
and she asked the Warrior to keep Robb strong and shield him in his battles. 
Lastly she turned to the Crone, whose statues often showed her with a lamp in one hand. 
"Guide me, wise lady," she prayed. 
"Show me the path I must walk, and do not let me stumble in the dark places that lie ahead."
'''

doc = nlp(text)

## the 'master' set, keeps track of the words in all documents
all_words = set()

## store the word frequencies by book
all_doc_frequencies = {}

## loop over the sentences
for j, sentence in enumerate(doc.sents):
    frequency = count_words(sentence.text)
    all_doc_frequencies[j] = frequency
    doc_words = set(frequency.keys())
    all_words = all_words.union(doc_words)

## create a matrix of zeros: (words) x (documents)
TDM = np.zeros((len(all_words), len(all_doc_frequencies)))

## fix a word ordering for the rows
all_words = sorted(list(all_words))

## loop over the (sorted) document numbers and (ordered) words; fill in matrix
for j in all_doc_frequencies:
    for i, word in enumerate(all_words):
        TDM[i, j] = all_doc_frequencies[j][word]

TDM[:10, ]
