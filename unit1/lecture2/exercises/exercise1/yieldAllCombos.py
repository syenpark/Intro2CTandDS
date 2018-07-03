# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    n = len(items)
    
    for i in range(3**n):
        bag1 = []
        bag2 = []
        
        for j in range(n):
            bits = (i // 3**j) % 3
            
            # If its bits is 1, the jth item is in bag1
            # or if its bits is 2, the jth item is in bag2
            # else, the jth item is in neither bag.
            if bits == 1:
                bag1.append(items[j])
            elif bits == 2:
                bag2.append(items[j])
    
        yield (bag1, bag2)

foo = yieldAllCombos(['a', 'b', 'c'])

"""
hints

With two bags, there are  possible combinations available.

With one bag we determined there were  possible combinations 
available by representing the bag as a list of binary bits, 0 or 1. 

Since there are N bits, and they can be one of two possibilities, 
there must be  possibilities.

With two bags there thus must be  possible combinations. 
You can imagine this by representing the two bags as a list of "trinary" bits, 
0, 1, or 2 (a 0 if an item is in neither bag; 1 if it is in bag1; 2 if it is in bag2). 
With the "trinary" bits, there are N bits that can each be one of three possibilities 
- thus there must be  possible combinations.
"""