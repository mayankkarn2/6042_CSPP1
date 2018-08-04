'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    product = 1
    temp_value = int_input 
    while temp_value>0:
    	rem_value = temp_value % 10
    	product = product * rem_value
    	temp_value = temp_value//10
    print(product)
if __name__ == "__main__":
    main()
