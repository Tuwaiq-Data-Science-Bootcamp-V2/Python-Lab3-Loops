number = int(input("Enter a number"))
def num_pyrm(a):
    for row in range(a,0,-1):
        for colmn in range(1,row+1):
            print(colmn , end=" ")
        print("\n")
num_pyrm(number)