'''
Name: Omri Daniel
Date: 11/11/2018
Desc: Maze solver functions(module)
'''
from random import randint
import pygame
pygame.init()
w=600
h=600
screen=pygame.display.set_mode((w,h))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

#---------------------------------------#        
# Functions                             #
#---------------------------------------#    
def draw_maze(mList):
  '''
  (list)->(none)
  takes list to draw the maze in pygame
  '''
  screen.fill(black)
  rows=len(mList)
  col=len(mList[0])
  x=0
  y=0

  for i in range(rows):
    x=0
    for j in range(col):
      if mList[i][j]==' ':
        pygame.draw.rect(screen,white,(x,y,h//rows,h//col))
      if mList[i][j]=='S' or mList[i][j]=='G':
        pygame.draw.rect(screen,green,(x,y,h//rows,h//col))
      if mList[i][j]=='+':
        pygame.draw.rect(screen,blue,(x,y,h//rows,h//col))
      if mList[i][j]=='x':
        pygame.draw.rect(screen,red,(x,y,h//rows,h//col))
      x+=h//rows
    y+=h//rows
  pygame.display.update()
  pygame.time.delay(50)

def load_maze(fname):
	'''
  	(str)->(list)
  	takes txt file and returns as list
  	'''
	mazeList=[]
	file=open(fname, 'r')
	mazeRead=file.readlines()
	for i in range(len(mazeRead)): mazeRead[i]=mazeRead[i][0:-1]	#Remove \n
	for i in mazeRead: mazeList.append(list(i))						#Convert to 2-D
	return mazeList

def print_maze(mList):
	'''
  	(list)->(none)
  	takes list and prints as string
  	'''
	rows=len(mList)													#determine rows for maze
	for i in range(rows):	
		print(''.join(mList[i]))									#join columns for printing

def pick_random_location(mList):
	'''
  	(list)->(tup)
  	takes list and returns tuple of two points
  	'''
	x=randint(1,len(mList[0])-1)									#Pick x,y cords random
	y=randint(1,len(mList)-1)
	while mList[x][y]=='#':											#If path is blocked pick new x,y
		x=randint(1,len(mList[0])-1)
		y=randint(1,len(mList)-1)
	return(x,y)														#return x,y thats on path

def find_path(mList, x, y):
	'''
  	(list)(int)(int)->(bool)
  	uses start cords to solve the maze
  	'''
	if y>len(mList) or x>len(mList[0]) or mList[y][x]=='#' or mList[y][x]=='x' or mList[y][x]=='+': return False	#return false if move invalid
	if mList[y][x]=='G': return True																				#return true if reached end
	mList[y][x]='+'																									#mark as solution
	draw_maze(mList)
	if find_path(mList, x, y-1) or find_path(mList, x+1, y) or find_path(mList, x, y+1) or find_path(mList, x-1, y): return True 	#checks NESW moves
	mList[y][x]='x'																													#backtracking if no move
	draw_maze(mList)
	return False