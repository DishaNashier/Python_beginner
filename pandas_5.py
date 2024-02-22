# -*- coding: utf-8 -*-
"""pandas_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q8WJ9aZnleJbRTTzf4p5-cKF07qXAK47
"""

# Agenda:
# Handling Missing Values (Data Cleaning)
# Date time functions
# String Functions

import numpy as np
import pandas as pd

!gdown 173A59xh2mnpmljCCB9bhC4C5eP2IS6qZ

data=pd.read_csv('Pfizer_1.csv')

data

data_melt= pd.melt(data,id_vars=['Date',"Drug_Name","Parameter"],
                   var_name="time",
                   value_name="reading")

data_melt

data_tidy=data_melt.pivot(index=["Date","time","Drug_Name"],columns="Parameter",values="reading")
data_tidy=data_tidy.reset_index()
data_tidy.columns.name= None

data.head()

data_tidy

# Detecting the missing values -
#  1) NaN "Not a Number" - Numerical columns
#  2) None -  Categorical values

pd.Series([1,5,np.nan,7,9,None])

data.isna().head() # .isnull is an alias for .isna

data.isnull().head()

data.isnull().sum()
#print True for both NaN and Null
#default axis=0

data.isnull().sum(axis=1)

# Total number of missing values -> sum+sum
data.isnull().sum(axis=1).sum()

# Two ways of handling missing values
# 1.Deleting, 2.Imputing -> estimating, fillna(0), fillna(avg) -> more prefered

data.dropna()
# only four rows in output because other rows got deleted
#draw back of .dropna(), entire row/column gets dropped

data.shape

data.dropna(axis=1)

# dropping is not the best thing to do , problem - loss of data

# imputing/estimating

data.fillna(0)

data.fillna(0).isna().sum() #all missing values are filled with 0

data.fillna(0).head()

data

data["1:30:00"].fillna(0)

data["1:30:00"].mean()

data["1:30:00"].fillna(data["1:30:00"].mean())

#Filling NaN values with average of temperature and pressure grouped by drug name

def temp_mean(group):
  group['Temp_avg']=group['Temperature'].mean()
  return group

data_tidy=data_tidy.groupby(["Drug_Name"]).apply(temp_mean)

def pressure_mean(group):
  group['Pressure_avg']=group['Pressure'].mean()
  return group

data_tidy=data_tidy.groupby(["Drug_Name"]).apply(pressure_mean)

data_tidy.isna().sum()

data_tidy

data_tidy.isna().sum()

data_tidy.iloc[:20]

data_tidy["Temperature"].fillna(data_tidy["Temp_avg"],inplace=True)

data_tidy.isna().sum()

data_tidy["Pressure"].fillna(data_tidy["Pressure_avg"],inplace=True)

data_tidy.isna().sum()

data_tidy.iloc[:20]

data_tidy["Pressure"].round(2)

# Example
sample = pd.Series(['1', '2', '3', np.NaN, None])
sample.fillna(0)

"""**pd.cut**


---


It is a function in pandas that is used for binning data into discrete intervals. It is particularly useful when you have a continuous variable and you want to categorize it into bins or intervals. This can be helpful in various data analysis and visualization tasks.
"""

# pd.cut
# numerical -> categorical

data_tidy["Temperature"].min(),data_tidy["Temperature"].max()

temp_points=[5,20,35,50,60]
temp_labels=['low','medium','high','vhigh']
data_tidy["temp_cat"]=pd.cut(data_tidy["Temperature"],bins=temp_points,labels=temp_labels)

data_tidy.head()

data_tidy["temp_cat"].value_counts()

"""**.str accessor**


---


is used to apply string methods to each element of a Series containing strings. This allows you to perform various string operations on the elements of a column in a pandas DataFrame.

upper(), lower(), capitalize(), strip(), replace(), etc.
"""

data_tidy["Drug_Name"].str

data_tidy["Drug_Name"].str.lower()

data_tidy["Drug_Name"].str.upper()

data_tidy["Drug_Name"].str.split()

data_tidy[data_tidy["Drug_Name"].str.contains('hydrochloride')]

data_tidy["Date"].str.split("-").apply(lambda x:x[-1])

#merging date time column
data_tidy["timestamp"]=data_tidy["Date"]+" "+data_tidy["time"]

data_tidy

data_tidy.drop(columns=["Date","time"],inplace=True)

data_tidy.head()

data_tidy.dtypes

""" the **to_datetime** function


---


 It is used to convert a variety of date-like objects into pandas DateTime objects. It is a powerful function that can parse different formats of date strings or convert other types of objects, such as integers or floats representing timestamps.
"""

data_tidy["timestamp"]=pd.to_datetime(data_tidy["timestamp"])

data_tidy.dtypes

ts=data_tidy["timestamp"][0]
ts

ts.year,ts.month,ts.month_name(),ts.day_name()

"""**.dt accessor**



---


In pandas, the .dt accessor is used to access the datetime properties of a Series or DataFrame containing datetime values. This allows you to perform various operations on the datetime values.
"""

data_tidy["timestamp"].dt

data_tidy["timestamp"].dt.year

data_tidy["timestamp"].dt.month_name()

data_tidy["Date"]=data_tidy["timestamp"].dt.day

data_tidy.head()

"""**Reshuffling column position**


---


"""

#reshuffling column position
cols=list(data_tidy.columns)
cols

cols.remove('timestamp')
cols.insert(0,'timestamp')

cols

data_tidy=data_tidy[cols]

data_tidy

data_tidy.head()

"""**Practise Question**
What will be the output of following code


---


df = pd.DataFrame([[1, '2020-01-01'], [2, '1998-01-12'], [3, '2012-11-05'],
                   [4, '2000-12-03'], [5, '1960-04-23'], [6, '2008-08-15']],
                    columns=["ID", "birth_dates"])



df["birth_dates"]=pd.to_datetime(df["birth_dates"])


df.iloc[2]['birth_dates'].year - df.iloc[1]['birth_dates'].year
"""

df = pd.DataFrame([[1, '2020-01-01'], [2, '1998-01-12'], [3, '2012-11-05'],
                   [4, '2000-12-03'], [5, '1960-04-23'], [6, '2008-08-15']],
                    columns=["ID", "birth_dates"])
df["birth_dates"]=pd.to_datetime(df["birth_dates"])

df

df.iloc[2]['birth_dates'].year - df.iloc[1]['birth_dates'].year

df.iloc[2]['birth_dates']

# dt is with series we are accessing specific row ,
# we have already converted to timestamp

"""**.to_csv function**


---



To save final data to csv file
"""

data_tidy.to_csv("pfizer_clean.csv",index=False)