'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    keys = sorted(dictionary.keys())
    for key in keys:
        hash_count = int(dictionary[key])
        # print(hash_count)
        hashes_p = generate_hashes(hash_count)
        print(key, "-", hashes_p)
def generate_hashes(hash_count):
    string = ''
    for i in range(1,hash_count+1,1):
        string = string + "#"
        # print(string)
    return string

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
