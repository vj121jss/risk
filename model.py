#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
df=pd.read_csv('bankdata.csv')


# In[20]:


df.drop('Unnamed: 0',axis=1,inplace=True)


# In[21]:


X=df.drop('default',axis=1)


# In[22]:


y=df['default']


# In[23]:


from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(max_iter=1000)
lr.fit(X,y)


# In[24]:


# it help to get predicted value of hosue  by providing features value 
def predict_risk(age,ed,employ,address,income,debtinc,creddebt,othdebt):

  x =np.zeros(len(X.columns)) 

  x[0]=age
  x[1]=ed
  x[2]=employ
  x[3]=address
  x[4]=income  
  x[5]=debtinc
  x[6]=creddebt
  x[7]=othdebt
    
  return lr.predict([x])[0] 


# In[27]:


print(predict_risk(age=27,ed=1,employ=10,address=6,income=31,debtinc=17.3,creddebt=1.362202,othdebt=4.000798))


# In[ ]:




