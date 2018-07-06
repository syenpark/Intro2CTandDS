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
    
class Edge(object):
    def __init__(self, src, dest):
        """
        inputs: src, dest are node
        """
        self.src = src
        self.dest = dest
        
    def get_source(self):
        return self.src
    
    def get_destination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()