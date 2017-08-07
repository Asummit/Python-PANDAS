import pandas as pd
import numpy as np

# Series() in Pandas

pd.Series
animals = ['Tiger', 'Dog', 'Cat']
print pd.Series(animals)

# Underneath panda stores series values in a typed array using the numpy library.
# This offers significant speed-up when processing data versus traditional python lists

# Example:
numbers = [1,2,3,4]
print pd.Series(numbers)  # Pandas automatically changes data_type.

# The most important is how numpy and thus pandas handle missing data.
# In Python, we have the NONE type to indicate a lack of data.
# But what do we do if we want to have a typed list like we do in the series object?

# Underneath, pandas does some type conversion. If we create a list of strings and we have one element,
# a None type, pandas inserts it as a None and uses the type object for the underlying array.
# If we create a list of numbers, integers or floats, and put in the None type,
# pandas automatically converts this to a special floating point value designated as NaN, which stands for Not_A_Number.

# Missing Data in the Array
animals = ['Tiger', 'Dog', None]
print pd.Series(animals)


# Missing Number from the Array
numbers = [1,3,2,None]
print pd.Series(numbers)  # NaN: Stands for Not_A_Number


# NaN is not None and when we try the equality test, it's false.
print np.nan == None  # Result is FALSE



# It turns out that you actually can't do an equality test of NaN to itself.
# When you do, the answer is always false.
# You need to use special functions to test for the presence of not a number,
# such as the num pi library isnan.

# Keep in mind when you see NaN, it's meaning is similar to none,
# but it's a numeric value and it's treated differently for efficiency reasons.
print np.isnan(np.nan)  # Result is TRUE..

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------


# Series Created by Dictionary..
# A series can be created from dictionary data.
# If you do this, the index is automatically assigned to the keys of the dictionary that you provided
# and not just incrementing integers.
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print s

#Once the series has been created, we can get the index object using the index attribute.
print s.index

#You could also separate your index creation from the data by
# passing in the index as a list explicitly to the series.
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
print s
print s.index



# So what happens if your list of values in the index object are not aligned with the keys in your dictionary for creating the series?
# Well, pandas overrides the automatic creation to favor only and all of the indices values that you provided.
# So it will ignore it from your dictionary, all keys, which are not in your index,
# and pandas will add non type or NaN values for any index value you provide,
# which is not in your dictionary key list.
# In this example, we pass in a dictionary of four items
# but only two are preserved in the series object because of the index list.
# We see that hockey has been added but since it's also in the index list, it has no value associated with it.

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print s  #NaN for Hockey...

