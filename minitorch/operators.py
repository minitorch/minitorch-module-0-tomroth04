"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float) -> float:
    return x * y

def id(x):
    return x

def add(x: float, y: float) -> float:
    return x + y

def neg(n: float) -> float:
    return -n

def lt(x: float, y: float): # TODO: could add return
    return x < y

def eq(x: float, y: float): # TODO: could add return
    return x == y

def max(x: float, y: float) -> float:
    if x > y:
        return x
    return y

def is_close(x: float, y: float): # TODO: could add return
    return abs(x - y) < (1 / (math.e **2))

def sigmoid(x: float):
    if x >= 0:
        return 1 / (1 + (math.e ** (-x)))
    return (math.e **x) / (1.0 + (math.e ** x))

def relu(x: float) -> float:
    return max(0, x)

def log(x: float) -> float:
    return math.log(x)

def exp(x: float) -> float:
    return math.e ** x

def inv(x: float) -> float:
    return 1 / x

def log_back(x: float, alpha: float) -> float:
    return (1 / x) * alpha

def inv_back(x: float, alpha: float) -> float:
    return -alpha * (1 / (x**2))

def relu_back(x: float, alpha: float) -> float:
    if x > 0:
        return alpha
    return 0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(l, f):
    return [f(l(i)) for i in l]

def zipWith()