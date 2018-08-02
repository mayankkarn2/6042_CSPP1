"""This a program to print natural numbers upto n by using while loop"""
NUM = int(input("Enter a number"))
SUM = 0
COUNT = 1
while COUNT <= NUM:
    SUM = SUM + COUNT
    COUNT = COUNT + 1
print(SUM)
