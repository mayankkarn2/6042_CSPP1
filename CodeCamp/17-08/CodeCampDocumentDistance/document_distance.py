'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
from collections import Counter
def word_frequency(list1, list2):
    freq_a = dict(Counter(list1))
    freq_b = dict(Counter(list2))
    word_freq = {}
    for key in freq_a:
        if key in freq_b.keys():
            word_freq[key] = [freq_a[key], freq_b[key]]
        else:
            word_freq[key] = [freq_a[key], 0]
    for key in freq_b:
        if key not in freq_a:
            word_freq[key] = [0, freq_b[key]]
    return word_freq

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    regex = re.compile('[^a-z]')
    dict1 = dict1.lower()
    dict2 = dict2.lower()
    dict1_ = []
    dict2_ = []
    dict1 = dict1.split()
    dict2 = dict2.split()
    for item in dict1:
        item = item.strip('')
    for item in dict2:
        item = item.strip('')
    for word in dict1:
        word = regex.sub("", word)
        dict1_.append(word)
    for word in dict2:
        word = regex.sub("", word)
        dict2_.append(word)
    stopwords = load_stopwords('stopwords.txt')
    sdict1_ = []
    sdict2_ = []
    for word in dict1_:
        if word not in stopwords.keys() and len(word) > 0:
            sdict1_.append(word)
    for word in dict2_:
        if word not in stopwords.keys() and len(word) > 0:
            sdict2_.append(word)
    word_frequency_ = word_frequency(sdict1_, sdict2_)
    num_sum = 0
    # word_frequency_ = { 'a':[5, 6], 'b': [4, 6], 'c': [1, 3]}
    for key in word_frequency_.values():
        num_sum = num_sum + (int(key[0]) * int(key[1]))
    den = 0
    den1 = 0
    for key in word_frequency_.values():
        den = den + (int(key[0]) * int(key[0]))
    den_ = math.sqrt(den)
    for key in word_frequency_.values():
        den1 = den1 + (int(key[1]) * int(key[1]))
    den1_ = math.sqrt(den1)
    numerator = num_sum
    denominator = den_ * den1_
    return numerator/denominator

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
