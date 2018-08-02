'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl',
then your program should print
Number of times bob occurs is: 2'''

def main():
    '''This programs counts the number of
    instances of the string 'Bob' in the given string'''
    str_input = input()
    check_string = 'bob'
    str_len = len(str_input)
    start_value = 0
    end_value = 2
    count_value = 0
    while end_value <= (str_len)-1:
        counter_i = start_value
        equals_flag = 1
        counter_j = 0
        while counter_i <= end_value and equals_flag == 1:
            if str_input[counter_i] != check_string[counter_j]:
                equals_flag = 0
            else:
                counter_i = counter_i + 1
                counter_j = counter_j + 1
        if equals_flag == 1:
                count_value = count_value + 1
        start_value = start_value + 1
        end_value = end_value + 1
    print(count_value)


if __name__ == "__main__":
    main()
