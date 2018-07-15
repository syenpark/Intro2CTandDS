# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Node(object):
    def __init__(self, name):
        """
        name should be a string
        """
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return self.__name
    
class Edge(object):
    def __init__(self, src, dest):
        """
        src and dest are Node
        """
        self.__src = src
        self.__dest = dest
        
    def get_src(self):
        return self.__src
    
    def get_dest(self):
        return self.__dest
    
    def __str__(self):
        return self.__src.get_name() + '->' + self.__dest.get_name()
    
class Digraph(object):
    """
    build digraction graph
    """
    def __init__(self):
        self.__edges = {}
        
    def add_node(self, node):
        if node in self.__edges:
            raise ValueError('Duplicate node')
        else:
            self.__edges[node] = []
            
    def add_edge(self, edge):
        src = edge.get_src()
        dest = edge.get_dest()
        
        if not (src in self.__edges and dest in self.__edges):
            raise ValueError('Node not in graph')
            
        else:
            self.__edges[src].append(dest)
            
    def child_of(self, node):
        return self.__edges[node]
    
    def has_node(self, node):
        return node in self.__edges
    
    def get_node(self, name):
        for node in self.__edges:
            if node.get_name() == name:
                return node
        else:
            raise NameError(name)
            
    def __str__(self):
        result = []
        
        for src in self.__edges:
            for dest in self.__edges[src]:
                result.append(src.get_name() + '->'\
                         + dest.get_name() + '\n')
                
        return "".join(result)[:-1]
    
class Graph(Digraph):
    """
    build graph by adding edges and their reversed ones using Digraph
    """
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        reversed_edge = Edge(edge.get_dest(), edge.get_src())
        Digraph.add_edge(self, reversed_edge)
    
def build_city_graph(graph_type):
    g = graph_type()
    
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.add_node(Node(name))
    
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    
    return g


print('\nDigraph:')
print(build_city_graph(Digraph))
    
print('Graph:')
print(build_city_graph(Graph))