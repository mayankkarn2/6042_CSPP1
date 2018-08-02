'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', 
then your program should print
Number of times bob occurs is: 2'''

def main():
   '''This programs counts the nimber of 
      instances of the string 'Bob' in the given string'''
    STR_INPUT = input()
    CHECK_STRING = 'bob'
    STR_LEN = len(STR_INPUT)
    START_VALUE = 0
    END_VALUE = 2
    COUNT_VALUE = 0
    while END_VALUE <= (STR_LEN)-1:
        COUNTER_I = START_VALUE
        EQUALS_FLAG = 1
        COUNTER_J = 0
        while COUNTER_I <= END_VALUE and EQUALS_FLAG == 1:
            if STR_INPUT[COUNTER_I] != CHECK_STRING[COUNTER_J]:
                EQUALS_FLAG = 0
            else:
                COUNTER_I = COUNTER_I + 1
                COUNTER_J = COUNTER_J + 1
            if EQUALS_FLAG == 1:
        COUNT_VALUE = COUNT_VALUE + 1
        START_VALUE = START_VALUE + 1
        END_VALUE = END_VALUE + 1
print(COUNT_VALUE)

if __name__ == "__main__":
    main()
