# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class WeightedEdge(Edge):
    """
    make a gragh weighted
    """
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        
    def getWeight(self):
        return self.weight
        
    def __str__(self):
        return Edge.getSource(self).getName() + '->' + Edge.getDestination(self).getName() + \
        ' (' + str(self.getWeight()) + ')'
