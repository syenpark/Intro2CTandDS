# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
import graph_module

def build_permutation_graph():
    nodes = []
    g = graph_module.Graph()
    
    permutations = ('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA')
    
    # create nodes with each name
    for line in permutations: 
        nodes.append(graph_module.Node(line))
    
    for n in nodes: 
        g.add_node(n)
        
    for node in nodes:
        line = node.get_name()
    
        if not g.child_of(node):
            g.add_edge(graph_module.Edge(g.get_node(line), \
                            g.get_node(line[0:1]+line[-1:]+line[1:-1])))
            g.add_edge(graph_module.Edge(g.get_node(line), \
                            g.get_node(line[1:-1]+line[0:1]+line[-1:])))
    return g
    
print(build_permutation_graph())