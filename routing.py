
import csv
import sys
import copy

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

# Helper function for printing
def printSolution(dist, spt):

    # Make a list of keys to reference the dictionary 
    # using the values 
    key_list = list(index_dict.keys()) 

    
    for node in range(1,len(vertices)):
        print(key_list[node], ":", dist[node], end = " ")
    
    print("\n\nShortest path tree for node {}".format(source))
    for x in range(1, len(spt)):
        for y in range(len(spt[x])):
            print(key_list[spt[x][y]], end = " ")
        print(" ")
    
        

# Method to implement dijikstra's algorithim
# Algortihim referenced from GeeksForGeeks
# Link: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
def dijkstra(node):

    # initialize all nodes as unvisited
    visited = [False] * len(vertices)
    # set all distances to infinity
    dist = [sys.maxsize] * len(vertices)
    # initialize shortest path tree
    spt = [[None]] * len(vertices)
    # set distance from start node to itself is 0
    dist[getIndex(node)] = 0
    temp = []
    for i in range(1,len(visited)):
        
        # Pick the minimum distance vertex from
        # the set of verticies not yet processed
        # u is always equal to srch in first iteration
        u = minDistance(dist, visited)
        
        # Put the minimum distance vertex in the
        # shortest path tree
        visited[u] = True
        temp.append(u)

        for v in range(1,len(visited)):
            if (int(adj_matrix[u][v]) > 0) and (visited[v] == False) and (dist[v] > dist[u] + int(adj_matrix[u][v])):
                dist[v] = dist[u] + int(adj_matrix[u][v])
        spt[i] = temp.copy()
                
    printSolution(dist,spt) 


def bellmanFord():
    pass

############## Main ########################
def main():
    # Get the starting point from the user input
    source = input("Please, provide the source node: ")
    print("\nCosts of least-cost paths for source node: {}".format(source))

    dijkstra(source)

main()