# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
for node in nodes:
    line = node.getName()
    
    if not g.childrenOf(node):
        g.addEdge(Edge(g.getNode(line), g.getNode(line[0:1]+line[-1:]+line[1:-1])))
        g.addEdge(Edge(g.getNode(line), g.getNode(line[1:-1]+line[0:1]+line[-1:])))