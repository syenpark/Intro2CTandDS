# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Item(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
    
    def get_value(self):
        return self.value
    
    def get_calories(self):
        return self.calories
    
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' \
               + str(self.calories) + '>'
               
def build_menu():
    menu = []
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 
             'cola', 'apple', 'donut', 'cake']
    values = [89,90,95,100,90,79,50,10]
    calories = [123,154,258,354,365,150,95,195]
    
    for i in range(len(values)):
        menu.append(Item(names[i], values[i], calories[i]))
    return menu

def greedy(menu, constraint, metric):
    bag = []
    calories = 0
    calories_constraint = constraint
    
    # evaluate each item
    eval_menu = [metric(item) for item in menu]
    
    highest_metric_value = max(eval_menu)
    index_of_highest = eval_menu.index(highest_metric_value)
    
    # while there are available menu and there is room in the bag
    while max(eval_menu) != -float('inf') and calories <= calories_constraint:         
        # if the highest item can be added to the bag, add it
        if calories + menu[index_of_highest].get_calories() <= calories_constraint:
            bag.append(menu[index_of_highest])
            calories += menu[index_of_highest].get_calories()
        
        # whether the item was added or not, a burgler checked it's availability
        # change the item's status into unavailable
        eval_menu[index_of_highest] = -float('inf')
        
        # pick the (next) highest item
        index_of_highest = eval_menu.index(max(eval_menu))
        
    return bag

def max_value(item):
    return item.get_value()
    

def min_calories(item):
    return  -item.get_calories()

def max_value_to_calories_ratio(item):
    try:
        return item.get_value() / item.get_calories()
    except ZeroDivisionError:
        return float('inf')

def test_greedy(constraint):
    key_funcs = [max_value, min_calories, max_value_to_calories_ratio]
    
    for key_func in key_funcs:
        print('Use greedy by value to allocate', constraint, 'calories')
        print('Metric: max value')
        bag = greedy(build_menu(), constraint, key_func)

        for item in bag:
             print('   ', item)
    
        print('')
        
test_greedy(1000)
    