'''
Programmer: Omri Daniel
Date: 11/11/2018
Desc: This program solves a maze of arbitrary size.
'''

from maze import*
import pygame
#---------------------------------------#        
# Main Program                          #
#---------------------------------------#    
while True:    
	fname = input("Enter filename: ")
	if fname.isalpha: break

maze = load_maze(fname)
# generate random start and goal locations
Sx,Sy = pick_random_location(maze)
maze[Sy][Sx] = 'S'
Gx,Gy = pick_random_location(maze)
maze[Gy][Gx] = 'G'
print ('\nHere is the maze with start and goal locations:')
print_maze(maze)

# now, find the path from S to G
find_path(maze, Sx, Sy)
print ('\nHere is the maze with the path from start to goal:')
maze[Sy][Sx]='S'
print_maze(maze)
'''
Questions  - answer the questions and add them as long strings in your Python file.
In order to demonstrate an understanding of this problem and solution, you should be able to answer the following questions:

1) What happens if instead of searching in the order North, East, South, West, FIND PATH searches North, South, East, West? 
Doesnt matter depends where start and end are.

2) When FIND-PATH returns False, does that mean there is no path from the start to the goal?
There is always a path but returnng false means it is going the wrong way or trying to make an invalid move.

3) Can parts of the maze be searched by FIND-PATH more than once? How does the algorithm deal with this situation?
Yes once a dead end is reached it results in backtracking and goes back on the moves to research the possible options

'''