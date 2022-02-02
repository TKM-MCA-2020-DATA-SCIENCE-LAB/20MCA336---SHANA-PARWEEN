# -*- coding: utf-8 -*-
"""Matplotlib[30/11/21].ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gJ3_PsRA5coX826UiiwW1HJkIIHvEriT
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,11)
y=x ** 3
x

y

plt.plot(x,y,'red')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("x-y graph")
plt.show()

plt.plot(x,y,'g')
plt.xlabel("x-axis")
plt.ylabel("y axis")
plt.title("x-y graph")
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'g--')
plt.subplot(1,2,2)
plt.plot(x,y,'r*-')
plt.show()

t=np.arange(0,20)
d=np.arange(0,20)
plt.subplot(1,3,1)
plt.plot(x,y,'g--')
plt.subplot(1,3,2)
plt.plot(x,y,'r*-')
plt.subplot(1,3,3)
plt.plot(t,d,'b--')
plt.show()

t=np.arange(0,20)
d=np.arange(0,20)
plt.subplot(2,2,1)
plt.plot(x,y,'g--')
plt.subplot(2,2,2)
plt.plot(x,y,'r*-')
plt.subplot(2,2,3)
plt.plot(t,d,'b--')
plt.subplot(2,2,4)
plt.plot(x,y,'g--')
plt.show()

# using object oriented method
fig=plt.figure() #empty canvas
axes=fig.add_axes([2,2,1,1])  # add set of axes to figure
axes.plot(x,y,'r--')
axes.set_xlabel('x axis')
axes.set_ylabel('y axis')
axes.set_title("x-y graph")
plt.show()

fig=plt.figure() #empty canvas
axes1=fig.add_axes([0.3,0.3,0.9,0.9])
axes2=fig.add_axes([0.4,0.6,0.4,0.4])  # add set of axes to figure
#larger one
axes1.plot(x,y,'r--')
axes1.set_xlabel('x axis')
axes1.set_ylabel('y axis')
axes1.set_title("x-y graph")
#smaller one
axes2.plot(x,y,'b--')
axes2.set_xlabel('x axis')
axes2.set_ylabel('y axis')
axes2.set_title("y-x graph")
plt.show()

fig,axes=plt.subplots(nrows=1,ncols=2)

# use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig,axes=plt.subplots(nrows=1,ncols=2)
# iterate through this array
for ax in axes:
  ax.plot(x,y,'r--')  # use axes object to add stuff to plot
  ax.set_xlabel('x axis')
  ax.set_ylabel('y axis')
  ax.set_title("x-y graph")
fig.tight_layout()

fig,axes=plt.subplots(figsize=(11,8))#width and height
axes.plot(x,y,'g*-') 
fig.show()

fig,axes=plt.subplots(figsize=(11,8),dpi=90)#width and height
axes.plot(x,y,'g--') 
fig.show()

fig.savefig("filename1.png") # save figures

fig=plt.figure() #empty canvas
axes=fig.add_axes([2,2,1,1])  # add set of axes to figure
axes.plot(x,x**2,label="x**2")
axes.plot(x,x**3,label="x**3")
axes.set_xlabel('x axis')
axes.set_ylabel('y axis')
axes.set_title("x-y graph")
axes.legend() #legend function
plt.show()

fig=plt.figure() #empty canvas
axes=fig.add_axes([2,2,1,1])  # add set of axes to figure
axes.plot(x,x**2,label="x**2")
axes.plot(x,x**3,label="x**3")
axes.set_xlabel('x axis')
axes.set_ylabel('y axis')
axes.set_title("x-y graph")
axes.legend(loc=7) #legend function with loc 
plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.plot(x,x+3,color='b',lw=3,ls='-',marker='o',markersize=12,linestyle='dashed',markeredgecolor='green',markeredgewidth=4,markerfacecolor='red')
plt.plot(x,x+4,color='r',lw=4,ls='-',marker='o',markersize=10,linestyle='dashed',markeredgecolor='blue',markeredgewidth=5,markerfacecolor='green')

plt.show()