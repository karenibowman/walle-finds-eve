######################################
#   Utilities for Path Creation      #
######################################

import dijkstra, sys

#OBSTACLE : Object to store obstacle data
class Obstacle:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value


#PATH : Object to store robot path definition data
class Path:
    def __init__(self):
        rows = 0
        cols = 0
        wI = 0
        wJ = 0
        eI = 0
        eJ = 0
        obstacles = []

    def set_plane(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def set_walle(self, i, j):
        self.wI = i
        self.wJ = j

    def set_eve(self, i, j):
        self.eI = i
        self.eJ = j

    def set_obstacles(self, costs):
        self.obstacles = costs

    #calulate the shortest path
    def find_path(self):
        #create graph
        graph = dijkstra.Graph()

        #construct vertices and edges
        for i in range(self.rows):
            for j in range(self.cols):
                id = i*self.rows+j
                adjacent = []
                if (i!=0):
                     adjacent.append((i-1)*self.rows+j)
                     graph.add_edge(id,(i-1)*self.rows+j, 1)
                if (j!=0):
                     adjacent.append(i*self.rows+j-1)
                     graph.add_edge(id,i*self.rows+j-1, 1)
                if (i!=(self.rows-1)):
                     adjacent.append((i+1)*self.rows+j)
                     graph.add_edge(id,(i+1)*self.rows+j,1)
                if (j!=(self.cols-1)):
                     adjacent.append(i*self.rows+j+1)
                     graph.add_edge(id,i*self.rows+j+1,1)
                new_v = dijkstra.Vertex(id, i, j, adjacent)
                graph.add_vertex(new_v)

        # update edges for obstacle nodes
        for edge in self.obstacles['costs']:
             id = edge['i']*self.rows + edge['j']
             graph.update_in_edges(id, edge['value'])

        #compute and convert the shortest path
        shortest_path = graph.shortest_path(self.wI*self.rows+self.wJ,self.eI*self.rows+self.eJ)
        dict_path = [{'i':v.i, 'j':v.j} for v in shortest_path]
        
        return {'steps': len(dict_path), 'path': dict_path}
