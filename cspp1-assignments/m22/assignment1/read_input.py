'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    string = ''
    lines = int(input())
    for _ in range(lines):
        str_list = input().split("\n")
        string = string + "\n" + ''.join(str_list)
    print(string)
if __name__ == '__main__':
    main()
