'''Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991'''

def main():
    '''This program prints square root'''
    input_n = int(input())
    low = 0
    high = input_n
    diff = 0.01
    while 1:
        mid = (low + high)/2
        if mid * mid >= (input_n-diff) and mid * mid <= (input_n+diff):
            break
        elif mid * mid > input_n:
            high = mid
        else:
            low = mid
    print(mid)
if __name__ == "__main__":
    main()
