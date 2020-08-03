#!/usr/bin/env python
# coding: utf-8

# In[7]:


import nltk;
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
 
text = "Are you curious about tokenization? Let's see how it works! We need to analyze a couple of sentences with punctuations to see it in action."


# In[3]:


#sentence tokenization
#sent_tokenize = sent_tokenize(text)
#print(sent_tokenize) #gives error


# In[8]:


word_punct_tokenizer = WordPunctTokenizer()
print ("\nWord punct tokenizer:")
print (word_punct_tokenizer.tokenize(text))


# In[9]:


#Stemming
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer


# In[10]:


words = ['table', 'probably', 'wolves', 'playing', 'is', 'dog', 'the', 'beaches', 'grounded', 'dreamt', 'envision']


# In[11]:


#Comparing stemmers
stemmers = ['PORTER', 'LANCASTER', 'SNOWBALL']


# In[19]:


stemmer_porter = PorterStemmer()
stemmer_lancaster = LancasterStemmer()
stemmer_snowball = SnowballStemmer('english')


# In[20]:


print(len(words))


# In[27]:


formatted_row = '{:>16}'*(len(stemmers)+1)
print('\n',formatted_row.format('WORD', *stemmers), '\n')


# In[28]:


for word in words:
    stemmed_words = [stemmer_porter.stem(word),
                    stemmer_lancaster.stem(word),
                    stemmer_snowball.stem(word)]
    print(formatted_row.format(word, *stemmed_words))


# In[36]:


#Lemmatization
#Noun and Verb lemmatizers
from nltk.stem import WordNetLemmatizer
lemmatizers = ['NOUN LEMATIZER', 'VERB LEMMATIZER']
lemmatizer_wordnet = WordNetLemmatizer()
formatted_row_1 = '{:>24}' * (len(lemmatizers) + 1)
print('\n', formatted_row_1.format('WORD', *lemmatizers), '\n')


# In[37]:


for word in words:
    lemmatized_words = [lemmatizer_wordnet.lemmatize(word, pos='n'), lemmatizer_wordnet(word, pos='v')]
    print(formatted_row_1.format(word, *lemmatized_words))


# In[ ]:




