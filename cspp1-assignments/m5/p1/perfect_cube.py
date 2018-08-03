# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
	INPUT_N = int(input())
	FOUND_FLAG = 0
	for x in range(1,INPUT_N+1,1):
		if x*x*x == INPUT_N:
			FOUND_FLAG = 1
			break
		else:
			FOUND_FLAG = 0
	if FOUND_FLAG == 1:
		print("Perfect Cube")
	else:
		print("Not a perfect cube")

if __name__ == "__main__":
	main()
