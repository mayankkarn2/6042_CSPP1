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
		return grid[0][3]

def diagonal_check(grid):
	if grid[0][0] == grid[1][1] == grid[2][2]:
		print(grid[0][0])
		return grid[0][0]
	if grid[0][2] == grid[1][1] == grid[2][0]:
		print("Here")
		return grid[0][2]

def main():
	winner = None
	grid = []
	for i in range(0,3,1):
		values = input().split(' ')
		temp = []
		for j in values:
			temp.append(j)
		grid.append(temp)
	# print(grid[0][0])
	winner = horizontal_check(grid)
	# print("HC", winner)
	if winner == None:
		winner = verical_check(grid)
		# print("VC", winner)
	if winner == None:
		winner = diagonal_check(grid)
		# print("DC", winner)
	print(winner)

if __name__ == '__main__':
	main()
