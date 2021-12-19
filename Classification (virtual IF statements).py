#!/usr/bin/env python
# coding: utf-8

# # Classification (virtual IF statements)
# 
# I want to know if a Number is bigger/smaller/equal to a Random value. The result of the comparison must be recorded in a column. Here's a script that doesn't use the IF statement directly.

# In[174]:


import numpy as np
import pandas as pd 
import random


numberList = []
for i in range(1,51):
    numberList.append(i)
    i+=1
    
numberList = pd.DataFrame(numberList, columns=['numbers'])
numberList.head()


# In[173]:


x = np.random.randint(1,50, size = 50)
numberList['random'] = x 
numberList['compare'] = 'is equal to'  # default value
numberList = numberList[['numbers','compare','random']]  #rearrange cols

mask = numberList['numbers'] > numberList['random']  
numberList.loc[mask, 'compare'] = 'is bigger than'  # 'compare' = 'bigger than' IF 'numbers' > 'random'

mask = numberList['numbers'] < numberList['random']
numberList.loc[mask, 'compare'] = 'is smaller than'

numberList


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




