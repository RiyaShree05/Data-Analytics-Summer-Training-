#!/usr/bin/env python
# coding: utf-8

# In[6]:


list=[1,5,7,3]
list.append(2)
print(list)


# In[7]:


list.insert(4,90)
print(list)


# In[8]:


list.extend([7,8,4])
print(list)


# In[13]:


list.pop()
print(list)


# In[14]:


list.extend([90,2,7,8])
print(list)


# In[15]:


list.remove(7)
print(list)


# In[16]:


list.pop()
print(list)


# In[17]:


list.clear()
print(list)


# In[19]:


list=[3,5,6,7,2,9,1]
list.index(5)


# In[20]:


list.count(2)


# In[22]:


list.sort()
print(list)


# In[25]:


list.reverse()
print(list)


# In[26]:


list.copy()
print(list)


# In[ ]:


PRACTICE QUESTION


# In[28]:


lst=[]
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
e=int(input("enter fifth number"))
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
lst.append(e)
print(lst)


# In[32]:


list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)


# In[34]:


list=[10,20,30,40]
list.insert(2,25)
print(list)


# In[35]:


list=[10,20,30,20,40]
list.remove(20)
print(list)


# In[40]:


list.pop()
list=[1, 2, 3, 4, 5]
print("pop item: ",list.pop())
print(list)


# In[42]:


list=[5, 10, 15, 20, 25]
list.index(15)


# In[43]:


list=[1, 2, 2, 3, 2, 4, 2]
list.count(2)


# In[50]:


list=[10, 5, 7, 3]
list.sort()
print(list)
list.reverse()
print(list)


# In[51]:


list=[1, 2, 3, 4, 5]
list.reverse()
print(list)


# In[52]:


list1=  [1, 2, 3]
list2 = list1.copy()
print(list2)
list2.append(4)
print("original list: ",list1)
print("copy list: ",list2)


# In[ ]:




