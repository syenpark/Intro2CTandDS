# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
    
    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight
    
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' \
               + str(self.weight) + '>'
               
def find_items():
    items = []

    items.append(Item('Dirt', 0, 4))
    items.append(Item('Computer', 30, 10))
    items.append(Item('Fork', 1, 5))
    items.append(Item('Problem Set', -10, 0))
    
    return items

def rob(items, metric):
    bag = []
    weight = 0
    weight_constraint = 14
    
    # evaluate each item
    eval_items = [metric(item) for item in items]
    
    highest_metric_value = max(eval_items)
    index_of_highest = eval_items.index(highest_metric_value)
    
    # while there are available items and there is room in the bag
    while max(eval_items) != -float('inf') and weight <= weight_constraint:         
        # if the highest item can be added to the bag, add it
        if weight + items[index_of_highest].get_weight() <= weight_constraint:
            bag.append(items[index_of_highest])
            weight += items[index_of_highest].get_weight()
        
        # whether the item was added or not, a burgler checked it's availability
        # change the item's status into unavailable
        eval_items[index_of_highest] = -float('inf')
        
        # pick the (next) highest item
        index_of_highest = eval_items.index(max(eval_items))
        
    return bag

def metric1(item):
    try:
        return item.get_value() / item.get_weight()
    except ZeroDivisionError:
        return float('inf')

def metric2(item):
    return  -item.get_weight()

def metric3(item):
    return item.get_value()

bag = rob(find_items(), metric1)

for item in bag:
    print(item)
    
    