
value = int(input("what is the product of 7 * 24 ?"))
while value != 168:
    print("Your Answer is wrong try again..")
    value = int(input("what is the product of 7 * 24 ?"))
print("You answered this Question correctly")

def looping(number):
    for i in range(number,0,-1):
        for j in range(i,0,-1):
            print(j, end=' ')
        print('')
looping(5)
