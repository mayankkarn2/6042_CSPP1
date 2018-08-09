'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def isWordGuessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i = 0
    found = 0
    while i < len(letters_guessed):
        if letters_guessed[i] in secret_word:
           return True
        else:
            return False
    
def getGuessedWord(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    i = 0
    secret_copy = list(secret_word)
    output = []
    for x_counter in range(0, len(secret_word), 1):
        output.append("_")
        x_counter = x_counter + 1
    while i < len(secret_word):
        if secret_copy[i] in letters_guessed:
            output[i] = secret_copy[i]
        i += 1
    return ''.join(output)



def getAvailableLetters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    set_alpha = "abcdefghijklmnopqrstuvwxyz"
    set_list = list(set_alpha)
    for search_index, _ in enumerate(set_list):
        if set_list[search_index] in letters_guessed:
            set_list[search_index] = ''
    return ''.join(set_list)

    

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " long")
    letters_guessed = []
    guesses = 8
    length = len(secret_word)
    win = 0
    while(guesses > 0 and win!=1):
        print("-------------------------------------------------------------------")
        print("you have " + str(guesses) + " left")
        print("Available letters:", getAvailableLetters(letters_guessed))
        k = list(input("please guess a letter "))
        # print(k)
        # print(letters_guessed)
        if k[0] in letters_guessed:
            print("Oops! You have already guessed that letter:", getGuessedWord(secret_word, letters_guessed))
        else:
            letters_guessed = letters_guessed + k
            if isWordGuessed(secret_word, k) == True:
                print("Good guess: ", getGuessedWord(secret_word, letters_guessed))
                if secret_word == getGuessedWord(secret_word, letters_guessed):
                    win = 1
            else:
                print("Oops! That letter is not in my word: ",getGuessedWord(secret_word, letters_guessed))
                guesses = guesses - 1

    if win == 1:
        print("You won")
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word)

def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secret_word = chooseWord(wordlist).lower()
    hangman(secret_word)
if __name__ == "__main__":
    main()
