# -*- coding: utf-8 -*-
"""numpy problems

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KWNEixeA5FPSNw5PWHJwmMLDSfaUwDFX
"""

# numpy array

# Create a 3×3 numpy array of all True’s
import numpy as np
# by comparison method
a = np.arange(1,10).reshape(3,3)
print(a>=1)
print()

# by full method
b = np.full((3,3), True, dtype=bool)
print(b)

# extract odd and even numbers
# by using list append method
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

even = []
odd = []
for i in a:
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
print("even nums:", even)
print("odd nums:", odd)

# replace odd nums with -1
import numpy as np
a = np.arange(1,10)
print(a)

for i in a:
  if (i%2)==0:
    a[0] = -1
    a[i] = -1
print(a)

# replace odd nums with -1 without affecting original array
import numpy as np
a = np.arange(0,10)
#print(a)
print(id(a))
b = a.copy()
#print(b)
print(id(b))

for i in b:
  if i%2==0:
    b[i] = -1
print("modified array:", b)
print(id(b))     # id of b is same after replacement due to mutabilty of array
print("original array:",a)

# how to stack two arrays vertically
import numpy as np
a = np.arange(0,10).reshape(2,5)
b = np.arange(10,20).reshape(2,5)

# by using concatenate method
c = np.concatenate((a,b), axis=0)       # axis = 0 for vertical
print(c)
print()

# by using vstack method
d = np.vstack([a,b])
print(d)
print()

# by using np.r_[arr1,arr2] method         # r stands for rows
e = np.r_[a,b]
print(e)

# stack two arrays horizontally.
import numpy as np
a = np.arange(8,18).reshape(2,5)
b = np.arange(10,20).reshape(2,5)

# by using concatenate
c = np.concatenate((a,b), axis=1)         # axis=1, horizontal
print(c)
print()

# by using hstack
d = np.hstack([a,b])
print(d)
print()

# by using np.c_[arr1,arr2] method       # c stands for column
e = np.c_[a,b]
print(e)

# array creation using reshape
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

print(a)
print()
print(b)

# np.r_[arr1,arr2]      # row      # for concatenate array from 1st axis
# np.c_[arr1,arr2]      # column   # for concatenate array from 2nd axis

# custom sequence 
# expected - [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
a = np.array([1,2,3])
c = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(c)

# extract common items from array
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = []

for i in range(len(a)):
  if i in b and i in a:
    c.append(i)
print(c)
print(type(c))

# using built in method
d = np.intersect1d(a,b)
print(d)
print(type(d))

# extract common items from array
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

f = []
for i in range(len(a)): 
  if i in a and i in b:
    #print(i)
    f = np.append(f,i)       # appending in array
print(f)

# remove from one array those items that exist in another
a = np.array([1,2,3,4,5,6])
b = np.array([5,6,7,8,9])

c = []
for i in a:
  if i in b:
    c.append(i)
print("items available in a and b:", c)

# elements of two arrays match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.where(a==b)
print(c)

# How to extract all numbers between a given range from a numpy array
# given range = 5,10

import numpy as np
a = np.arange(1,11)
print(a)

b = range(5,11)

for i in a:
  if i in b:
    print(i, end=" ")
print()

# if i want ndarray of given o/p
# appending with array 
op = []
for i in a:
  if i in b:
    op = np.append(op, i)
print(op)

# get the maximum of two array 
import numpy as np
a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,2,8,29])

# using maximum
c = np.maximum(a,b)              # it check element index to index
print(c)

# using function
def maxi(i,j):
  if i >= j:
    return i
  else:
    return j

maximum = np.vectorize(maxi)               

a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,2,8,29])

maximum(a,b)

# access columns and rows
import numpy as np
a = np.arange(9).reshape(3,3)
print(a)

#print(a[1:])

# swap 1 and 2 column
import numpy as np
a = np.arange(9).reshape(3,3)
print(a)

print()

