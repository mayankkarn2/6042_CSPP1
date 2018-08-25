'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
from collections import Counter
def tokenize(string):
    '''
        This function returns the frequency
        of values
    '''
    str_list = string.split()
    # print(str_list)
    dic = dict(Counter(str_list))
    return dic

def main():
    '''
        This is main function
        Here we tokenize the string
    '''
    lines = int(input())
    str_1 = ''
    for i in range(0, lines, 1):
        string = input()
        if i == 0:
            str_1 = str_1 + string
        else:
            str_1 = str_1 + " " + string
    regex = re.compile('[^ a-zA-Z0-9]+')
    string_c = ''
    for letter in str_1:
        letter = regex.sub("", letter)
        string_c = string_c + letter
    # print(string_c)
    print(tokenize(string_c))

if __name__ == '__main__':
    main()
