import numpy as np
import sympy as sy
import scipy as sp
from scipy import optimize
from sympy import *

x, y, z = symbols ('x y z')
init_printing(use_unicode=True)




def f(x):
    return (x**2)


def g(x):
    return (x**3)


def h(x):
    return ((-1/diff(f(x), x)) + (f(x) + x/diff(f(x), x)))

def j(x):
    return (g(x) - h(x))

root = optimize.newton(j(x), 1.0)

print(root)