"""
file name: DJ38TSP.py
created by: Jasmy Elizabeth Joson
created on: May 28, 2020.
"""

import numpy as np
import matplotlib.pyplot as plt
from satsp import solver
import sys
import time


def plotBestTSP(path, points):
    '''The method plot the best solution for the TSP problem'''
    
    # Rearranging the co-ordinates of the cities according to the shortest path.
    coords = [[points[i-1][1], points[i-1][2]] for i in path.astype(int)]
    coords = np.array(coords)
    x = coords[:,0]
    y = coords[:,1]
    
    plt.figure(figsize=(8, 8))
    #Plotting the cities.
    plt.plot(x, y, 'o', color='black')
    
    # Draw the best path for the TSP problem
    plt.plot([x[-1], x[0]], [y[-1], y[0]], '-', color='black')
    for i in range(len(x)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], '-', color='black')
    plt.show()

def getCoordinates():
    ''' This function creates an array of city coordinates along with the city id.
        Return an array of shape N*3, where N is the number of cities.'''
    coords_list = []
    with open('./dj38/dj38tsp.txt', 'r') as file:
        for line in file:
            coords_list.append([int(line.split()[0]), float(line.split()[1]), float(line.split()[2])])
    coord_array = np.array(coords_list)
    with open("./dj38/output.txt", "w") as f:
        print('The co-ordinates of the cities with id : ', file=f, end='\n\n')
        print(coords_list, file=f, end='\n\n')
    
    coord_array[:,0] = coord_array[:,0].astype(int)
    return coord_array

def main():
    coordinates = getCoordinates()

    stdoutOrigin=sys.stdout 
    sys.stdout = open("./dj38/epochs.txt", "w")
    #Calling satsp method to solve the TSP problem
    start_time = time.time()
    solver.Solve(coordinates, epochs=600)
    time_taken = time.time() - start_time
    
    with open("./dj38/output.txt", "a") as f:
        print('Time taken to compute the solution : ', time_taken, file=f, end='\n\n')
        print('The best TSP tour length : ', solver.GetBestDist(), file=f, end='\n\n')
        print('The best tour : ', np.array(solver.GetBestTour()).astype(int), file=f, end='\n\n')
    
    path = np.array(solver.GetBestTour())
    plotBestTSP(path.astype(int), coordinates)
    
    solver.PrintConvergence()

if __name__ == '__main__':
    main()