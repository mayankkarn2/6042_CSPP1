# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    '''This program checks if a number is
        perfect cube or not'''
    input_n = int(input())
    found_flag = 0
    for x_i in range(1, input_n+1, 1):
        if x_i*x_i*x_i == input_n:
            found_flag = 1
            break
        else:
            found_flag = 0
    if found_flag == 1:
        print(str(input_n)+" is a perfect cube")
    else:
        print(str(input_n)+" is not a perfect cube")


if __name__ == "__main__":
    main()
