# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def power_set(elements):
    """
    recursive version
    """
    if not elements:
        return [[]]
    else:
        result= []
        first = elements[0]
        subsets = power_set(elements[1:])
        
        for subset in subsets:
            result.append(subset)
            new = [first] + subset
            result.append(new)
        
        return result

print(power_set([1, 2, 3, 4]))