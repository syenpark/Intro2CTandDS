# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Node(object):
    def __init__(self, name):
        """
        type(name) == str
        """
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return self.__name
    
class Edge(object):
    def __init__(self, src, dest):
        """
        src and dest are instance of Node
        """
        self.__src = src
        self.__dest = dest
        
    def get_src(self):
        return self.__src
    
    def get_dest(self):
        return self.__dest
    
    def __str__(self):
        return self.get_src() + "->" + self.get_dest()
    
class Digraph(object):
    def __init__(self):
        self.__edges = {}
    
    def add_node(self, node):
        if node in self.__edges:
            raise ValueError('Duplicated node')
        else:
            self.__edges[node] = []
            
    def add_edge(self, node):
        src = node.get_src()
        dest = node.get_dest()
        
        if not (src in self.__edges and dest in self.__edges):
            raise ValueError('Node not in graph')
            
        self.__edges[src].append(dest)
        
    def child_of(self, node):
        return self.__edges[node]
    
    def has_node(self, node):
        return node in self.__edges
    
    def get_node(self, name):
        for node in self.__edges:
            if node.get_name() == name:
                return node
        
        raise NameError(name)
        
    def __str__(self):
        result = []
        
        for src in self.__edges:
            for dest in self.__edges[src]:
                result.append(src.get_name() + '->'+ dest.get_name() + '\n')
        
        # omit final new line
        result[-1] = result[-1][:-1]
        
        return ''.join(result)
    
class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_dest(), edge.get_src())
        Digraph.add_edge(self, rev)
