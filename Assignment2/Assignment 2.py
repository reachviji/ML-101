
# coding: utf-8

# In[1]:


# Create an array using the method 1. array 2. arange 3. linspace
import numpy as np
a = np.array([[34,56],[56,76]])
a_arange = np.arange(3)
a_linspace = np.linspace(10,5,5)

print('Array using np.array: {}'.format(a))
print('Array using np.arange : {}'.format(a_arange))
print('Array using np.linspace : {}'.format(a_linspace))


# In[2]:


#Identify the shape and dimensions of an array

a = np.array([[2,3],[3,4],[4,5],[89,78]])
# Shape of the array
print('Shape of the array is: {}'.format(a.shape))
print('Dimensions of array is: {}'.format(a.ndim))
print('Length of the array is: {}'.format(len(a)))


# In[3]:


#Replace the values which are multiples of 5 by -1 using fancy indexing in [1,5,10,4,15,20,7,35]
a = np.array([1,5,10,4,15,20,7,35])
mask = (a%5 == 0)
a[mask] = -1
print('Replacing the values which are multiples of 5 by -1 using fancy indexing are: {}'.format(a))


# In[4]:


# Create a array and find out the sum of the elements
# Single Dim array
sing_dim = np.array([12,34,45,57])
# Sum of the elements
print('Sum of elements in single dimension array is: {}'.format(np.sum(sing_dim)))

# Two Dimension array
two_dim = np.array([[2,3],[3,4],[4,5],[89,78]])
# Sum of the elements in the array
print('Sum of elements in two dimension array is: {}'.format(np.sum(two_dim,axis = 0)))


# In[5]:


# Reshape an array np.array([1, 2, 3, 4], ndmin=2) using ravel and identify the shape, dimensions and write your conclusions
# This is a two dimensional array
a = np.array([1, 2, 3, 4], ndmin=2) 
print('The given array is: {}'.format(a))
print('The shape of given array is: {}'.format(a.shape))
print('The dimensions of given array is: {}'.format(a.ndim))
print()
# Changing it to one dimensional array using ravel
new_a = a.ravel()
# find out the new array, its shape, dimensions
print('Changed array: ')
print('The new array is: {}'.format(new_a))
print('The shape of the new array is: {}'.format(new_a.shape))
print('The dimensions of new array is: {}'.format(new_a.ndim))
print()
print('Conclusion: ravel method is used to reshape the array.\nSyntax is: numpy.ravel(a, order= C) where it returns a contiguous flattened array \nThere are other orders like A,F or K which can be used depending on the business case')


# In[6]:


# How to remove from one array those items that exist in another? a = np.array([1, 2, 3, 4, 5]) b = np.array([5, 6, 3, 1, 4])
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 3, 1, 4])

# Remove from a those elements that exists in b and display a.
# We will use np.isin method to achive this
mask = np.isin(a,b)
print('The unique elements in a are: {}'.format(a[~mask]))


# In[ ]:


# Pandas


# In[7]:


# How to combine two series into a dict 
import pandas as pd
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz')) 
ser2 = pd.Series(np.arange(26))
print('combining two series into a dictionary, we get:\n {}'.format(dict(zip(ser1,ser2))))


# In[10]:


# How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
a = pd.Series(np.random.normal(10, 5, 25))
# print('The values generated in the series are:\n {}'.format(a))
# print('Minimum value of the series is : {}'.format(a.min()))
value = a.describe()
print('The values are shown below: ')
value


# In[9]:


#  How to convert a numpy array to a dataframe of given shape? 
a = pd.Series(np.random.randint(1, 10, 35))
df = pd.DataFrame({'Value':a})
df


# In[11]:


# How to calculate the number of characters in each word in a series?
series = pd.Series(['how', 'to', 'kick', 'ass?'])
count = 0
while count < len(series):
    print('Length of the letter {} in index {} is: {}'.format(series[count],count,len(series[count])))
    count = count + 1
                                


# In[12]:


# Import csv file using pd.read_csv method, Use the weather_data.csv from the pandas folder
weather_data = pd.read_csv("weather_data.csv")
weather_data


# In[13]:


# Obtain the columns, index and shape of the above data frame.
print('the content of the weather data in terms of cloumns and index is :\n{}'.format(weather_data))
print('\nShape of the data frame is : {}'.format(weather_data.shape))


# In[14]:


# Use describe method on the dataframe and write your conclusion
weather_data.describe()


# In[15]:


# Conclusion:
print('Pandas describe() is used to view some basic statistical details like percentile, mean, std etc.\nof a data frame or a series of numeric values')

