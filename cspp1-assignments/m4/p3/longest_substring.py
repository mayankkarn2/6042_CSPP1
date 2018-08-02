'''Assume s is a string of lower case characters.

Write a program that prints the longest
substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging.
We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course
If you have time, come back to this problem after
you've had a break and cleared your head.'''

def main():
    """This program prints the longest sequence of alphabets"""
    string_input = input()
    string_a = string_input + "!"
    temp = ''
    temp_1 = ''
    beg_val = 0
    mov_val = 1
    leng = len(string_a)
    count = 1
    length = 1
    while mov_val <= leng-1:
        count = 1
        temp = string_a[beg_val]
        while string_a[beg_val] <= string_a[mov_val] and mov_val < leng:
            count = count + 1
            temp = temp+string_a[mov_val]
            beg_val = mov_val
            mov_val = mov_val + 1
        beg_val = mov_val
        mov_val = mov_val + 1
        if count == length:
            temp_1 = temp_1

        if count > length:
            length = count
            temp_1 = ""
            temp_1 = temp
    print(temp_1)



if __name__ == "__main__":
    main()