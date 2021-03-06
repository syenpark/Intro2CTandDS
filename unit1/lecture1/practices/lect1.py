# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Food(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
        
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_cost(self):
        return self.calories
    
    def get_density(self):
        try:
            return self.get_value() / self.get_cost()
        except ZeroDivisionError:
            return float('inf')
    
    def __str__(self):
        return self.name + ': <' + str(self.value) \
               + ', ' + str(self.calories) + '>'
        
def build_menu(names, values, calories):
    menu = []
    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    
    return menu

def greedy(menu, constraint, key, key_func):
    results = []
    value, calories = 0.0, 0.0
    
    # sort the first argment by key and O(nlogn) 
    foods_copy = sorted(menu, key=key_func, reverse=True)
    
    for food in foods_copy:
        if calories + food.get_cost() <= constraint:
            results.append(food)
            value += food.get_value()
            calories += food.get_cost()
        
    print('Use greedy by', key, 'to allocate', constraint,'calories')
    print('Total value of items taken  =', value)
    for result in results:
        print('    ', result)
    print('')

def test_greedy(constraint):
    key_funcs = {'value': Food.get_value, 'cost': lambda x: 1/Food.get_cost(x),
                 'density': Food.get_density}
    
    names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
    values = [89,90,95,100,90,79,50,10]
    calories = [123,154,258,354,365,150,95,195]
    
    menu = build_menu(names, values, calories)
    
    for key in key_funcs:
        greedy(menu, constraint, key, key_funcs[key])
    
test_greedy(1000)