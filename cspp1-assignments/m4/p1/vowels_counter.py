"""# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
"""
#Number of vowels: 5

def main():
    '''
        This program counts the number
        of vowels in given string
    '''
STR_INPUT = input()
VOWEL_COUNT = 0
STR_INPUT = STR_INPUT.lower()
for char in STR_INPUT:
    if char in "aeiou":
        VOWEL_COUNT = VOWEL_COUNT + 1
print(VOWEL_COUNT)
	# the input string is in s
	# remove pass and start your code here
if __name__ == "__main__":
	main()
