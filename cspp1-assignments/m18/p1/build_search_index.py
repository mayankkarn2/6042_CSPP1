'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
from collections import Counter
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    regex = re.compile('[^a-z]')
    text_c = []
    text_c2 = []
    text_c3 = []
    for string in text:
        string = string.lower().split()
        text_c.append(string)
    for sentence in text_c:
        k = []
        for word in sentence:
            word = regex.sub("", word)
            k.append(word)
        text_c3.append(k)
    stop_words = load_stopwords('stopwords.txt')
    c_text = []
    for sentence in text_c3:
        k = []
        for word in sentence:
            if word not in stop_words.keys() and len(word)!=0:
                k.append(word)
        c_text.append(k)
    return c_text

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    print(docs)
    list1 = word_list(docs)
    search_index = {}
    for sentence in list1:
        i = 0
        while i < len(sentence):
            search = sentence[i]
            for sublist in list1:
                if search in sublist:
                    ind = list1.index(sublist)
                    cnt = sublist.count(search)
                    t = (ind, cnt)
                    if search not in search_index.keys():
                        search_index[search] = list(tuple(t))
                    else:
                        search_index[search].append(list(tuple(t)))

            i = i +1
    print(search_index)
    return search_index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    build_search_index(documents)
    # print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
