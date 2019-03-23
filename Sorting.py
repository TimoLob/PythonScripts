#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import time
values = np.array([random.randint(0,100) for _ in range(10)])


# In[2]:


print(values)


# In[104]:


def qsort(values,low,high):
    if high<=low:
        return
    
    midpoint = partition(values,low,high)
    #print(low,midpoint,high)
    qsort(values,low,midpoint-1)
    qsort(values,midpoint+1,high)


# In[105]:


def partition(values,low,high):
    pivot = values[high]
    #print("partitioning from {} to {}".format(low,high))
    #print("pivot={}".format(pivot))
    left = low
    right = high-1
    while right > left:
        if values[left]>=pivot:
            if values[right]<pivot:
                swap(values,left,right)
                #print("swapped {} and {}".format(left,right))
            else:
                right-=1
        else:
            left+=1   
        #print(left,right)
    
    if values[left]>=pivot:
        swap(values,left,high)
        return left
    else:
        swap(values,left+1,high)
        return left+1
    

    
    


# In[106]:


def swap(values,a,b):
    #print("swap",a,b)

    tmp=values[a]
    values[a]=values[b]
    values[b]=tmp
    #print(values)
    #return values


# In[107]:


def quicksort(values):
    return qsort(values,0,len(values)-1)


# In[112]:


values = [random.randint(0,100) for _ in range(10)]
print(values)
quicksort(values)
print(values)


# In[109]:


#test quicksort
error = False
for i in range(100):
    values = np.array([random.randint(0,100) for _ in range(10)])
    print(values)
    quicksort(values)
    print(values)
    prev = values[0]
    for i in range(len(values)):
        if values[i]<prev:
            print("ERROR")
            error = True
            
print(error)


# In[110]:


values = np.array([7,78, 39, 66, 39, 56, 23, 23, 39, 41])
quicksort(values)
print(values)


# In[144]:


# test time
def test(sortingFunction,n):
    
    times = []
    for i in range(n):
        print(i)
        values = [random.randint(0,1000000) for _ in range(10000)]
        start = time.time()
        sortingFunction(values)
        end = time.time()
        error = False
        for i in range(len(values)):
            if values[i]<prev:
                print("ERROR")
                error = True
        if not error:
            times.append(end-start)
                
    return np.median(times)


# In[145]:


test(quicksort,100)


# In[146]:


test(sorted,100)


# In[147]:


def bubblesort(values):
    for n in range(len(values),1,-1):
        for i in range(0,n-1):
            if values[i] > values[i+1]:
                swap(values,i,i+1)


# In[148]:


test(bubblesort,2)


# In[ ]:




