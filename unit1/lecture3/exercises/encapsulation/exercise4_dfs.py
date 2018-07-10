# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
import graph

def counstrct_graph(names):
    nodes = []
    g = graph.Graph()
    
    # create nodes with each name
    for i in range(len(names)): 
        nodes.append(graph.Node(names[i]))
    
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

def print_path(path):
    """
    path is a list of nodes
    """
    result = []
    
    for i in range(len(path)):
        result.append(str(path[i]))
        
        # do append -> except the last
        if i != len(path) - 1:
            result.append('->')
    
    return ''.join(result)

def dfs(graph, start, end, path, shortest, print_flag = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    
    if print_flag:
        print('Current dfs path:', print_path(path))
        
    if start == end:
        return path
    
    for node in graph.child_of(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest,
                              print_flag)
                if new_path != None:
                    shortest = new_path
        elif print_flag:
            print('Already visited', node)
            
    return shortest
    
def shortest_path(graph, start, end, print_flag = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return dfs(graph, start, end, [], None, print_flag)

def testSP(source, destination):
    names = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    g = counstrct_graph(names)
    sp = shortest_path(g, g.get_node(source), g.get_node(destination),
                      print_flag = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', print_path(sp))
    else:
        print('There is no path from', source, 'to', destination)

#testSP('Chicago', 'Boston')
testSP('ABC', 'CAB')