b = a[:, [1, 0, 2]]         # swap 1st and 2nd column
print(b)
print()

# swap 1 and 2 row
b = a[[2,1,0],:]             # swap 1st and 3rd row
print(b)

# how to reverse the array
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
print(a[::-1])                    # ndarrays are not comma separated

# reversed method
print(list(reversed(a)))         # list values are comma separated

# flip method
b = np.flip(a)
print(b)                       # reverse the array

# reverse the array using for loop
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
print(type(a))

for i in range(len(a)-1, -1, -1):        # reverse range  
  print(a[i], end= " ")                  # i should be less than len(a)
  
print()
print(type(a))

# reverse 
a = [10,20,30,40]
for i in range(len(a)-1,-1,-1):
  print(a[i], end=" ")
print()

b = "hello python"
for i in range(len(b)-1,-1,-1):
  print("".join(b[i]), end=" ")
print()
c = {"a":200, "b":300, "c":400, "d":500}
print(c)
for i in range(len(c)-1, -1,-1):
  print(i)
print(sorted(c, key= lambda x:x[0]))

# reverse columns in array
import numpy as np
a = np.arange(9).reshape(3,3)
print(a)
print()
print(a[:,::-1])

# reverse the rows in array
import numpy as np
a = a = np.arange(9).reshape(3,3)
print(a)
print()
print(a[::-1])

# create a 2D array containing random floats between 5 and 10
import numpy as np
a = np.random.uniform(5,10, size=(5,3))
print(a)

# print only 3 decimal places in python numpy array
import numpy as np
a = np.random.uniform(5,10, size=(5,3))
print(a)

print()

# decimal places - 1
np.set_printoptions(precision=1)
print(a)

# find out zero or Nan available in array
import numpy as np
arr = np.array([1,2,4,8,3,6,0,2,5,7,8])
print(arr)

if all(arr) == False:
  print("zero not available")
else:
  print("zero is in array")

# test whether any of the elements of a given array is non-zero
import numpy as np
a = np.array([0,0,0,0,5,0,0,0])

# method 1
if any(a) == True:
  print("non zero available")
else:
  print("not available")

# method 2
for i in a:
  if i > 0:
    c = "available"
    break
  else:
    c = "not available"
    
print(c)

# isnan - to find nan value
# isinf - to find infinite value

# identity matrix
import numpy as np
a = np.identity(5)
print(a)

#  3x3 identity matrix
b = np.identity(3)
print(b)

# NumPy program to create an array of 10 zeros,10 ones, 10 fives
import numpy as np
a = np.zeros(10)
print(a)

b = np.ones(10)
print(b)

c = np.full(10,5)
print(c)

# generate random nums
import numpy as np
a = np.random.randint(1,15)
print(a)

# set the limit to op, print only 1st 3 and last 3 values
import numpy as np
a = np.arange(12)
print(a)

np.set_printoptions(threshold=6)
print(a)

# 15 random numbers from a standard normal distribution
import numpy as np
a = np.random.rand(15)
print(a)

#  create a vector with values ​​ranging from 15 to 55 and print all values ​​except the first and last
import numpy as np
a = np.arange(15,55)
print(a[1:])

# create a vector of length 10 with values evenly distributed between 5 and 50.
import numpy as np
a = np.linspace(5,50,5)
print(a)
print(len(a))

a = [10,20,30,40]                     # list
print(a*3)

import numpy as np
b = np.array([10,20,30,40])           # array
print(b*3)

# create 3X4 array and iterate through loop
import numpy as np
a = np.arange(1,13).reshape(3,4)
print(a)
for i in np.nditer(a):
  print(i, end=" ")

# vector of length 10 with values evenly distributed between 5 and 50
import numpy as np
a = np.linspace(10,50,5)            # here 5,50 is range and 5 is no of elements
print(a)

# create a vector of length 5 filled with arbitrary integers from 0 to 10.
import numpy as np
a = np.random.randint(0,10,5)
print(a)

