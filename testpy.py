import numpy as np
import sympy as sy
import scipy as sp
from scipy import optimize
from sympy import *
import matplotlib.pyplot as plt

#Definitions of Functions
def f(x):
    return (x**2)

def fprime(x):
    return (2*x)                                     #Evaluated derivative of f(x)

def g(x):
    return (x**3)

def gprime(x):
    return (3*x)

def h(x,x1):
    return (-x/fprime(x1) + (f(x1) + x1/fprime(x1))) #Definintion of h(x)

def j(x,x1):
    return (g(x) - h(x,x1))                          #j(x) is the component polynomial formed by setting h(x) equal to g(x) 

#x, x1, y, z = symbols ('x x1 y z')
init_printing(use_unicode=True)

#print(h(2,4))
root = optimize.newton(j, 1.0,args=(2,))

print(root)

#Integrate the 'root' value into the distance formula
for x1 in range(1,10,1):
    distance = ((root - x1)**2 + (g(root) - f(x1))**2)**.5 #distance formula
    print('Distance for a function for x' +str(x1),distance)

# Check the solution graphically
xvect = np.linspace(1,2,num=101) # Vector from 1 to 2
jvect = j(xvect,2) # j evaluated at xvect with x2 = 2
plt.plot(xvect,jvect) 
plt.show()
