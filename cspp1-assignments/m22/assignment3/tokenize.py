'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
from collections import Counter
def tokenize(string):
    str_list = input().split()
    dic = dict(Counter(str_list))
    return dic
            
def main():

    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
