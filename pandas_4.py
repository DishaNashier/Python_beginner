# -*- coding: utf-8 -*-
"""pandas_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1677QeSI5Os54Jb24wTSglueCkg54fL1d
"""

# Agenda
# Multi indexing
#             ********Restructuring data***********
#
# Restructuring data in pandas often involves reshaping and transforming data to meet the specific requirements of your analysis or visualization.
# The pivot and melt functions in pandas are powerful tools for reshaping and transforming data.
#
# ******************** Pivot Function *********************************
# The pivot function is used to reshape a DataFrame by pivoting the values in a column into columns.
# It allows you to reorganize data based on the values in one or more columns.
#
#                   **** Syntax ****
# DataFrame.pivot(index=None, columns=None, values=None)
#
# index: The column whose unique values will become the new DataFrame's index.
# columns: The column whose unique values will become the new DataFrame's columns.
# values: The column whose values will populate the new DataFrame.
#
#  ****************** Melt function ******************************
# The melt function is used to transform a DataFrame from wide format to long format, unpivoting it.
# It is particularly useful when you want to gather different columns into a single column.
#
#                  **** Syntax ****
# pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value')
#
# id_vars: Columns to keep as identifier variables.
# value_vars: Columns to melt (unpivot)
# var_name: Name to use for the variable column (default is 'variable')
# value_name: Name to use for the value column (default is 'value')

import pandas as pd
import numpy as np

!gdown 1s2TkjSpzNc4SyxqRrQleZyDIHlc7bxnd
!gdown 1Ws-_s1fHZ9nHfGLVUQurbHDvStePlEJm

movies = pd.read_csv('movies.csv', index_col=0)
directors = pd.read_csv('directors.csv',index_col=0)

data=movies.merge(directors,how="left", left_on="director_id", right_on='id')
data.drop(['director_id','id_y'],axis=1,inplace=True)

data.head()

# Task: which director will be considered as most productive director

#Counting number of movies by each director
data.groupby("director_name").count()["title"].sort_values(ascending=False)

# Aggregation function in pandas, use of {} to aggregate different columns
data_agg=data.groupby("director_name").aggregate({"title":"count","year":['min','max']})
data_agg
# here indexes are director names

# Hera data is MultiIndexed, "Year" have two columns min and max
# MultiIndexing, or hierarchical indexing, is a powerful feature in pandas,
# It allows you to have multiple levels of indexing for rows and columns in a DataFrame,
# Providing a way to represent higher-dimensional data in a more structured and intuitive manner.
data_agg.columns

# data_agg['max']
# *** to access max we have to use tuple
data_agg[('year','max')]

data_agg.reset_index()

data_agg.head()

# reassign columns names will remove indexing
data_agg.columns=["title_count","year_min","year_max"]

data_agg

data_agg.head()

data_agg=data_agg.reset_index()
data_agg.head()

# Find director with maximum productivity- directors who have more movies per year

# Calculating active years
data_agg['active_yrs']= data_agg["year_max"]-data_agg["year_min"]
data_agg

# calculating movies per year = number of movies/ active years
data_agg["movies_per_year"]= data_agg["title_count"]/data_agg["active_yrs"]
data_agg

data_agg.sort_values("movies_per_year",ascending=False)
#this output is biased because directors who have started producing movies recently are shown as most productive director

data_agg

data_agg[data_agg["title_count"]>=10].sort_values(by="movies_per_year",ascending=False)
#to remove bias nature we filter directors who have produced more than 10 movies

"""Restructuring data

*   Melt
*   Pivot



"""

!gdown 173A59xh2mnpmljCCB9bhC4C5eP2IS6qZ

data = pd.read_csv('Pfizer_1.csv')
data.shape

data

# wide format data =  where number of columns > number of rows
# long format data =  where number of rows > number of columns

data.info()

# melt is similar to unpivot

data.head()

# to reduce wide format
# melt function
# id_vars , parameters that you want to keep as it is
pd.melt(data,id_vars=['Date','Parameter','Drug_Name'])

data_melt=pd.melt(data,id_vars=["Date","Parameter","Drug_Name"],var_name="time",value_name="reading" )
data_melt

# to convert elements of columns to new columns
data_tidy=pd.pivot(data_melt,index=['Date','Drug_Name','time'],
         columns='Parameter',
         values="reading")

data_tidy

data_tidy.loc['15-10-2020']

data_tidy.loc['15-10-2020','diltiazem hydrochloride','4:30:00']

data_tidy.loc['15-10-2020','diltiazem hydrochloride','10:30:00']

data=data_tidy.reset_index()
data

data.set_index(["Date","Drug_Name"])

### pivot table ########
pd.pivot_table(data,index="Drug_Name",columns=["Date"],values="Temperature",aggfunc=np.mean)

pd.pivot_table(data,index="Drug_Name",columns=["Date"],values="Temperature",aggfunc=np.min)

pd.pivot_table(data,index="Drug_Name",columns=["Date"],values=["Temperature","Pressure"],aggfunc=np.min)