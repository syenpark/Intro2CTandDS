# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Node(object):
    def __init__(self, name):
        """
        name is a string
        """
        self.name = name
        
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name