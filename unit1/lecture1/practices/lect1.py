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
        
    def getValue(self):
        return self.value
    
    def getCost(self):
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