# multiply the values of two integers
import numpy as np
a = np.arange(5)
b = np.arange(5,10)
print(a)
print(b)
c = a*b                 # element wise lement
print(c)

# dot method gives the multiplication of matrix
d = np.dot(a,b)
print(d)               # mulitplication

#  create a 3x4 matrix filled with values from 10 to 21
import numpy as np
a = np.arange(10,22).reshape(3,4)
print(a)

# find the number of rows and columns of a given matrix
import numpy as np
a = np.arange(20).reshape(4,5)
print(a)

# find rows and column
b = np.shape(a)
print("shape of given matrix:", b)

print("total rows:", b[0])
print("total columns:", b[1])

# NumPy program to create a 9X9 matrix, in which the elements on the borders will be equal to 1, and inside 0
import numpy as np
a = np.zeros(81).reshape(9,9)
print(a)

print()

a[0]= np.ones(9)
a[-1] = np.ones(9)
a[:,0] = np.ones(9)
a[:,-1] = np.ones(9)
print(a)

import numpy as np
a = np.ones((9, 9))
a[1:-1, 1:-1] = 0
print(a)

# create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4,5
import numpy as np
a = np.diag([1,2,3,4,5])                  # return ndarray
print(a)
print()

# using for loop                         # return matrix
n = 6       # no of rows and column
for i in range(0,n):
  for j in range(0,n):
    if i==j:
      print(i, sep=" ",end=" ")
    else:
      print("0", sep=" ",  end=" ")
  print()

a = np.zeros((5,5))
a[0,0] = 1
a[1,1] = 2
a[2,2] = 3
a[3,3] = 4
a[4,4] = 5
print(a)

# identity matrix using for loop
n = 5       # no of rows and column
for i in range(0,n):
  for j in range(0,n):
    if i==j:
      print(j, sep=" ",end=" ")
    else:
      print("0", sep=" ",  end=" ")
  print()

# alternate 1,0 row wise
n = 5       # no of rows and column

for i in range(0,n):
  for j in range(0,n):
    if i%2==0:
      print(1, sep=" ",end=" ")
    else:
      print("0", sep=" ",  end=" ")
  print()

# alternate 1,0 column wise
n = 5       # no of rows and column

for i in range(0,n):
  for j in range(0,n):
    if j%2==0:
      print(1, sep=" ",end=" ")
    else:
      print("0", sep=" ",  end=" ")
  print()

# alternate 1,0 column/row wise
# using for loop
n = 5       # no of rows and column

for i in range(0,n):
  for j in range(0,n):
    if j%2==i%2:
      print(1, sep=" ",end=" ")
    else:
      print("0", sep=" ",  end=" ")
  print()

print()
# by using slicing
import numpy as np
xa = np.zeros((4, 4))
a[::2, 1::2] = 1
a[1::2, ::2] = 1
print(a)

# create a 3x3x3 array filled with arbitrary values.
import numpy as np
a = np.empty(27).reshape(3,3,3)
print(a)

# find sum of given array..
import numpy as np
a = np.arange(1,17).reshape(4,4)
print(a)

# row wise sum
row_sum = np.sum(a, axis=1)
print("row-wise:",row_sum)

col_sum = np.sum(a, axis=0)
print("column-wise:",col_sum)

total_sum  = np.sum(a)
print("total:", total_sum)

# to compute the inner product of two given vectors
import numpy as np
a = np.arange(1,5).reshape(2,2)
b = np.arange(8,12).reshape(2,2)

print(a)
print(b)

# multiplication with * will give the element wise multiplication
c = a*b
print(c)                 # element wise

# we need product                 # dot method
d = np.dot(a,b)
print(d)

# to add a vector to each row of a given matrix
import numpy as np
a = np.arange(10,19).reshape(3,3)
b = np.array([1,2,3])
print(a)
print(b)

