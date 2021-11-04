
import csv
import sys


def main():
    # Varables
    source = '' # starting node
    adj_matrix = [] # for storing nodes and their cost

    # Get the csv file to read from the command line argument
    file_to_read = sys.argv[1]

    with open(file_to_read, newline = '') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        # Read through the csv file row-by-row
        for row in csv_reader:
            adj_matrix.append(row)
    
    print(adj_matrix)

    # Get the starting point from the user input
    #source = input("Please, privide the source node: ")

def dijkstra():
    pass

def bellmanFord():
    pass

main()
