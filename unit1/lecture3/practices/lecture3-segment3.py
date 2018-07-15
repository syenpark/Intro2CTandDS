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
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    
    return g

def print_path(path):
    """
    path is a list of nodes
    """
    result = []
    
    for i in range(len(path)):
        result.append(str(path[i]))
        
        # if not last path
        if i != len(path) - 1:
            result.append('->')
            
    return ''.join(result) 

def DFS(graph, start, end, path, shortest, print_flag=False):
    """
    inputs:  graph is a Digraph; 
             start and end are nodes;
             path and shortest are lists of nodes
    returns: a shortest path from start to end in graph
    """
    # The way to get back after finding local shortest path;
    # Creates a new local veriable in each recursive execution
    # If path.append(start) is used, path is not local
    path = path + [start]
    
    if print_flag:
        print('Current DFS path:', print_path(path))
        
    if start == end:
        return path
    
    for node in graph.child_of(start):
        # Checks previous path to avoid cycles
        if node not in path:
            
            # if find a shortest path
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest, print_flag)
                
                if new_path != None:
                    shortest = new_path
        
        # Avoids cycles            
        elif print_flag:
            print('Already visited', node)
            
    return shortest
    
def shortest_path(graph, start, end, print_flag=False):
    """
    inputs:  graph is a Digraph;
             start and end are nodes
    returns: a shortest path from start to end in graph
    """
    return DFS(graph, start, end, [], None, print_flag)

def testSP(source, destination):
    g = build_city_graph(Digraph)
    
    src_node = g.get_node(source)
    dest_node = g.get_node(destination)
    
    sp = shortest_path(g, src_node, dest_node, print_flag=True)
    
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', print_path(sp))
    else:
        print('There is no path from', source, 'to', destination)

#testSP('Chicago', 'Boston')
testSP('Boston', 'Phoenix')

def BFS(graph, start, end, print_flag = False):
    """
    Assumes graph is a Digraph; start and end are nodes
    Returns a shortest path from start to end in graph
    """
    
    init_path = [start]
    path_queue = [init_path]
    
    while len(path_queue) != 0:
        # Get and remove oldest element in path_queue
        tmp_path = path_queue.pop(0)
        
        if print_flag:
            print('Current BFS path:', print_path(tmp_path))
            
        last_node = tmp_path[-1]
        
        if last_node == end:
            return tmp_path
        
        for next_node in graph.child_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
                
    return None

def shortestPath(graph, start, end, print_flag = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, print_flag)
    
testSP('Boston', 'Phoenix')
    
