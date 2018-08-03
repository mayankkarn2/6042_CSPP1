# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    
    epsilon = 0.01
    step = 0.1
    num = int(input())
    guess = 0.0
    while abs((guess**2) - num ) >= epsilon:
        guess = guess + step
    if abs((guess**2) - num) >= epsilon:
        print(num)
    else:
        print(guess)
if __name__ == "__main__":
    main()
