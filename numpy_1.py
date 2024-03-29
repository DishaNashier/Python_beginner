# -*- coding: utf-8 -*-
"""Numpy-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_160l-k9pTtVj1G8XR1y7Q857-03TypB
"""

#AGENDA
# **********************************************Data analysis and Visulaisation********************************
# Numpy
# Arrays/Create/Use
# Arrays vs List
# NPS USe Case
# Data Analysis and Visulaisation: Libraries(Numpy, Pandas, MatPlotlib, Seaborn)

# **** NumPy ****
# Numerical computation using Python
# NumPy is a library for the Python programming language, adding support for large,
# Multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
# pip(python package manager)
# pip install numpy

pip install numpy

import numpy as np

#List(Heterogeneous) vs Array(Homogeneous)
# Case 1 - Well organised variables - NumPy Array - Fast Computation- sequential memory allocation
# Case 2 - Not well organise variables - Python List- Slow Computation- distributed memory allocation/ Random location
# Numpy library was written in C with a wrapper to interact with Python
# Numpy arrays are super fast
# for arrays more function available as compared to list
# For Example:- .sum(), .mean(), .median()

a=[1,2,3,4,5]
print(a)

# Write a code where list variable(ans) stores list of squares of 'a' list items
ans=[]
for i in a:
  ans.append(i**2)
print(ans)

res=[ele**2 for ele in a]
print(res)

# If you find type of any variable it can display 3 possiblities
# 1. inbuilt type- for example- list,string etc
# 2. user_defined(Class created in current script) than it will display type of variable as- __main__.class_name, string here class type is list,string
# 3. Module/Package type- class belonging to some other module/package For eg- numpy.ndarray here class is ndarray

#Lets create numpy array
#np means numpy
# array is a numpy function
arr=np.array(a)
arr

type(arr)

#numpy.ndarray
#.ndarray is a class in numpy package script
# if .ndarray class would have present in current script the suffix would have been "main" instead of "numpy"

a=[1,2,3,4,5]
type(a)
# it will display type "list" because list is an inbuilt function

# sqaure of all elements in numpy array
a=[1,2,3,4,5]
arr=np.array(a)
arr**2

# colab function
# 💡 %timeit 💡
# Time execution of a Python statement or expression using the timeit
# module.  This function can be used both as a line and cell magic

# Commented out IPython magic to ensure Python compatibility.
# ✅Numpy arrays are faster than python Lists
l=range(1000000)
# %timeit [i**2 for i in l]

# Commented out IPython magic to ensure Python compatibility.
l=np.array(l)
# %timeit l**2

## Dimensions and Shapes
# 1D array
# 2D array
# 3D array
# nD array

arr=np.array([1,2,3,4,5,6])
arr

type(arr)

#to check number of dimensions
arr.ndim

# returns tuple -->(a,b,c) elemnts are count of items in array every dim.
arr.shape
#output- (6,) -it shows its a one dimension array having 6 elements, "," is present at last because output is always in tuple

arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2

arr2.ndim

arr2.shape
# output- (3, 3) -means 1st dimension have 3 items(3 rows) and 2nd dimension also have 3 items (3colums)

# To find total number of items in arr2
arr2.size

a=np.array([1,2,3,4,5,6,7,8])
print(a.ndim,a.shape)

#range()
# Similar to range function we have np.arange(1,5)
np.arange(1,7,2)

np.arange(1,5,0.5)

# array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])
# output contains 1. not 1 because of homogenous concept
# all numbers will be float numbers because step size is 0.5

np.arange(10)

arr=np.arange(5)
arr[2:4]=0
print(arr)

# if we use single element in any array as float rest integer, every element will be converted to float
arr= np.array([1,2,3,4,5])
arr

arr=np.array([1,2,3,4,5.0])
arr

arr=np.array([1,2,3,4,'Harry'])
arr
#every element is converted to string

# @title Indexing and slicing

m1= np.arange(2,12)
m1

m1[0]

m1[len(m1)-1]

m1[-1]

# if we want to extract multiple elements
# we need to use double [[]]
# m1[int]
# m1[list]
m1[[6,2,9,4,1,6]] #elements are index positions

a=np.array([0,1,2,3,4,5])
a[4:]=10
print(a)

#@title Fancy Indexing/Boolean Indexing

m1=np.arange(5,15)

m1>10

mask=m1<8
mask

m1[mask]

m1[m1<8]

#checking if element is divisible by 2
m1[m1%2==0]

#aggregation
m1[m1%2==0].sum()

#Use case: NPS [Net Promoter Score]
# Score- 0-6 Detractors
# Score- 7-8 Passives
# Score- 9-10 Promoters
# Net Promoter score=%Promoters-%Detractors

# https://drive.google.com/file/d/1c0ClC8SrPwJq5rrkyMKyPn80nyHcFikK/view

#google down -to download
!gdown https://drive.google.com/file/d/1c0ClC8SrPwJq5rrkyMKyPn80nyHcFikK/view

scores=np.loadtxt('/survey.txt', dtype='int')
scores

type(scores)

#total number of people who participated in survey
total=scores.size
total

scores.shape

scores[:5]

promoters=scores[scores>8]
n_promoters=promoters.size
n_promoters

detractors=scores[scores<7]
n_detractors=detractors.size
n_detractors

NPS=100*(n_promoters-n_detractors)/total
NPS

np.round(NPS,2)

