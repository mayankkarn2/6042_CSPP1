'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    LEN = len(str_input)
    new = list(str_input)
    for x in range(LEN):
    	if new[x] == '!' or new[x] == '@' or new[x] == '#' or new[x] == '$' or new[x] == '%' or new[x] == '^' or new[x] == '&' or new[x] == '*':
    		new[x] = ' '
    str_input=''.join(new)
    print(str_input)
if __name__ == "__main__":
    main()
