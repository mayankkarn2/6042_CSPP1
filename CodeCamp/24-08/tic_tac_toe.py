def horizontal_check(grid):
    if grid[0][0] == grid[0][1] == grid[0][2]:
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][0]

def verical_check(grid):
    if grid[0][0] == grid[1][0] == grid[2][0]:
        return grid[0][0]
    if grid[0][1] == grid[1][1] == grid[2][1]:
        return grid[0][1]
    if grid[0][2] == grid[1][2] == grid[2][2]:
        return grid[0][2]

def diagonal_check(grid):
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

def is_valid_grid(grid):
    for inputs in grid:
        for j in inputs:
            if j == 'x' or j == 'o' or j == '.':
                pass
            else:
                return False
    return True 

def is_valid_game(grid):
    count_x = 0
    count_o = 0
    count_dot = 0
    for inputs in grid:
        for j in inputs:
            if j == 'x':
                count_x += 1
            elif j == 'o':
                count_o += 1
            elif j == '.':
                count_dot += 1 
    if abs(count_x - count_o >=2):
        return False
    elif abs(count_x - count_o == 0) and count_dot > 0:
        return False
    return True
def main():
    winner = None
    grid = []
    for i in range(0,3,1):
        values = input().split(' ')
        temp = []
        for j in values:
            temp.append(j)
        grid.append(temp)
    valid_grid = is_valid_grid(grid) and is_valid_game(grid)
    if valid_grid == True:
        winner = horizontal_check(grid)
        if winner == None:
            winner = verical_check(grid)
        if winner == None:
            winner = diagonal_check(grid)
        if winner == None:
            print("draw")
        else:
            print(winner)
    else:
        if not (is_valid_grid(grid)):
            print("invalid input")
        if  not (is_valid_game(grid)):
            print("invalid game")

if __name__ == '__main__':
    main()
