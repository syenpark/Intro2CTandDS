# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
import graph

def counstrct_graph():
    nodes = []
    g = graph.Graph()
    
    names = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    
    # create nodes with each name
    for name in names: 
        nodes.append(graph.Node(name))
    
    for n in nodes: 
        g.add_node(n)
        
    for node in nodes:
        line = node.get_name()
    
        if not g.child_of(node):
            g.add_edge(graph.Edge(g.get_node(line), \
                            g.get_node(line[0:1]+line[-1:]+line[1:-1])))
            g.add_edge(graph.Edge(g.get_node(line), \
                            g.get_node(line[1:-1]+line[0:1]+line[-1:])))
    return g
    
print(counstrct_graph())