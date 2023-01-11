for i in range(45, 210):
    if i == 100:
        continue
    elif i == 205:
        break
    print(i)

userinput = int(input("what is the product of 7 * 24 ?"))
while userinput == 168:
    print("You answered this Question correctly")
    break
else:
    print("Your Answer is wrong try again..")
    userinput = input("what is the product of 7 * 24 ?")


def patter(x):
    for i in reversed(range(1, x + 1)):
        for j in reversed(range(1, i + 1)):
            print(j, end=' ')
        print("")


patter(5)
