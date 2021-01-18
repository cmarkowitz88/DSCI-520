# B1:Function(3/3)

import re
import sys
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


# --- Program Starts Here ---
paragraphs = load_book('84')
print(len(paragraphs))
print(paragraphs[10])
