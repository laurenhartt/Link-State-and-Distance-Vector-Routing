
import csv
import sys


############ Variables ###################

index_dict = {} # used for referencing the adjacency array with strings
source = '' # starting node
adj_matrix = [] # for storing nodes and their cost 
vertices = [] # a list of every vertex  
visited = [] # for tracking visited nodes

############ File Reading ################

# Get the csv file to read from the command line argument
#file_to_read = sys.argv[1]
file_to_read = "topology-1.csv"

# Open the csv file for reading
with open(file_to_read, newline = '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # Read through the csv file row-by-row and
    # build the adjacency matrix
    for row in csv_reader:
        adj_matrix.append(row)
    
# Take the first row from the csv file 
# to get the indexes and remove the blank space 
temp = adj_matrix[0]
#temp.pop(0)
vertices = temp


# Build the dictionary.
# This purpose of this dictionary is to allow us
# to reference the adjacency matrix using the 
# nodes as strings
index_dict = dict.fromkeys(temp, None)
for i in range(len(temp)):
    index_dict[temp[i]] = [i]


# Method for navigating the dictionary.
# This just takes the string of the node 
# you want to find and it matches it with the
# index of the adj. matrix.
def getIndex(s: str):
    list = index_dict[s]
    return list[0]

# Utility function to find the vertex with
# minimum distance value, from the set of verticies
# not yet inlcuded in the Minimum Spanning Tree
def minDistance(dist, visited):

    # Initilialize minium distance for next node
    min = sys.maxsize
    min_index = 1

    # Search not nearest node not in SPT
    for v in range(1,len(visited)):
        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_index = v
    
    return min_index

def printSolution(dist):
        print("Vertex tDistance from Source")
        for node in range(len(vertices)):
            print(node, "t", dist[node])

# Method to implement dijikstra's algorithim
def dijkstra(node):

    # initialize all nodes as unvisited
    visited = [False] * len(vertices)
    # set all distances to infinity
    dist = [sys.maxsize] * len(vertices)
    # set distance from start node to itself is 0
    dist[getIndex(node)] = 0

    for cout in range(1,len(visited)):

        u = minDistance(dist, visited)

        visited[u] = True

        for v in range(1,len(visited)):
            #print(type(adj_matrix[u][v]))
            if (int(adj_matrix[u][v]) > 0) and (visited[v] == False) and (dist[v] > dist[u] + int(adj_matrix[u][v])):
                dist[v] = dist[u] + int(adj_matrix[u][v])
                

    printSolution(dist)    
    print(visited)



        






def bellmanFord():
    pass

############## Main ########################
def main():
    pass
    # Get the starting point from the user input
    #source = input("Please, provide the source node: ")

    # Compute the min spanning tree
    #print("Shortest path tree for node {}".format(source))
    #dijkstra(source)

dijkstra('u')