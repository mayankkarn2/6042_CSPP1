def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    row1 = len(m1)
    col1 = len(m1[0])
    row2 = len(m2)
    col2 = len(m2[0])
    if col1 != row2:
        print("Error: Matrix shapes invalid for mult")
        return
    else:
        mul_matrix = []
        for i in range(0,row1,1):
            temp = []
            for j in range(0,col1,1):
                add = 0
                for k in range(0,col1,1):
                    add = add + m1[i][k] * m2[k][j]
                temp.append(add)
            mul_matrix.append(temp)
        print(mul_matrix)

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    row1 = len(m1)
    col1 = len(m1[0])
    row2 = len(m1)
    col2 = len(m1[0])
    if row1!=row2 or col1!=col2:
        print("Error: Matrix shapes invalid for addition")
        return
    else:
        addition_matrix = []
        for i in range(0,row1,1):
            temp = []
            for j in range(0,col1,1):
                k = m1[i][j] + m2[i][j]
                temp.append(k)
            addition_matrix.append(temp)
        print(addition_matrix)
        return
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
    q = input()
    dim1 = q.split(',')
    for i in range(1,int(dim1[0])+1,1):
        values = input()
        rows = (values.split(" "))
        k = []
        for j in rows:
            k.append(int(j[0]))
        m1.append(k)
    q = input()
    dim2 = q.split(',')
    for i in range(1,int(dim2[0])+1,1):
        values = input()
        rows = (values.split(" "))
        print(rows)
        k = []
        for j in rows:
            k.append(int(j))
        m2.append(k)
    add_matrix(m1, m2)
    # mult_matrix(m1, m2)

    

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    read_matrix()

if __name__ == '__main__':
    main()
