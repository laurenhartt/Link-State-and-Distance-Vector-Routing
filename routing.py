
import csv
import sys


############ Variables ###################

index_dict = {} # used for referencing the adjacency array with strings
source = '' # starting node
adj_matrix = [] # for storing nodes and their cost   


############ File Reading ################

# Get the csv file to read from the command line argument
file_to_read = sys.argv[1]

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
def minDistance(dist, MST):
    pass

# Method to implement dijikstra's algorithim
def dijkstra(node: str):
    # initlialize the MST
    min_tree = []
    min_tree.append(source)




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

print(adj_matrix) # should be a 2D array
print(adj_matrix[getIndex('w')][getIndex('x')]) # w and x should cost 4