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
    LEN_str = len(str_input)
    n_s = list(str_input)
    for x_i in range(LEN_str):
        if n_s[x_i] == '!' or n_s[x_i] == '@' or n_s[x_i] == '#' or n_s[x_i] == '$' or n_s[x_i] == '%' or n_s[x_i] == '^' or n_s[x_i] == '&' or n_s[x_i] == '*':
            n_s[x_i] = ' '
    str_input =''.join(n_s)
    print(str_input)
if __name__ == "__main__":
    main()
