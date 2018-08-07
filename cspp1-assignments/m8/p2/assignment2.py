'''# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one 
number and returns the sum of digits of given number.

# This function takes in one number and returns one number.'''


def sumofdigits(var_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if var_n == 0:
    	return 0
    var_r = var_n % 10
    var_n = var_n//10
    return var_r + sumofdigits(n)


def main():
    var_a = input()
    print(sumofdigits(int(a)))

if __name__== "__main__":
    main()

