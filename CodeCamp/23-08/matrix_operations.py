def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    row_1 = len(m1)
    col_1 = len(m1[0])
    row_2 = len(m2)
    col_2 = len(m2[0])
    if col_1 != row_2:
        print("Error: Matrix shapes invalid for mult")
        return "None"
    else:
        mul_matrix = []
        for i in range(0, row_1, 1):
            temp_list = []
            for j in range(0, col_2, 1):
                add = 0
                for k in range(0, col_1, 1):
                    add = add + m1[i][k] * m2[k][j]
                temp_list.append(add)
            mul_matrix.append(temp_list)
        return mul_matrix

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    row_1 = len(m1)
    col_1 = len(m1[0])
    row_2 = len(m2)
    col_2 = len(m2[0])
    if row_1 != row_2 or col_1 != col_2:
        print("Error: Matrix shapes invalid for addition")
        return "None"
    else:
        addition_matrix = []
        for i in range(0, row_1, 1):
            temp_list = []
            for j in range(0, col_1, 1):
                k = m1[i][j] + m2[i][j]
                temp_list.append(k)
            addition_matrix.append(temp_list)
        return addition_matrix
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    m1 = []
    m2 = []
    try:
        q_int = input()
        dim_1 = q_int.split(',')
    except:
        print("Error: Invalid input for the matrix")
    else:
        for i in range(1, int(dim_1[0])+1, 1):
            values = input()
            rows = (values.split(" "))
            k = []
            for j in rows:
                k.append(int(j))
            m1.append(k)
    try:
        q_int = input()
        dim_2 = q_int.split(',')
    except:
        print("Error: Invalid input for the matrix")
    else:
        for i in range(1, int(dim_2[0])+1, 1):
            values = input()
            rows = (values.split(" "))
            k = []
            for j in rows:
                k.append(int(j))
            m2.append(k)
        len_check1 = 1
        len_check2 = 1
        for i in m2:
            if len(i) != int(dim_2[1]):
                len_check2 = 0
        for i in m1:
            if len(i) != int(dim_1[1]):
                len_check1 = 0
        if len(m2) != int(dim_2[0]) or len_check2 == 0:
            print("Error: Invalid input for the matrix")
        elif len(m1) != int(dim_1[0]) or len_check1 == 0:
            print("Error: Invalid input for the matrix")
        else:
            print(add_matrix(m1, m2))
            print(mult_matrix(m1, m2))

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    read_matrix()

if __name__ == '__main__':
    main()
