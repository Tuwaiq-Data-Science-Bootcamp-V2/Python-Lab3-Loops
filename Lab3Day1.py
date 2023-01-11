for i in range(45, 210):
    if i == 100:
        continue
    elif i == 205:
        break
    print(i)

userinput = input("what is the product of 7 * 24 ?")
while userinput == 168:
    print("You answered this Question correctly")
else:
    print("Your Answer is wrong try again..")
    userinput = input("what is the product of 7 * 24 ?")


