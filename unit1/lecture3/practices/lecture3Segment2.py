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
        self.src = src
        self.dest = dest
        
    def get_src(self):
        return self.src
    
    def get_dest(self):
        return self.dest
    
    def __str__(self):
        return self.src.get_name() + '->' + self.dest.get_name()
    
class Digraph(object):
    def __init__(self):
        self.edges = {}
        
    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    
    def add_edge(self, node):
        src = node.get_src()
        dest = node.get_dest()
        
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
            
        self.edges[src].append(dest)
        
    def child_of(self, node):
        return self.edges[node]
    
    def has_node(self, node):
        return node in self.edges
    
    def get_node(self, name):
        for node in self.edges:
            if node.get_name() == name:
                return node
        
        raise NameError(name)
        
    def __str__(self):
        result = []
        
        for src in self.edges:
            for dest in self.edges[src]:
                result.append(src.get_name() + '->'+ dest.get_name() + '\n')
        
        # omit final new line
        result[-1] = result[-1][:-1]
        
        return ''.join(result)
    
class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_dest(), edge.get_src())
        Digraph.add_edge(self, rev)
        
def build_city_graph(graph_type):
    g = graph_type()
    
    names = ['Boston', 'Providence', 'New York', 'Chicago',
             'Denver', 'Phoenix', 'Los Angeles']
    
    # create 7 nodes with each name
    for name in names: 
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
    
print(build_city_graph(Graph))
        
"""
output:
    
    Boston->Providence
    Boston->New York
    Boston->Providence
    Boston->Los Angeles
    Providence->Boston
    Providence->Boston
    Providence->New York
    New York->Boston
    New York->Providence
    New York->Chicago
    New York->Denver
    Chicago->New York
    Chicago->Denver
    Denver->Chicago
    Denver->Phoenix
    Denver->New York
    Phoenix->Denver
    Los Angeles->Boston
"""