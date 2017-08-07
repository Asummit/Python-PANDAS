import pandas as pd

#Creating a DataFrame
from pandas.io.tests.json.test_pandas import cat

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

# Modifying the values of any column in the DataFrame may cause changes to the original DataFrame as well.
# For example changing the values of COST column here changes the COST values in 'df' DataFrame as well.
costs = df['Cost']
print costs

costs += 2                        # Increasing values of COST by +2
print costs

print df                          # Changed values of COST can be seen in original df DataFrame


# Importing a CSV file to play with...

s = open('C:\Users\Summit\Desktop\Olympics.csv')
df = pd.read_csv(s)
print df.head()

#setting index column as = 0th column.. which is the name of the countries.. and skipping first row..
df = pd.read_csv('C:\Users\Summit\Desktop\Olympics.csv', index_col = 0, skiprows=1)
print df.head()

# all of the columns in the dataset..
print df.columns

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


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# Querying in NumPy and Pandas

# Boolen Masking:
# Boolean masking is the heart of fast and efficient querying in NumPy.
# It's analogous a bit to masking used in other computational areas.
# A Boolean mask is an array which can be of one dimension like a series,
# or two dimensions like a DataFrame, where each of the values in the array are either true or false.
# This array is essentially overlaid on top of the data structure that we're querying.
# And any cell aligned with the true value will be admitted into our final result,
# and any sign aligned with a false value will not.
# Boolean masking is powerful conceptually and is the cornerstone of efficient NumPy and pandas querying.

# create a DataFrame of only those countries who have won a gold at a summer games.
# We see that the resulting DataFrame keeps the original indexed values,
# and only data from countries that met the condition are retained.
# All of the countries which did not meet the condition have NaN data instead.
print df['Gold'] > 0

only_gold = df.where(df['Gold'] > 0)
print only_gold.head()

