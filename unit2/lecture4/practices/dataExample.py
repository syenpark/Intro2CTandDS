# -*- coding#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 01:49:38 2018

@author: syenpark
"""
import pylab as plt

def fib(n, memo={}):
    if n < 2:
        return 1
    
    else:
        try:
            return memo[n]
        except KeyError:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
            return memo[n] 
    
def gatherFacts(n):
    inputs = []
    results = []
    
    for i in range(n):
        inputs.append(i)
        results.append(fib(i))
        
    return inputs, results

def displayFibs(n):
    (xvals, yvals) = gatherFacts(n)
    plt.figure('fibs')
    plt.plot(xvals, yvals, label = 'fibonacci')
    plt.show()
    
displayFibs(5)