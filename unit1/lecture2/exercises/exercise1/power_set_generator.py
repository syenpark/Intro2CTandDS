# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def power_set(items):
    """
    inputs : a list 
    generates all combinations of n items
    """
    n = len(items)
    
    # enumerates the 2**n (== 1 << n) possible combinations
    for i in range(1 << n):
        combo = []
        
        for j in range(n):
            # tests bit jth of iterger i
            if (i >> j) & 1:
                combo.append(items[j])
                
        yield combo
            
    
foo = power_set(['a', 'b', 'c'])