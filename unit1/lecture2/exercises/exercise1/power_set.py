# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def power_set(elements):
    """
    bitwise version
    """
    subsets = []
    n = len(elements)
    
    for i in range(1<<n):
        subset = []
        
        for j in range(n):
            print('i=', i, '; j=', j, ';; i >> j =', i >> j, ';; (i >> j) % 2 = ', (i >> j) % 2)
            
            if (i>>j) & 1:
                subset.append(elements[j])
                
        subsets.append(subset)
        print('---------------------------------------------------------')
        
    return subsets

print(power_set([1, 2, 3, 4]))

"""
By Eynsa in the discussion form.
https://courses.edx.org/courses/course-v1:MITx+6.00.2x+3T2017/discussion/forum/c6b266e9539842df955871f288a3b444/threads/59e2b9a4bc04a609f6001ec5


I'm going to step back a bit and explain the powerset all the way through to make understanding it a bit easier.

Let's say you have a list of 3 items = ['spoon', 'fork', 'knife']. To get every combination in that list, you loop over range(2 ** len(items)). Why? So the binary representation of each number literally tells you which item in the list you need to take. 1 means take, 0 means leave it. It looks like so:

0 = 000 = []
1 = 001 = ['knife']
2 = 010 = ['fork']
3 = 011 = ['fork', 'knife']
4 = 100 = ['spoon']
5 = 101 = ['spoon', 'knife']
6 = 110 = ['spoon', 'fork']
7 = 111 = ['spoon', 'fork', 'knife']
How do you accomplish that in code? Both by bit shifting (>>) and using the modulus operator (%).

Let's start with bit shifting. We have a list of 3 items, which is also the length of our binary numbers. range(len(items)) will give you a loop 0, 1, 2.

Imagine we're currently evaluating the number 5 (101 in binary) and see how the loop works:

5 >> 0 = 5  # 101
5 >> 1 = 2  #  10
5 >> 2 = 1  #   1
So in our loop we bit shift our number 0, 1, or 2 bits to the right. We're doing this solely so we can evaluate each bit in our 3 bit number, to determine whether it is 1 so we can take the item that bit represents. And this is done by the modulus operator.

Using the output from the same loop from above, we get the following:

5 % 2 = 1  # the right bit in 101
2 % 2 = 0  # the middle bit in 101
1 % 2 = 1  # the left bit in 101
Combining both for clarity:

5 >> 0 % 2 == 1  # True. Take item 0 from our list
5 >> 1 % 2 == 1  # False
5 >> 2 % 2 == 1  # True. Take item 2 from our list.
"""