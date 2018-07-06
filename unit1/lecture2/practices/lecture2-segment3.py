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
        
    def get_value(self):
        return self.value
    
    def get_calories(self):
        return self.calories
    
    def get_density(self):
        try:
            return self.get_value() / self.get_calories()
        except ZeroDivisionError:
            return float('inf') 
    
    def __str__(self):
        return self.name + ': <' + str(self.get_value()) \
               + ', ' + str(self.get_calories()) + '>'
    
def build_menu(names, values, calories):
    menu = []
    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
        
    return menu

def max_value(foods, room):
    """    
    inputs : foods is a list of Food objects, and room is available space
    returns: a tuple of a maximum value and foods in that case 
    """
    global num_recur_calls
    num_recur_calls += 1
    
    if not foods or not room:
        result = (0, ())
        
    elif foods[0].get_calories() > room:
        result = max_value(foods[1:], room)
    
    else:
        with_val, with_foods \
        = max_value(foods[1:], room - foods[0].get_calories())
        
        with_val += foods[0].get_value()
        
        without_val, without_foods \
        = max_value(foods[1:], room - foods[0].get_calories())
        
        if with_val > without_val:
            result = (with_val, with_foods + (foods[0],))
        else:
            result = (without_val, without_foods)
        
    return result

def max_value_memo(foods, room, memo={}):
    """
    Dynamic programming
    
    inputs : foods is a list of Food objects, and room is available space
    returns: a tuple of a maximum value and foods in that case 
    """
    global num_memo_calls
    num_memo_calls += 1
    
    if (len(foods), room) in memo:
        result = memo[(len(foods), room)]
        
    elif not foods or not room:
        result = (0, ())
        
    elif foods[0].get_calories() > room:
        result = max_value_memo(foods[1:], room, memo)
    
    else:
        with_val, with_foods \
        = max_value_memo(foods[1:], room - foods[0].get_calories(), memo)
        
        with_val += foods[0].get_value()
        
        without_val, without_foods \
        = max_value_memo(foods[1:], room - foods[0].get_calories(), memo)
        
        if with_val > without_val:
            result = (with_val, with_foods + (foods[0],))
        else:
            result = (without_val, without_foods)
        
    memo[(len(foods), room)] = result
        
    return result

def test_max_value(foods, constraint, algorithm, is_print=True):
    print('Use search tree to allocate', constraint, 'calories')
    
    value, items = algorithm(foods, constraint)
    
    print('Total value of items taken =', value)
    
    if is_print:
        for item in items:
            print(item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

foods = build_menu(names, values, calories)

num_recur_calls = 0
test_max_value(foods, 750, max_value)
print('# of calls in recursion: ', num_recur_calls)
print('')
num_memo_calls = 0
test_max_value(foods, 750, max_value_memo)
print('# of calls in dynamic programming: ', num_memo_calls)