
# coding: utf-8

# In[1]:


# Addation of a two number without + operator
def Add_no(x,y):
    while(y!=0):
        carry = x&y
        x=x^y
        y= carry<<1
    return x


# In[2]:


Add_no(2,4)

