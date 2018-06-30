# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
        
    def get_value(self):
        return self.value
    
    def get_cost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                + ', ' + str(self.calories) + '>'
                
def build_menu(names, values, calories):
    """
    returns list of Foods
    """
    menu = []
    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
        
    return menu

def greedy(items, max_cost, key_function):
    """
    inputs items a list, max_cost >= 0
    """
    items_copy = sorted(items, key=key_function, reverse=True)
    
    result = []
    total_value, total_cost = 0.0, 0.0
    
    for i in range(len(items_copy)):
        if(total_cost + items_copy[i].get_cost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_cost()
            total_value += items_copy[i].get_value()
            
    return (result, total_value)

def test_greedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print('Total value of items taken =', val)
    
    for item in taken:
        print('   ', item)