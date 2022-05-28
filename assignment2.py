#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
Ans:Thier are two boolean data type True And False 


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
Ans:
    There are three basic Boolean search commands: AND, OR and NOT.


# In[ ]:


get_ipython().set_next_input('3. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 >4) and (3 == 5)
Ans=False
not (5 > 4)
Ans=False
(5 > 4) or (3 == 5)
Ans=True
not ((5 > 4) or (3 == 5))
Ans=False
(True and True) and (True == False)
Ans=False
(not False) or (not True)
Ans:True
    


# In[ ]:


get_ipython().set_next_input('4. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
Ans:
   less than (<) ,greater than (>) ,less than or equal to (<=) ,greater than or equal to (>=),equa;l to (==) ,not equal to (!=) are the six comparision operators


# In[ ]:


How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one
Ans:
    The “=” is an assignment operator is used to assign the value on the right to the variable on the left. The '==' operator checks whether the two given operands are equal or not. If so, it returns true. Otherwise it returns false


# In[9]:


##7. Identify the three blocks in this code:
spam = 0
if spam==10:
    print("eggs")
    if spam > 5:
        print("beacon")
else:
    print('ham')
    print('spam')
    print('spam')


# In[25]:


##8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints.Greetings! if anything else is stored in spam.
spam =1
if spam==1:
    print("Hello")
if spam ==2:
    print("Howdy")
else:
    print('Greetings!')


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
Ans:
    i button is used to interupt the kernel


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
Ans:
    The difference =between break and continue is the break ends the innerclose loop to futher itration and the continue is used to continuation of the loop to futher itaration to happen.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans:The range(10) function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a 10.
    while the range(0,10) function returns a sequence of numbers, starting from 0 enter by manully at first place, and increments by 1 (by default), and stops before a 10.
    and The range(0,10,1) function returns a sequence of numbers, starting from 0 , and increments by 1 , and stops before a specified number.


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


# In[28]:


for i in range(1,11):
    print (i)


# In[35]:


n=1
while n<=10:
    print(n, end=' ')
    n= n+1


# In[ ]:


13. If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')
Ans:The function can be called by spam.bacon()