print(a+b)    # row wise addition possible directly,

c = b.T        # need to transpose, beacuse of change in shapes
print(c)

d = a + c            # adding element in each column
print(d)

# Write a NumPy program to convert a given list into an array,
# then again convert it into a list. Check initial list and final list are equal or not
import numpy as np
li = [10,20,30,40,50]
arr = np.array(li)
print(li)
print(arr)

new_list = arr.tolist()
print(new_list)
print(type(new_list))

li == new_list            # content equality
id(li) == id(new_list)    # different memory address

# find missing data from array
import numpy as np
data = np.array([[3, 2, np.nan, 1],[10, 12, 10, 9],[5, np.nan, 1, np.nan]])
print(data)

print(np.isnan(data))          # return True when nan present

# find two vectors equal or not, element wise
import numpy as np
a = np.array([10,15,14,12,16])
b = np.array([12,15,10,14,16])

print(a==b)

# using built in
b = np.equal(a,b)
print(b)

# one-dimensional array of single, two and three digit numbers
import numpy as np
a = np.arange(1,10)
b = np.arange(10,20)
c = np.arange(100,110)

print(a)
print(b)
print(c)

# create a one dimensional array of forty pseudo-randomly generated values. 
#Select random numbers from a uniform distribution between 0 and 1.
import numpy as np  
np.random.seed(10)
print(np.random.rand(40))

# create a two-dimensional array with shape (8,5) of random numbers. 
# Select random numbers from a normal distribution (200,7)
import numpy as np
np.random.seed(40)
a = np.random.rand(40)
print(a)

# need to check random.seed()

# create 4X4 and swap 1st and last row
import numpy as np
a = np.arange(1, 17).reshape(4,4)
print(a)
print(a[[3,1,2,0],:])

# swap column
print(a[:,[2,0,3,1]])

# print 7, 3 alternatively, empty spaces fill with zero
import numpy as np
n = 6
m = 6
for i in range(n):
  for j in range(m):
    if i%2!=0 and j%2!=0:
      print(3, end=" ")
    elif i%2==0 and j%2==0:
      print(7, end=" ")
    else:
      print(0, end=" ")
  print()

# sort a given 1D array in ascending order.
import numpy as np
a = np.array([10,15,3,7,1,19,5,4,6])
print(a)

# using built in    # return ndarray
b = np.sort(a)    
print(b)
print(type(b))

# using sorted  method -- Return list in op
c = sorted(a) 
print(c)
print(type(c))

# using for loop

for i in range(len(a)):
  for j in range(i+1):
    if a[i] < a[j]:
      a[i],a[j] = a[j],a[i]
print(a)
print(type(a))                 # type ndarray

# reversed array
import numpy as np
a = np.array([10,15,3,7,1,19,5,4,6])
print(a)

# reversed() method
b = list(reversed(a))                # op in list
print(b)

#using slicing
print(a[::-1])

# using for lo

# find maxium and minimum
import numpy as np
a = np.array([10,15,3,7,1,19,5,4,6])
print(a)

# using for loop
maxi = a[0]
print(maxi)
for i in range(len(a)):
  if maxi < a[i]:
    maxi = a[i]
print(maxi)

mini = a[0]
for i in range(len(a)):
  if mini > a[i]:
    mini = a[i]
print(mini)

# reversed list using while loop
a = [10,15,3,7,1,19,5,4,6]
print(a)
b = []
l = len(a)         # length of list
while l>0:
  b.append(a[l-1])         
  l = l - 1
print(b)

print("array reversing using while loop")
import numpy as np
arr = np.array([1,2,3,4,5,6])
print("original array:", arr)
l = len(arr)
#print(l)
rev = []
while l>0:
  rev = np.append(rev, (l-1))
  l = l - 1
print("reversed array:", rev)

# list reversed
a = [10,15,3,7,1,19,5,4,6]
c = []
for i in range(len(a)-1,-1,-1):
  c.append(a[i])
print(c)

# replace items if value greater than 5, then replace with 8
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print()

b = np.where(a>=5, 8, a)
print(b)

print()
for x in range(len(a)):
  pass

for i in a:
  for j in i:
    #print(j)
    if j>=5:
      a[x] = 8
print()

# how to iterate numpy array elements
import numpy as np
# 1D array
a = np.array([10,20,30,40,50,60])
print(a)
for i in a:
  print(i, end=" ")
print()

# 2D array
b = np.array([[1,2],[3,4,]])
print(b)
for i in b:
  for j in i:
    print(j, end=" ")
print()

# 3d Array
c = np.array([[[10,20,30],[40,50,60],[70,80,90]]])
print(c)
for i in c:
  for j in i:
    for k in j:
      print(k,end=" ")
print()

# create 4X4 array and swap 1st and last and 2nd and 3rd row
import numpy as np 
a = np.arange(1, 17).reshape(4,4)
print(a)

print()
b = a[[3,2,1,0],:]
print(b)
print()
print(a[::-1])           # for rows reverse
print()
print(a[:,::-1])         # for columns reverse

# create 3d array with 3,5,4
import numpy as np
a = np.arange(60).reshape(3,5,4)
print(a)

# replace nums from given array with zeros
import numpy as np
a = np.array([[5.54, 3.38, 7.99],[3.54, 8.32, 6.99],[1.54, 2.39, 9.29]])

print(a)

b = np.zeros_like(a)
print(b)

# remove elemts which are less than 7
import numpy as np
a = np.arange(1,17).reshape(4,4)
print(a)

# using for loop
b = []
for i in a:
  for j in i:
    if j <= 7:
      b = np.append(b, j)
print(b)


# using condition
c = a[a > 7]
print(c)

# print the NumPy version in your system
import sys
sys.__version__

# conevert list into 1D
a = [12.23, 13.32, 100, 36.32]
import numpy as np
b = np.array(a)
print(b)

# create null of size 10 and update 11 at 6th position
import numpy as np
a = np.zeros(10)
print(a)

a[6] = 11
print(a)

# reverse array
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
for i in range(len(a)-1, -1, -1):
  print(a[i], end=" ")

# revrese array
a = [1,2,3,4,5,6,7,8,9,10]
import numpy as np

print(a[::-1])

print(np.flip(a))

# change datatype to float
a = [1,2,3]
import numpy as np
a = np.array(a, dtype=float)
print(a)

#  create array zero inside and 1 border
import numpy as np
a = np.ones(25).reshape(5,5)
print(a)
print()
a[1:-1, 1:-1] = 0
print(a)

# create a 8x8 matrix and fill it with a checkerboard pattern
n = 8
for i in range(n):
  for j in range(n):
    if j%2 == 0:
      print(1, end=" ")
    else:
      print(0, end=" ")
  print()

# append values at end of array
import numpy as np
a = np.array([10,20,30])
print(a)

b = np.append(a, [40,50,60])
print(b)

# convert the values of Centigrade degrees into Fahrenheit degrees and vice versa.
# Values are stored into a NumPy array.
# formula = c = (f-32)*(5/9)

a = [0, 12, 45.21, 34, 99.91]
import numpy as np
a = np.array(a)
print(a)
b = []
for i in a:
  c = (i-32)*(5/9)
  b = np.append(b, c)
print(b)

import numpy as np
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])

print(x.real)
print(y.real)

print(x.imag)
print(y.imag)

# find memory consumed
a = np.array([1,2,3], dtype=np.float64)
import numpy as np
b = a.size
c = a.itemsize
d = a.nbytes

print(b)
print(c)
print(d)

# test whether each element of a 1-D array is also present in a second array
import numpy as np
a = np.array([10,20,30])
b = np.array([10,40])

c = np.in1d(a,b)
print(c)
print(a[c])    # very very important

# common in both
import numpy as np
a = np.array([10,20,30,40])
b = np.array([10,40,50,60])
c = np.intersect1d(a,b)
print(c)

# get the unique elements of an array
import numpy as np
a = np.array([10,10,10,20,20,30])
b = np.unique(a)
print(b)

# setdifference in both, that not contain in 2nd array
import numpy as np
a = np.array([10,20,30,40])
b = np.array([10,40,50,60])
k = []
for i in a:
  if i not in b:
    k = np.append(k, i)
print(k)

# using builtin
e = np.setdiff1d(a,b)
print(e)

# find unique from both array
import numpy as np
a = np.array([0,10,20,40,60,80])
b = np.array([10, 30, 40, 50, 70])
print(a)
print(b)
d = []

for i in a:
  if i not in b:
    d = np.append(d, i)
for j in b:
  if j not in a:
    d = np.append(d, j)
print(d)

# built in method
e = np.setxor1d(a,b)
print(e)

# repeat elmets
import numpy as np
a = np.array([1,2,3])
b = np.tile(a, 2)
print(b)

# repeat elements
import numpy as np
x = np.repeat(3, 4)
print(x)
x = np.array([[1,2],[3,4]])
print(np.repeat(x, 2))

# find maximum and minimum
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
max = a[0]
for i in range(len(a)):
  if max<a[i]:
    max = a[i]
print("maximum value:", max)

min = a[0]
for i in range(len(a)):
  if min>a[i]:
    min = a[i]
print("minimum value:", min)

# check empty array
import numpy as np
a = np.array([])
if a == []:
  print("empty")
else:
  print("not empty")

# fancy indexing
a = np.array([1,8,6,7,6,9,3])
#print(a[[1,6,3]])

b = np.arange(9).reshape(3,3)
print(b)
print()

print(b[[2,1],[0,2]])     # access 6 and 5

# create a new array of 3*5, filled with 2
import numpy as np
a = np.ones(15).reshape(3,5) * 2
print(a)

print()

# another method
a = np.full((3,5), 2)
print(a)

# sort array with first name and last name 
import numpy as np
a =    ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
b = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')
x = np.lexsort((a,b))              # it sort array and return indices
print(x)

# Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.
import numpy as np
a = np.array([[ 0,10,20],[20,30,40]])
print(a)

# to get the values greater than 10
for i in a:
  for j in i:
    if j>10:
     c = j
     print(c, end=" ")
print()

#another method
b = np.where(a>10)
print(b)               # indices are- [row elements],[column elements]

# another method
d = a[a>10]
print(d)       # get the valeus

# another method
e = np.nonzero(a>10)
print(e)

# find memory size of array
import numpy as np
a = np.array([10,20,30,40,50])
print("memory size:", a.nbytes)

b = np.arange(40).reshape(2,4,5)
print("memory size:", b.nbytes)

# contigeous array
a = np.arange(20).reshape(2,2,5)
print(a)

b = a.flatten()
print(b)

# another built in 
c = np.ravel(a)
print(c)

# sum
import numpy as np
a = np.array([[1,2],[4,5]])
print(a)

print(np.sum(a, axis=1))
print(np.sum(a, axis=0))
print(np.sum(a))

# values greater than 10... op must be indices.
import numpy as np
a = np.array([[ 0,10,20],[20,30,40]])
print(a)
print()

b = a>10
print(b)
print()

print(a[b])      # get values

# print the shape, type and data type of the array.
import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(type(x))	
print(x.shape)
print(x.dtype)

# create arrray of 4 nums amnd then print 10

import numpy as np
x = np.arange(4, dtype=np.int64)
y = np.full_like(x, 10)
print(y)

#  create a 2-D array whose diagonal equals [4, 5, 6, 7] and 0's elsewhere

import numpy as np
a = np.diagflat([4,5,6,7])
print(a)

#  Create a 1-D array of 30 evenly spaced elements between 2.5. and 6.5,last exclusive
import numpy as np
a = np.linspace(2.5,6.5,30)
print(a)

# as per given pattern, chnage 8,11,12 with 0
import numpy as np
a = np.arange(2, 14).reshape(4, 3)
print(a)

a[[2,3,3],[0,0,1]] = 0
print(a)

# access 4th elements 
a = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(a)
print(a[1][0])

# another method
print(a.flat[3])

# 1d array to 2d column wise
import numpy as np
a = np.array((10,20,30))
b = np.array((40,50,60))
c = np.column_stack((a, b))
print(c)

# 1d array to 2d row wise
import numpy as np
a = np.array((10,20,30))
b = np.array((40,50,60))
c = np.row_stack((a, b))
print(c)

# split 14 elements in 3 arrays
import numpy as np
a = np.array([10,20,30,40,50,60,70,80,90])
b = np.array_split(a, [2,5])
print(b)

c = np.split(a, 3)
print(c)

# split horizontally
import numpy as np
a = np.arange(16).reshape(4,4)
print(a)

b = np.hsplit(a, 2)
print(b)

# shorcut method to find most ocuuring num
lst = [1, 2, 3, 5, 4, 2, 3, 1, 5, 4, 5]
print(max(set(lst), key = lst.count))

# find non zero nums, indices and count
import numpy as np
a = np.array([[0, 10, 20], [20, 30, 40]])
print(a)

b = np.nonzero(a)          # reurn indices
print(b)

c = np.count_nonzero(a)    # no of count
print(c)

# pattern
n=5
for i in range(0,n):
  for j in range(0, n):
    print(j+1, end=" ")
  print()

# create a vector of size 10 with values ranging from 0 to 1, both excluded
import numpy as np
a = np.linspace(0,1,10)[1:-1]
print(a)

# a NumPy program (using NumPy) to sum of all the multiples of 3 or 5 below 100.
import numpy as np
x = np.arange(1,100)
print(x)

n= x[(x % 3 == 0) | (x % 5 == 0)]
print(n)
print(sum(n))

# create cube of given array
import numpy as np
a = np.array([1,5,6,8,20]) 
print(a)
b= []
for i in a:
  b = np.append(b, i**3)
print(b)

# iterate numpy array
import numpy as np
x = np.arange(12).reshape(3, 4)
for x in np.nditer(x):
    print(x,end=' ')
print()

# fortan order and c order
a = np.arange(16).reshape(4,4)
print(a)

for i in np.nditer(a, order="F"):
  print(i, end=" ")
print()

# Write a numpy python program that converts a binary numpy matrix (containing only 0s and 1s) into a numpy boolean matrix 
# (i.e. the '1 will be replaced by True and the '0' by False)
import numpy as np
a = np.array([0,1,1,0,1,0,5,1,0,2,0,1]).reshape(4,3)
print(a)
for num in a:
  for i in num:
    if i == 1:
      print(True)
    elif i == 0:
      print(False)
    else:
      print(i)
print(a)

# another method
b = a.astype(bool)
print(b)

# how to reshape the array
import numpy as np
a = np.arange(15)
print(a)

print(a.reshape(5,-1))           # -1 automatically decide the no of columns

print(a.reshape(3,-1))

import numpy as np
a = np.array([1,3,5,58,89])
b = a.size
c = a.itemsize

d = a.nbytes
print(d)
print(a,b,c)

import numpy as np
a = np.arange(20).reshape(4,5)
print(a)
print(a[:,0])

# Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
import numpy as np
a = np.arange(100,200,10).reshape(5,2)
print(a)

# print last  column
import numpy
a = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print(a)
print(a[:,2])
print(a[:,2:])

# print odd rows and even columns
import numpy
a = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print(a)

print(a[::2, 1::2])

# Create a result array by adding the following two NumPy arrays. 
#Next, modify the result array by calculating the square of each element
a = numpy.array([[5, 6, 9], [21 ,18, 27]])
b = numpy.array([[15 ,33, 24], [4 ,7, 1]])
print(a)
print()
print(b)
print()
c = a + b
print(c)
print()
# square
d = c**2
print(d)

# Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 
# and then Split the array into four equal-sized sub-arrays.
import numpy as np
a = np.arange(10,34).reshape(8,3)
print(a)

# spliting
b = np.split(a, 4)
print(b)

# sort array by axis
import numpy as np
a = np.array([[34,43,73],[82,22,12],[53,94,66]])    # 
print(a)

b = np.sort(a, axis=None)     # flatten array
print(b)

c = np.sort(a, axis=0)      # row wise
print(c)

d = np.sort(a, axis=1)       # column wise
print(d)

# # sort array by 2nd row and 2nd acolumn
import numpy as np
a = np.array([[34,43,73],[82,22,12],[53,94,66]])    # 
print(a)

b = np.sort(a, axis=None)     # flatten array
print(b)

c = a[:, a[1,:].argsort()]     # sort by 2nd row
print(c)

d = a[a[:, 1].argsort()]    # by second column 
print(d)

# print max and min from 0 and 1 axis
import numpy as np
a = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(a)

b = np.max(a)
print(b)

c = np.min(a)
print(c)

d = np.max(a, axis=0)
print(d)

e = np.max(a, axis= 1)
print(e)

f = np.min(a, axis=0)
print(f)

g = np.min(a, axis= 1)
print(g)

# delete 2nd column and insert with [10,10,10]
import numpy as np
a = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(a)
b = np.array([[10,10,10]])

a = np.delete(a,1,axis=1)    
print(a)

a = np.insert(a, 1, b, axis=1)
print(a)

# create 2 arrays and plot them using matplotlib
import numpy as np
import matplotlib.pyplot as plt

x= np.array([1,2,3,4,5])    # array creation
y= np.array([4,5,6,7,8])

plt.figure(dpi=50)      # creating figure

plt.plot(x,y)           # plotting

# basic parametere
plt.title("First plot")
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Displaying the plot
plt.show()

# Importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# Creating a new figure 
plt.figure(dpi=100)

# Creating array from list 
x= np.random.randint(1,100,20)
y= np.random.randint(1,100,20)

# Numpy array as scatter plot
plt.scatter(x,y)

# Adding details to the plot
plt.title('Scatter Plot of a NumPy Array')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Displaying the plot
plt.grid()
plt.show()

# 3x3 identity matrix
import numpy as np
a = np.identity(3)
print(a)

# find mean of random 30 
import numpy as np
a = np.random.random(30)
print(a)

mean = np.mean(a)
print(mean)

m = a.mean()
print(m)

# how to print 0 at border
import numpy as np
a = np.ones((5,5))
print(a)

b = np.pad(a, pad_width=1)
print(b)

# by using fancy indexing
a[:, [0, -1]] = 0
a[[0, -1], :] = 0
print(a)

print(np.diag([1,2,3,4]))

# checkboard pattern 
a = np.zeros((5,5))
a[1::2, ::2] = 1
a[::2, 1::2] = 1
print(a)

# Alternative solution: Using reshaping
a = np.ones(64,dtype=int)
a[::2]=0
a = a.reshape((8,8))
print(a)

# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
import numpy as np
a = np.arange(336).reshape(6,7,8)
#print(a)
b = np.unravel_index(99, (6,7,8))
print(b)

# to print checkboard pattern
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)

# normalise 5X5 random matrix
import numpy as np
a = np.random.random(25)
print(a)
print()
mean = np.mean(a)      # mean
print(mean)
print()
std = np.std(a)        # standard deviation
print(std)
print()

a = (a-mean)/std
print(a)

# Multiply a 5x3 matrix by a 3x2 matrix
a = np.arange(1,16).reshape(5,3)
b = np.arange(1,7).reshape(3,2)
print(a)
print(b)