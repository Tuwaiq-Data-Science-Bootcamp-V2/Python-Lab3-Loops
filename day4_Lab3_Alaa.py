#!/usr/bin/env python
# coding: utf-8

# #### 1) Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205.

# In[34]:


for i in range(45,210):
    if i ==100:
        continue
    elif i == 205:
        break
    else:
        print(i)
    


# #### 2) Using a while loop and input, do the following:
# #### Ask the the user : "what is the product of 7 * 24 ?"
# #### check if the answer is right then exit the loop and print "You answered this Question correctly".
# #### if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.

# In[182]:


x=7
y=24
z = x*y
while (True) :
    ques = input("What is the product of 7 * 24?:  ")
    if int(ques) == z:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")   


# #### 3)Create a function that takes one parameter of type int, then it prints out the result formatted like the following pattern (if we give it 5 for example):
# #### 5 4 3 2 1
# #### 4 3 2 1
# #### 3 2 1
# #### 2 1
# #### 1

# In[162]:


def my_func():
    N = input("Enter any number")
    x= list(range(1,int(N)+1))
    x.reverse()
    for i in range(int(N)):
        print(str(x)[1:-1].replace(',',''))
        x.pop(0)   


# In[163]:


my_func()


# In[180]:


def my_func():
    N = input("Enter any number: ")
    x= list(range(1,int(N)+1))
    x.reverse()  
    for i in range(int(N)):
        res = ''
        for j in x:
            res=res+ ' '+ str(j)
        print(res)
        x.pop(0)


# In[181]:


my_func()

