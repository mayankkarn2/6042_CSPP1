'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
from collections import Counter
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    is_valid_range = range_check(sudoku)
    if is_valid_range is True:
        is_valid_row = row_check(sudoku)
        if is_valid_row is True:
            is_valid_col = col_check(sudoku)
            if is_valid_col is True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        # print(is_valid_row)
        # if is_valid_row is True:
        #     is_valid_col = col_check(sudoku)
        #     print(is_valid_col)
        #     if is_valid_col is True:
        #         return True
    # else:
    #     return False

def range_check(sudoku):
    for row in sudoku:
        for number in row:
            if int(number) >= 1 and int(number) <= 9:
                pass
            else:
                return False
    return True
def row_check(sudoku):
    for row in sudoku:
        # print(row)
        dicti = Counter(row)
        # print(dicti)
        if len(dicti) == 9:
            pass
        else:
            return False
    return True
def col_check(sudoku):
    for i in range(0,9,1):
        lis = []
        for j in range(0,9,1):
            lis.append(sudoku[j][i])
        dicti = Counter(lis)
        if len(dicti) == 9:
            pass
        else:
            return False
    return True
    

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    # print(sudoku)
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()