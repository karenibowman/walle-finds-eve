######################################
#   Utilities for Graph Computation  #
######################################

import queue, sys
from sortedcontainers import SortedDict
from collections import defaultdict

#VERTEX: Object to store vertex data and neighbors
class Vertex:
    # Initializer for vertex with values i,j, node id, and adjacent node id values
    def __init__(self, node_id, i, j, adjacent):
        self.node = node_id
        self.i = i
        self.j = j
        self.dist = sys.maxsize
        self.adjacent = adjacent
        self.visited = False
        self.previous = None

    # Add a neighbor node id to the adjacent list for this vertex
    def add_neighbor(self, other):
        self.adjacent.append[other]

    # Compare operator for this object. Uses the attribute dist.
    def __cmp__(self, other):
        return cmp(self.dist, other.dist)

#GRAPH : Object to store vertices and edges, and compute a shortest path
class Graph:
    # Initialized vertices and edges data structures
    def __init__(self):
        self.vertices = {}
        self.edges = a = defaultdict(dict)

    # Adds a new Vertex object 'vertex' to the graph
    def add_vertex(self, vertex):
        self.vertices[vertex.node] = vertex

    # Adds new edges (u,v) and (v,u) with weight 'length' to the graph
    def add_edge(self, u, v, length):
        self.edges[u][v] = length
        self.edges[u][v] = length

    # Sets all ingoing edges to node to value length
    def update_in_edges(self, node_id, length):
        for v in self.vertices[node_id].adjacent:
            self.edges[v][node_id]=length

    # Finds the shortest path in the existing graph from the source to target
    # Input: Source node id (int), Target node id (int)
    # Output: the path, an ordered array of vertex objects
    def shortest_path(self, source_id, target_id):
        self.vertices[source_id].dist = 0
        found = False

        #create a sorted dicitonary to store unvisited nodes
        unvisited = SortedDict(self.vertices.copy())

        target = self.vertices[target_id]
        source = self.vertices[source_id]

        #iterate through unvisited nodes until there are none left or target
        #is found
        while (len(unvisited) > 0):
            min_dist = unvisited.popitem(0)[1]
            min_dist.visited = True

            if (min_dist.node == target.node):
                found = True
                break;

        #update the new shortest distance of min_dist's neighbors
            for v in min_dist.adjacent:
                new_dist = min_dist.dist + self.edges[min_dist.node][v]
                if (new_dist < self.vertices[v].dist and self.vertices[v].visited==False):
                    self.vertices[v].dist = new_dist
                    self.vertices[v].previous = min_dist.node
                    unvisited.update({v: self.vertices[v]})

        #backtrace to determine shortest path
        path = []
        if(found == True):
            current = target
            while (current != None):
                path.append(current)
                if current.previous!=None:
                    current = self.vertices[current.previous]
                else:
                    current = None

        return path
