# Both series and DataFrames can have indices applied to them.
# The index is essentially a row level label, and we know that rows correspond to axis zero.
# In our Olympics data, we indexed the data frame by the name of the country.
# Indices can either be inferred, such as when we create a new series without an index,
# in which case we get numeric values, or they can be set explicitly...


# Set_index function...
# This function takes a list of columns and promotes those columns to an index.
# Set index is a destructive process, it doesn't keep the current index.

# Importing CSV file..
import pandas as pd
s = open('D:\Python Assignments\Pandas\DataFrame Indexing, Loading, Quering\Olympics.csv')
df = pd.read_csv(s)
print df.head()

#setting index column as = 0th column.. which is the name of the countries.. and skipping first row..
df = pd.read_csv('D:\Python Assignments\Pandas\DataFrame Indexing, Loading, Quering\Olympics.csv', index_col = 0, skiprows=1)
print df.head()

# Cleaning and editing Column table names
# We can change the values of the column names by iterating over this list
# and calling the rename method of the data frame.
# set the ever-important 'inplace' parameter to 'True' so Pandas knows to update this data frame directly.

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='N':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)
print df.head()


# Let's say that we don't want to index the DataFrame by countries,
# but instead want to index by the number of gold medals that were won at summer games.
# First we need to preserve the country information into a new column.
# We can do this using the indexing operator or the string that has the column label.
# Then we can use the set_index to set index of the column to summer gold medal wins.

df['country'] = df.index
df = df.set_index('Gold')
print df.head()

# Re-Setting index
# We can get rid of the index completely by calling the function reset_index.
# This promotes the index into a column and creates a default numbered index.

df = df.reset_index()
print df.head()



# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Multi-Level Indexing
# One nice feature of pandas is that it has the option to do multi-level indexing.
# This is similar to composite keys in relational database systems.
# To create a multi-level index, we simply call set index and give it a list of columns that we're interested in promoting to an index.
# Pandas will search through these in order, finding the distinct data and forming composite indices.
# A good example of this is often found when dealing with geographical data which is sorted by regions or demographics.

# New Data Set imported for Multi-Level indexing...
#  In particular, this is a breakdown of the population level data at the US county level.
# It's a great example of how different kinds of data sets might be formatted when you're trying to clean them.
df = pd.read_csv('D:\Python Assignments\Pandas\Indexing DataFrames and Missing Values\census.csv')
print df.head()



# In this DataFrame, we see that the possible values for the sum level are using the unique function on the DataFrame.
print df['SUMLEV'].unique()  #Unique function to find out unique values in a column...

# There are only two different values, 40 and 50.
# Let's get rid of all of the rows that are summaries at the state level and just keep the county data.
# Also while this data set is interesting for a number of different reasons,
# Let's reduce the data that we're going to look at to just the total population estimates and the total number of births.

df = df [df['SUMLEV'] == 50]
print df.head()

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
print df.head()

# The US Census data breaks down estimates of population data by state and county.
# We can load the data and set the index to be a combination of the state and county values and see how pandas handles it in a DataFrame.
# We do this by creating a list of the column identifiers we want to have indexed.
# And then calling set index with this list and assigning the output as appropriate.
# We see here that we have a dual index, first the state name and then the county name.

df = df.set_index(['STNAME', 'CTYNAME'])
print df.head()

# Querying Multi-Level indexed coloumns...
df.loc['Michigan', 'Washtenaw County'] # for 1 county of a STATE
df.loc[ [('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County')]] # for 2 counties of a STATE..

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# Question...
# Reindex the purchase records DataFrame to be indexed hierarchically, first by store,
# Then by person. Name these indexes 'Location' and 'Name'. Then add a new entry to it with the value of.
# Name: 'Kevyn', Item Purchased: 'Kitty Food'
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print df


# Missing Values
# When you use statistical functions on DataFrames, these functions typically ignore missing values.
# For instance if you try and calculate the mean value of a DataFrame,
# the underlying NumPy function will ignore missing values.

# One of the handy functions that Pandas has for working with missing values is the filling function, fillna.
# This function takes a number or parameters, for instance,
# you could pass in a single value which is called a scalar value to change all of the missing data to one value.

df.fillna  # To fill the NA values..
df.ffill() #is for forward filling and it updates an na value for a particular cell with the value from the previous row.
           # It's important to note that your data needs to be sorted in order for this to have the effect you might want.
df.bfill() # Backward fill..


# In Pandas we can sort either by index or by values.
# Here we'll just promote the time stamp to an index then sort on the index.
#Example:

df = df.set_index('time') #Indexing according to the time..
df = df.sort_index() # Sorting
print df

#Resetting
df = df.reset_index()
df = df.set_index (['time', 'user']) #Multi Indexing...
print df




