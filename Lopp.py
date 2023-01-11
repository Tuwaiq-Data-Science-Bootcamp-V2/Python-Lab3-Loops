# q1

for i in range(45,210):

    if i == 100:
        continue
    if i == 205:
        break
    print(i)
#q2

while True:
    x = input("what is the product of 7 * 24 ?")
    p = int(x)
    if p == 168:
        print("You answered this Question correctly")
    else:
        print("Your Answer is wrong try again..")

# q3
a = int(input("Enter the number you want: "))
def check(a:int):
    for i in range(a , 0, -1):
        for j in range(i, 0,-1):
            print(j, end=" ")
        print("")
check(a)