#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]


def apply_to_each(L, add):
	L1 = []
	for x in L:
		L1.append(add(x))
	return L1
def add(n):
	return n+1
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, add))
if __name__ == "__main__":
    main()
