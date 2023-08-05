#!/usr/bin/env python
# coding: utf-8

# Q-1 What is an Exception handling in python? Write the difference between Exception handling and syntax errors.

# Ans-1 An Excetpion in python is an incident that happens while excuting a program that causes the regular course of the program's commands to be discrupted . When a python code comes across a condition it can't handle .it raises an exception . An object in python that describe an error is called an Exception .
# 
# SYNTAX ERROR: As the name suggests this error is caused by the wrong syntax in the code .it lead to the termination of the program.
# 
# EXCEPTIONS : Exception are raised when the program is syntactically correct ,but the code results in an

# Q-2 What happens when an exception is not handled ? Explain with an example

# Ans-2 When an exception occurs, and if you don't handle it , the program will terminate abrupty ( the piece of code after the line causing the exception will not get executed).

# In[2]:


def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is ",result)
    finally:
        print("executing finally clause")


# Q-3 Which python statements are used to catch and handle exceptions? Explain with an example.
# 

# In[3]:


''' The try and except block in python is used to catch and handle executions.'''
try:
    num=10
    deno=0
    result= num/deno
    print(result)
except:
    print("error: Denominator cannot be Zero 0")


# Q-4 Explain with an example:
# a.try and else ,
# b.finally ,
# c.raise

# In[15]:


# a. try and else
try:
    num= int(input("enter the number:"))
    assert num%2 ==0
except:
    print("Not an Even number!")
else:
    reciprocal=1/num
    print(reciprocal)

# b. finally
  
try:
    print(x)
except :
    print("something went wrong")
finally:
    print("The try except is finished")
    
# c. raise
a=5 
if a % 2 !=0 :
    raise Exception("the num should not be an odd integer")


#     Q-5 What are custom Exception in python ? Why do we need custom Exception ? Explain with an example

# In[16]:


''' 
  In python , we can define custom exceptions by creating a new class that is derived from the built-in exception class.
   To create custom exception class you define a class that inherits from built in exception class or one of its as valueerror 
    class . custom exception will add information about project - related problems.'''

class CustomException(Exception):
    """
     My custom exception class"""


# Q-6 Create a custom exception class .use this class to handle an exception.

# In[19]:


class CustomException(Exception):
 """ My custom exception class"""
    
try:
    raise CustomException("this is my custom exception")
exc


# In[ ]:




