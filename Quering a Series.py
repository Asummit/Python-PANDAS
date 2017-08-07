#Quering a Series
import pandas as pd
import numpy as np

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print s

# If you wanted to see the fourth country on this, we would use the iloc attribute with the parameter 3.
# If you wanted to see which country has golf as its national sport,
# we would use the loc attribute with parameter golf.
# Keep in mind that iloc and loc are not methods, they are attributes.
# So you don't use parentheses to query them, but square brackets instead,
# which we'll call the indexing operator.
# Though in Python, this calls get and set an item methods depending on the context of its use.

print s.iloc[3] #if you want to query by the Index Number
print s.loc['Golf'] #if you want yo query by Index Lable



# This might seem a bit confusing if you're used to languages where encapsulation of attributes,
# variables, and properties is common, such as in Java.
# Pandas tries to make our code a bit more readable and provides a sort of smart syntax,
# using the indexing operator directly on the series itself. For instance, if you pass in an integer parameter,
# the operator will behave as if you want it to query via the iloc attribute.
# If you pass in an object,it will query as if you wanted to use the label based loc attribute.

#Example
print s[3] #by integer Parameter
print s['Golf'] #by object as a Parameter or Index Lable


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


# Working with DATA
# suppose we want a SUM of the number in the series...

s = pd.Series([212,342,243.67])
# Pandas when sees any floating point value in the Series,
# it automatically converts other values to the same Datatype.
print s

# Normal Approach to find the sum the values in the series..
total = 0
for item in s:
    total+= item
print(total)

# Pandas and the underlying NumPy libraries support a method of computation called vectorization.
# Vectorization works with most of the functions in the NumPy library, including the sum function.
# Example..
total = np.sum(s)
print(total)


#Creating a list of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
print s.head()
print len(s)

#Broadcasting
#Related feature in Pandas and NumPy is called broadcasting.
#With broadcasting, you can apply an operation to every value in the series, changing the series.

s += 2
print s.head()  #adding 2 to the series of object we could do so quickly using the += operator directly on the series object.


#Procedural way..
for label, value in s.iteritems():
    s.set_value(label, value+2)
print s.head()

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# The .loc attribute lets you not only modify data in place, but also add new data as well.
# If the value you pass in as the index doesn't exist, then a new entry is added.
# And keep in mind, indices can have mixed types.
# While it's important to be aware of the typing going on underneath,
# Pandas will automatically change the underlying NumPy types as appropriate.
s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
print s                    #Mixed types for data values or index labels are no problem for Pandas.


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------


# Sometimes index values are not unique, and this makes data frames different,
# conceptually, that a relational database might be.
# It's possible to create a new series object with multiple entries for cricket,
# and then use append to bring these together. There are a couple of important considerations when using append.
# First, Pandas is going to take your series and try to infer the best data types to use.
# In this example, everything is a string, so there's no problems here.


original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'],
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])

# The append method doesn't actually change the underlying series.
# It instead returns a new series which is made up of the two appended together.
# We can see this by going back and printing the original series of values and seeing that they haven't changed.
all_countries = original_sports.append(cricket_loving_countries)

print original_sports
print cricket_loving_countries
print all_countries
print all_countries.loc['Cricket']


