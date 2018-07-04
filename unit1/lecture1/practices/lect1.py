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
    
    def get_calories(self):
        return self.calories
    
    def __str__(self):
        return self.name + ': <' + str(self.value) \
               + ', ' + str(self.calories) + '>'
        