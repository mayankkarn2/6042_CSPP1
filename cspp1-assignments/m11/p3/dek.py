file = open(r"C:\\Users\\Lenovo\\Desktop\\ex.txt","r")
k = file.read()
print(k)
# o = k.split("\n")
# print(o)
dic = {}
for i in open(r"C:\\Users\\Lenovo\\Desktop\\ex.txt","r"):
	keys, values = i.split()
	# print(keys, values)
	if keys in dic.keys():
		if int(values) not in dic[keys]:
			dic[keys].append(int(values))
	else:
		dic[keys] = [int(values)]
print(dic)






