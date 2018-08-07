# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
	gcd=1
	if a>b:
		for x in range(1,b+1,1):
			if a%x==0 and b%x==0:
				gcd=x
	else:
		for x in range(1,a+1,1):
			if a%x==0 and b%x==0:
				gcd=x
	return gcd
 
    
def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__ == "__main__":
    main()