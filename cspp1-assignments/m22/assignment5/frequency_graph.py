'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''
        Displays the frequency using "#" as text based graph"
        Input a dictionary
        Outputs a string
    '''
    keys = sorted(dictionary.keys())
    for key in keys:
        hash_count = int(dictionary[key])
        # print(hash_count)
        hashes_p = generate_hashes(hash_count)
        print(key, "-", hashes_p)
def generate_hashes(hash_count):
    '''
        Generates the number of "#"
        Inputs a integer
        Outsputs a string
    '''
    string = ''
    for _ in range(1, hash_count+1, 1):
        string = string + "#"
        # print(string)
    return string

def main():
    '''
        This is the main funtion
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
