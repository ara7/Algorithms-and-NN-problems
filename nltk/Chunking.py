#!/usr/bin/env python
# coding: utf-8

# In[4]:


nltk.download('brown')


# In[5]:


import nltk
import numpy as np
from nltk.corpus import brown


# In[6]:


words = ['table', 'probably', 'wolves', 'playing', 'is', 'dog', 'the', 'beaches', 'grounded', 'dreamt', 'envision']


# In[9]:


#spliting a text into chunk
def splitter(data, num_words):
    words = data.split(' ')
    output = []
    current_count = 0
    current_words = []
    for word in words:
        current_words.append(word)
        current_count += 1
        
        if current_count == num_words:
            output.append(' '.join(current_words))
            current_words = []
            current_count = 0
        output.append(' '.join(current_words))
    return output


# In[16]:


if __name__=='__main__':
    data = ' '.join(brown.words()[:10000])


# In[14]:


num_words = 1700
chunks = []
counter = 0


# In[15]:


text_chunks = splitter(data, num_words)
print("Number of text chunks=", len(text_chunks))


# In[ ]:




