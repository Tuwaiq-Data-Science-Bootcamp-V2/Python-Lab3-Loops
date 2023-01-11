
for x in range(45, 210,-100):
    if x != 100:
        print(x)
        if x == 205:
            break

#user answer to 7 * 24
answer = int(input("what is the product of 7 * 24 ?"))
#while loop asking the user what is 7*24
while True:
    if answer != (7*24):
        print("Your Answer is wrong try again..")
        answer = int(input("what is the product of 7 * 24 ?"))
    else:
        print("You answered this Question correctly")
        break

