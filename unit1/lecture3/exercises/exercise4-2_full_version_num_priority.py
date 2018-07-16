# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
class Node(object):
    def __init__(self, name):
        """
        inputs:  name should be a string
        """
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def __str__(self):
        return self.__name
    
class Edge(object):
    def __init__(self, src, dest):
        """
        inputs:  src and dest are instance of Node
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
    builds digraction graph
    """
    def __init__(self):
        """
        self.__edges is a dictionary to represent graph;
        Its key is a source node and values are adjacent nodes (=destinations)
        """
        self.__edges = {}
        
    def add_node(self, node):
        """
        Add a node in graph means add a key into a dictionary self.__edges
        """
        
        # Without this duplication checker,
        # destinations could have set a empty list again
        if node in self.__edges:
            raise ValueError('Duplicate node')
        else:
            self.__edges[node] = []
            
    def add_edge(self, edge):
        """
        """
        src = edge.get_src()
        dest = edge.get_dest()
        
        # Checks validity of edge
        if not (src in self.__edges and dest in self.__edges):
            raise ValueError('Node not in graph')
            
        else:
            self.__edges[src].append(dest)
            
    def child_of(self, node):
        return self.__edges[node]
    
    def has_node(self, node):
        return node in self.__edges
    
    def get_node(self, name):
        """
        inputs : name is a string and is of node 
        returns: a node of the name
        """
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
    builds graph by adding edges and their reversed ones using Digraph
    """
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        reversed_edge = Edge(edge.get_dest(), edge.get_src())
        Digraph.add_edge(self, reversed_edge)
        
def build_permutation_graph(graph_type):
    nodes = []
    g = graph_type()
    
    # create nodes with each name
    for line in permutations: 
        nodes.append(Node(line))
    
    for n in nodes: 
        g.add_node(n)
        
    for node in nodes:
        line = node.get_name()
    
        if not g.child_of(node):
            g.add_edge(Edge(g.get_node(line), \
                            g.get_node(line[0:1]+line[-1:]+line[1:-1])))
            g.add_edge(Edge(g.get_node(line), \
                            g.get_node(line[1:-1]+line[0:1]+line[-1:])))
    return g

def print_path(path):
    """
    path is a list of nodes
    """
    result = []
    
    for i in range(len(path)):
        result.append(str(permutations.index(str(path[i]))))
        
        # if not last path
        if i != len(path) - 1:
            result.append('->')
            
    return ''.join(result) 

def dfs_first_path(graph, start, end, path, shortest, print_flag=False):
    """
    inputs:  graph is a Digraph; 
             start and end are nodes;
             path and shortest are lists of nodes
    returns: the first found path from start to end in graph with DFS;
             and lower numbered node as a top priority
    """
    # The way to get back after finding local shortest path;
    # Creates a new local veriable in each recursive execution
    # If path.append(start) is used, path is not local
    path = path + [start]
    
    if print_flag:
        print('Current dfs_first_path path:', print_path(path))
        
    if start == end:
        return path
    
    # Sets top priority lower numbered nodes
    names = [node.get_name() for node in graph.child_of(start)]
    priority = sorted([permutations.index(name) for name in names])
    
    for node_index in priority:
        node_name = permutations[node_index]
        node = graph.get_node(node_name)
        
        # Checks previous path to avoid cycles
        if node not in path:
            
            # if find a shortest path
            if shortest == None or len(path) < len(shortest):
                new_path = dfs_first_path(graph, node, end, path, shortest, print_flag)
                
                if new_path != None:
                    shortest = new_path
                    
                    # Gives the first path found to the listed destination nodes;
                    # not to find out the shortest path
                    # If find the path from src to destination, finish it ASAP
                    break
        
        # Avoids cycles            
        elif print_flag:
            print('Already visited', permutations.index(node.get_name()))
            
    return shortest
    
def first_path(graph, start, end, print_flag=False):
    """
    inputs:  graph is a Digraph;
             start and end are nodes
    returns: the first found path from start to end in graph with DFS;
             and lower numbered node as a top priority
    """
    return dfs_first_path(graph, start, end, [], None, print_flag)

def testSP(src_index, dest_index):
    g = build_permutation_graph(Digraph)
    
    source = permutations[src_index]
    destination = permutations[dest_index]
    
    src_node = g.get_node(source)
    dest_node = g.get_node(destination)
    
    sp = first_path(g, src_node, dest_node, print_flag=True)
    
    if sp != None:
        print('Shortest path from', src_index, 'to',
              dest_index, 'is', print_path(sp))
    else:
        print('There is no path from', src_index, 'to', dest_index)

permutations = ('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA')

testSP(3, 1)