import pandas as pd

# Creating a dataframe

# p1 = pd.Series({'Name': 'Summit', 'Item': 'Milk', 'Cost': '5.00'})
# p2 = pd.Series({'Name': 'Amit', 'Item': 'Biscuit', 'Cost': '4.00'})
#
# f = pd.DataFrame([p1, p2], index=['Store1', 'Store2'])
# print f.head()

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
print df.head()

# Retreving the elements of the dataframe
print df.loc['Store 2']

# Finding the type of the function
print type(df.loc['Store 2'])

# Indices and Column name can be Non-unique (Horzontal or Vertical)
# Exaple:
print df.loc['Store 1'] # 2 purchase records at different rows..

# We can quickly select database on multiple Axis
# like from the example if we want just the cost from the Store 1.
# Example:
print df.loc['Store 1', 'Cost'] # Index name and Column name is required.

# Transposing the DataFrame
print df.T

# Here .loc takes ROW INDEX and COLUMN NAME as parameters,
# Chaining gives you the COPY of the data not the VIEW...  time complexity issue..
print df.loc['Store 1']['Cost']

# Slicing in loc Function.. with selecting all ROWS with : and multiple COLUMNS..
# The key concepts to remember are that the rows and columns are really just for our benefit.
# Underneath this is just a two axis labeled array, and transposing the columns is easy.
print df.loc[:, ['Name', 'Cost']]



# Droping or Deleting Data.. This takes a single parameter (Index or ROW lable..)
print df.drop('Store 1')  # it just gives you the Copy of the modified dataframe keeping the original Dataframe intact.
print df                  # our original DataFrame is still intact.


# Copying the dataframe..
ddf = df.copy()
ddf = ddf.drop('Store 1') # Drop has two interesting optional parameters.
print ddf                 # The first is called 'inplace', and if it's set to true - inplace = True,
                          # The DataFrame will be updated in place, instead of a copy being returned.


# Permanently deleting a column, direct effect on DataFrame
del ddf['Name']
print ddf

# Adding a new column...
df['Location'] = None # This broadcast the default value(None) to the new column...
print df