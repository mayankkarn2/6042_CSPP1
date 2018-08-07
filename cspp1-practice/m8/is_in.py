# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    low = 0
    high = len(aStr)
    mid = (low + high)//2

    if aStr[mid] == char:
        return bool(1)
    elif mid <= 0:
        return bool(0)
    elif char < aStr[mid]:
        high = mid
        return isIn(char, aStr[:high])
    else:
        low = mid
        return isIn(char, aStr[low+1:])


def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__== "__main__":
    main()