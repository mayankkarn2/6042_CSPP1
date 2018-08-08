#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(L, f):
	L1 = []
	for x in L:
		L1.append(f(x))
	return L1

    

def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
