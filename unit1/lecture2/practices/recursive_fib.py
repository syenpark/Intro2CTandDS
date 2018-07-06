# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def fib(n):
    """
    a pure recursive fib
    """
    if n < 2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)

# https://www.quora.com/What-is-memoization    
def fast_fib(n, memo={}):
    """
    a recursive fib with memoization a.k.a dynamic programming
    """
    if n < 2:
        return 1
    
    try:
        return memo[n]
    
    except KeyError:
        memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        return memo[n]
        
print(fast_fib(4))
