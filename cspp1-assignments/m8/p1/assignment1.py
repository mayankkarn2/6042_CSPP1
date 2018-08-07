'''# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns
 the factorial of given number.

# This function takes in one number and returns one number.'''


def factorial(input_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if input_n in (1, 0):
        return 1

    return input_n * factorial(input_n-1)
def main():
    '''T  his program calculates factorial
    '''
    a_input = input()
    print(factorial(int(a_input)))

if __name__ == "__main__":
    main()
