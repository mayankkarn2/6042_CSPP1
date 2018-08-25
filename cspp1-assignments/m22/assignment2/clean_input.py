'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    regex = re.compile('[^a-z]')
    out_str = ''
    for letter in string:
    	# print(letter)
    	lett = regex.sub("", letter)
    	# print(lett)
    	out_str = out_str + lett
    return out_str

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
