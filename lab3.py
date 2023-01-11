for i in range(45,210):
    if i == 100:
        continue
    if i == 205:
        break
    print(i)        



while True:
    x = input("what is the product of 7 * 24 ?")
    y = int(x)

    if y == 168:
        print("You answered this Question correctly")
        break

    elif y != 168:
        print("Your Answer is wrong try again..")
        continue


number = int(input("Enter number"))
def numbers(number:int):
    for i in range(number,0,-1):
        for x in range(i,0,-1):
            print(x , end=" ")
        print("")    
numbers(number)        














