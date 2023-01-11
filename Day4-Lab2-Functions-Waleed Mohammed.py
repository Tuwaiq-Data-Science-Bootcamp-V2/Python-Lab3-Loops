#Day4 Lab2 Functions

def myfunction(x):

	for row in range(x,0,-1):
		for col in range(row,0,-1):
			print(col, end=' ')
		print('')


myfunction(8)