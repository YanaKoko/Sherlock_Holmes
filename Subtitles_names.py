#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[59]:


my_dir = ".\subtitles"
my_subs = os.listdir(path=my_dir)
print(my_subs)


# In[86]:


def make_sentences(text):
    new_text = []
    text_two = []
    text_three = []
    text_four = []
    text_five = []
    punct = '?!."'
    text_one = text.split('.')
    for t in text_one:
        text_two.extend(t.split('?'))
    for t in text_two:
        text_three.extend(t.split('!'))
    for t in text_three:
        text_four.extend(t.split('«'))
    for t in text_four:
        text_five.extend(t.split(':'))
    for t in text_five:
        new_text.extend(t.split('@'))
    return new_text


# In[87]:


punct = '?!."'
for s in my_subs:
    my_path = os.path.join(my_dir, s)
    print(my_path)
    names = []
    with open (my_path, encoding = 'utf-8') as file:
        f = file.read()
        my_sentences = make_sentences(f)
        for s in my_sentences:
            my_s = s.split(' ')
            #print(my_s)
            new_my_s = []
            for n in my_s:
                if not n == '':
                    new_my_s.append(n)
            #print(new_my_s)
            for word in new_my_s[1:]:
                if word != '':
                    if word[0].isupper() and len(word) >2:
                        print(word)
                        print(s)
                        names.append(word)
    print(names)


# In[ ]:




