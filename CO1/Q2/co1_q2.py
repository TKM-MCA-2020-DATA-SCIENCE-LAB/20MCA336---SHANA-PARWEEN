# -*- coding: utf-8 -*-
"""CO1_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zw40KlUnSUXBeXdGJ4hjaGF9RkASzDgF
"""

import numpy as pd

n=[1,2,3,4,5]
print (n)

pd.array(n)

m=[[1,2,3],[4,5,6],[7,8,9]]
pd.array(m)

pd.arange(0,10)

pd.arange(0,14,3)

pd.zeros(3)

pd.zeros((5,5))

pd.ones(5)

pd.ones((5,5))

pd.eye(3)

pd.linspace(0,20,5)

pd.linspace(1,6,3)

pd.linspace(0,100,10)

pd.random.rand(5)

pd.random.rand(2)

pd.random.rand(2,2)

pd.random.randn(5)

pd.random.randint(1,10)

pd.random.randint(1,100,10)

arr=pd.arange(25)

pd.arange(25)

ranarr=pd.random.randint(0,25,5)

ranarr

arr.reshape(5,5)

ranarr.max()

ranarr.min()

ranarr.argmax()

ranarr.argmin()

arr.shape

arr.dtype

arr[5]

arr[6]

arr[1:6]

arr[1:6]=50

arr

arr.reshape(5,5)

arr[1:5][3:5]=0

arr

arr_copy=arr.copy()

arr

slice_of_arr=arr[0:6]

arr

A=pd.array([[5,10,15],[20,25,30],[35,40,45]])
A

A[1:,:2]





A[:2,1:]

A>5

A<5

A>10

A<0

true=A>5

A[true]

import numpy as pd

pd.arange(0,10)

a=pd.arange(0,10)
a

b=pd.arange(10,20)

c=pd.add(a,b)

c

b

c=pd.subtract(a,b)

c

c=pd.subtract(b,a)
c

c=pd.multiply(a,b)
c

c=pd.divide(a,b)
c

a+b

a-b

a*b

a/b 
a/b

a/a

1/a

a/0

"""SVD:"""

import numpy as np
A = np.arange(0,25)
from scipy.linalg import svd

A

a = np.arange(1,19).reshape(6,3)

U, s, VT = svd(a)

U

s

VT

U, s, VT = svd(a,full_matrices=True)

U

U, s, VT = svd(a,full_matrices=False)

U

from numpy import diag
from numpy import dot

a= (U @ np.diag(s) @ VT)

a





