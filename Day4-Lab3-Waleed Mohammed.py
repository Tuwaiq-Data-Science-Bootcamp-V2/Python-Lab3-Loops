#Day4 Lab1 Loop

for x in range(45,210):
	if x == 100:
		continue
	elif x == 205:
		break


#------2) the second question----

while True:
	User = int(input("what is the product of 7*24 ?"))
	if User == 168:
		print('You answered this Question correctly')
		break
	else:
		print('Your Answer is wrong try again..')
		continue

