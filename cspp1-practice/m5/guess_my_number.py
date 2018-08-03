low=0
high=100
print("Please think of a number between 0 and 100!")
while 1:
	num=(low+high)//2
	print("Is your secret number "+str(num))
	print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	i=input()
	if i=='c':
		break
	elif i=='h':
		low=num
	elif i=='l':
		high=num
	else:
		print("Sorry, I did not understand your input")
print("Game over. Your secret number was: "+str(num))