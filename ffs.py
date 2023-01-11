#sol1
for i in range(45,210):
    if(i==100):
        continue
        if(i==205):
            break
            print(i)
#sol2
x=0
while(x!=168):
    x=int(input("what is the product of 7*24?")
          if(x!=168):
              print("you answer this question correctly")
          else:
              print("your answer is wrong try again")

 # sol3
def countDown(num: int):
    while (num != 0):
        for i in reversed(range(1, num + 1)):
            print(i, end=" ")
        print("\n")
        num -= 1