'''
Exercise: Assignment-1
First, implement the function isWordGuessed that takes in two parameters -
a string, secret_word, and a list of letters, letters_guessed. This function
returns a boolean - True if secret_word has been guessed (ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''


def is_word_guessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secret_word are in letters_guessed;
	  False otherwise
	'''
	i = 0
	found = 0
	while i<len(secret_word):
		if secret_word[i] in letters_guessed:
			found += 1
			i += 1
		else:
			i += 1
	print(found)
	if found >= len(secret_word):
		return True
	else:
		return False

def main():
	'''
	Main function for the program
	'''
	user_input = input()
	if user_input:
		data = user_input.split()
		secret_word = data[0]
	else:
		data = []
		secret_word = ""
	list1 = []
	for j in range(1, len(data)):
		list1.append(data[j][0])
	print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
	main()
