#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#loops


# In[ ]:


while True:
    user_input=input("type 'q' to quit:")
    if user_input=='q':
        print("exited loop!")
        break
    else:
        print("you typed",user_input)


# In[2]:


password="open1234"
attempts=3
while attempts>0:
    user_input=input("enter passwaord:")
    if user_input==password:
        print("access granted")
        break
    else:
        attempts-=1
        print(f"wrong password! {attempts} attempts left")


# In[3]:


password="hello12"
for attempts in  range(3):
    user_input=(input("enter password:"))
    if user_input==password:
        print("access granted")
        break
    else:
        print(f"wrong password!{2-attempts} attempts left")
                


# In[6]:


for i in range(1,6):
    if i==3:
        continue
    print(i)


# In[16]:


for i in range(1,11):
    if i==5:
        continue
    elif i==8:
        break
    else:
        print(i)


# In[26]:


password="hello12"
for attempts in  range(5):
    user_input=(input("enter password:"))
    if attempts==2:
        continue
    elif user_input==password:
        print("access granted")
        break
    else:
        print(f"wrong password!{4-attempts} attempts left")


# In[27]:


def riya():
    print("hello form function")
riya()


# In[28]:


def sum():
    a=23
    b=34
    c=a+b
    print(c)
sum()    


# In[9]:


num="1234"
reverse=num[::-1]
reverse


# In[1]:


print(3 + 2 * 2)


# In[2]:


print(4 != 5)


# In[3]:


5 > 3 and 2 < 1


# In[4]:


10 / 5


# In[5]:


print(3**2)


# In[9]:


x = 5; 
if x > 3:
    print('Yes')


# In[10]:


if 5 < 10:
    print('OK')


# In[14]:


'python'[0]


# In[15]:


len('hello')


# In[16]:


print('Hello, World!')


# In[17]:


a=int(input("enter num1"))
b=int(input("enter num2"))
c=(a+b)
print(c)


# In[22]:


num=int(input("enter a number"))
if num%2==0:
    print("even")
else:
    print("odd")


# In[28]:


num1=int(input("enter num1"))
num2=int(input("enter num2"))
if (num1>num2):
    print("first number is largest:",num1)
else:
    print("second number is largest:",num2)


# In[31]:


num=int(input("enter a number"))
if num>0:
    print("positive")
else:
    print("negative")


# In[1]:


num=1
while num<=10:
    print(num)
    num+=1


# In[5]:


num=int(input("enter a number"))
for i in range(1,11):
    print(f"{num} X {i}={num*i}")


# In[8]:


num=int(input("enter a number"))
a=1
for i in range(1,num+1):
    a=a*i

print("factorial is:",a)


# In[10]:


num=int(input("enter a num"))
if num%num==0:
    print("prime number")


# In[ ]:




