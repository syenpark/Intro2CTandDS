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
    if not foods or not room:
        return (0, ())
    
    elif foods[0].get_calories() > room:
        return max_value(foods[1:], room)
    
    else:
        candidate = foods[0]
        
        value_with_candidate, foods_with_candidate \
        = max_value(foods[1:], room - candidate.get_calories())
        
        value_with_candidate += candidate.get_value()
        
        
        value_without_candidate, foods_without_candidate \
        = max_value(foods[1:], room - candidate.get_calories())
        
        if value_with_candidate > value_without_candidate:
            return (value_with_candidate \
                    , foods_with_candidate + (candidate, ))
        else:
            return (value_without_candidate, foods_without_candidate)
    

def test_max_value(foods, constraint, is_print=True):
    print('Use search tree to allocate', constraint, 'calories')
    
    value, items = max_value(foods, constraint)
    
    print('Total value of items taken =', value)
    
    if is_print:
        for item in items:
            print(item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

foods = build_menu(names, values, calories)
test_max_value(foods, 750)