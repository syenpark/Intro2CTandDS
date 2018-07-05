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
    
    def get_cost(self):
        return self.calories
    
    def get_density(self):
        try:
            return self.get_value() / self.get_cost()
        except ZeroDivisionError:
            return float('inf') 
    
    def __str__(self):
        return self.name + ': <' + str(self.get_value()) \
               + ', ' + str(self.get_cost()) + '>'
    
def build_menu(names, values, calories):
    menu = []
    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
        
    return menu

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]

foods = build_menu(names, values, calories)