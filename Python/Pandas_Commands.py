# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 21:13:59 2018

@author: Ting Yu Dell
"""

import pandas as pd
import os


#comparing sum() with a list comprehension to a generator comprehension using the %time magic.
%time sum([x for x in range(100000)])

# Summary of magic functions (from %lsmagic):
%magic
%quickref

# Render our plots inline
%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })


# EDA Section
df2.dtypes
df.head()
df.tail(3)

df.index
df.columns
df.values
df.describe()

# Transposing your data:
df.T
# Sorting by an axis:
df.sort_index(axis=1, ascending=False)
# Sorting by values:
df.sort_values(by='B')

# Selection
df['A']
df[0:3]
df['20130102':'20130104']

# Selection by Label
df.loc[dates[0]]
df.loc[:,['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc['20130102',['A','B']]
df.loc[dates[0],'A']

# Selection by Position
df.iloc[3]
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
# For slicing rows explicitly:
df.iloc[1:3,:]
# For slicing columns explicitly:
df.iloc[:,1:3]
df.iloc[1,1]

# Boolean Indexing
df[df.A > 0]
df[df.iloc[:, 0] > 0]

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]


# Setting values by label:
df.at[dates[0],'A'] = 0
#Setting values by position:
df.iat[0,1] = 0

df['D']
df.loc[:,'D'] = np.array([5] * len(df))

# To drop any rows that have missing data.
df1.dropna(how='any')
# Filling missing data.
df1.fillna(value=5)
pd.isna(df1)


# Apply
# Applying functions to the data:
df.apply(np.cumsum)

df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

# Join
# SQL style merges. See the Database style joining section.
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')

# Append
s = df.iloc[3]
df.append(s, ignore_index=True)

#Grouping
#By “group by” we are referring to a process involving one or more of the following steps:
#Splitting the data into groups based on some criteria
#Applying a function to each group independently
#Combining the results into a data structure

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
'C' : np.random.randn(8),
'D' : np.random.randn(8)})

df.groupby('A').sum()
df.groupby(['A','B']).sum()

# Time Series
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample('5Min').sum()
ts_utc = ts.tz_localize('UTC')

ps = ts.to_period()
ps.to_timestamp()

ts = ts.cumsum()
ts.plot()

# On a DataFrame, the plot() method is a convenience to plot all of the columns with labels:
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])

df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc='best')

