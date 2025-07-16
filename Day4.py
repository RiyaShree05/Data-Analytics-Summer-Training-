#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("calculate simple interest")
def SI(p,r,t):
    print((p*r*t)/100)
SI(45,4,6)


# In[20]:


print("Sum of natural number")
def Naturalnumber(a,b):
    sum=0
    for i in range(a,b):
        sum+=i
    print(sum)
Naturalnumber(1,51)


# In[23]:


print("Table of 2")
def table(num):
    for i in range(1,11):
        print(f"{num} x {i}={num*i}")
table(2)        


# In[26]:


print("sum of odd number")
def sum (a,b):
    sum=0
    for i in range(a,b):
        if i%2!=0:
            sum+=i
    print(sum)
sum(1,51)    


# In[31]:


def add(a,b):
    c=a+b
    print(c)
add(10,7)    


# In[32]:


def add(a,b):
    c=a+b
    return c
add(10,7)    


# In[33]:


add=lambda a,b:a+b
add(10,7)


# In[43]:


def add(a,b):
    def add_1(a,b):
        c=a+b
        print(c)
    add_1(12,1)
    x=a+b
    print(x)
add(10,5)


# In[45]:


try:
    num1=int(input("enter num1"))
    num2=int(input("enter num2"))
    result=num1/num2
except ZeroDivisionError:
    print("Error: cannot be divided by zero")
except ValueError:
    print("Error: please enter valid integer only")
else:
    print("Result is:",result)


# In[47]:


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))    


# In[48]:


a=input("enter a string")
reverse=a[::-1]
reverse


# In[14]:


String=input("enter a string")
def reverse():
    print(String[::-1])
reverse()    


# In[4]:


def square(num):
    if num==1:
        return 1
    return num*num
print(square(2))


# In[7]:


def sum(a,b):
    c=a+b
    return c
sum(10,2)    


# In[11]:


def even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
even(2)        


# In[15]:


type(lambda x: x)


# In[20]:


def largest(num):
    largest = num[0] 
    for n in num:
        if n> largest:
            largest = n
    return largest
list = [1,2,3,4,5]
print("Largest number is:", largest(list))


# In[21]:


def foo(): pass
print(foo())


# In[24]:


def countvowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    return count
a = input("Enter a string: ")
print("Number of vowels:", countvowels(a))


# In[29]:


n = int(input("Enter the number of terms: "))
def Fibonacci(num):
    a, b = 0, 1
    print("Fibonacci series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
Fibonacci(n)


# In[ ]:




