# Position Based Indexer - Tomas Pasiecznik

# Imports
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re
import os
import queue
import natsort
from collections import OrderedDict

# Package Downloads (Will make sure package punkt installed and up-to-date!)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Add Input Path Here - Crawled Pages
input_path = ''

# Add Output Path Here - Inverted Index
output_path = ''


# Position-Based Indexer
def indexer(source, destination):
    # Index Initialization
    index = {}

    # File Path Queue Initialization
    q = queue.Queue()

    # Get File Names
    files = os.listdir(source)

    # Used natsort to order numbered input files.
    files = natsort.natsorted(files)

    # File Parser
    for file in files:
        # Append File Name To Source Path & Add To Queue
        q.put(source + file)

    # Document Numbering + File Count
    d = 1
    fc = 0

    # Defining Stopwords
    stop_words = stopwords.words('english')

    print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')
    print('| Indexer Activated |')
    print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')

    # File Path Queue Traversal
    while q.qsize() != 0:
        print('Currently Indexing: ' + files[fc])
        print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')

        # Get File Path From Queue
        path = q.get()

        # Pass File Path into BeautifulSoup
        with open(path, encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Get Text From HTML Document
        text = soup.get_text()

        # Clean Text
        text = text.lower()
        text = re.sub(r"[^\w]", " ", text)
        text = re.sub("([^\x00-\x7e])+", " ", text)
        text = re.sub("[1234567890_]", " ", text)

        # Tokenize The Text
        tokens = nltk.word_tokenize(text)
        print(tokens)

        # Stopword Removal
        stopword_index = -1
        for token in tokens:
            stopword_index += 1
            if token in stop_words:
                tokens.pop(stopword_index)

        # Token Parser
        position = 0
        for token in tokens:
            position += 1
            if token not in index:
                index[token] = []
                index[token].append([d, position])
            else:
                index[token].append([d, position])


        # Document Counter Increase
        d += 1
        fc += 1

    # Alphabetical Order Index
    ordered_index = OrderedDict(sorted(index.items()))

    # File Output: Save Inverted Index File
    f = open(destination + 'position-based-index.txt', 'w', encoding='utf-8')
    for term in ordered_index:
        f.write(term + ' => ')
        for posting in ordered_index[term]:
            doc_id = str(posting[0])
            term_position = str(posting[1])
            f.write('(' + doc_id + ':' + term_position + ') ')
        f.write('\n')
    f.close()

    print('| Indexer Deactivated |')
    print('――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――')


indexer(input_path, output_path)
