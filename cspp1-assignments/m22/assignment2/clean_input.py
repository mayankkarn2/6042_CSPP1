'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''
        Cleans up all special characeters
        Input = string
        returns string
    '''
    regex = re.compile('[^0-9a-zA-Z]+')
    out_str = ''
    for letter in string:
        # print(letter)
        lett = regex.sub("", letter)
        # print(lett)
        out_str = out_str + lett
    return out_str

def main():
    '''
        This is main function
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
