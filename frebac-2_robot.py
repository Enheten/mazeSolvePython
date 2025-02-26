#Fredrik Backlund
#frebac-2
#R0006E
#2025
#LTU
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

start = (0,0) # start position
end = (3,3) # end position
sizeGrid = 4 # size of the grid
obstacles = {(1,1), (1,2), (2,2)} # sets the hardcoded obstacles.

def move(start, goal): # will return the path if there is one.
    visited = [start]
    current_path = [start]
    x = 0
    y = 0
    while (x,y) != goal:
        if (can_visit(x + 1, y, visited) and can_move(x + 1, y)): # will check if its ok to move to the right, if it can, it will add +1 to x
            x += 1
        elif (can_visit(x - 1, y, visited) and can_move(x - 1, y)): # will check if it cant move to the right and if its ok to move to the left, if it can, it will subtract -1 from x
            x -= 1
        elif (can_visit(x, y + 1, visited) and can_move(x, y + 1)): # moves up
            y += 1
        elif (can_visit(x, y - 1, visited) and can_move(x, y - 1)): # moves down
            y -= 1
        elif not current_path: # if all positions have been popped, and the list is empty, there is no path to the end. 
            return None
        elif (( x, y ) == current_path[-1]): # if no changes have been made since last run, it will try to go back 1 step.
            current_path.pop()
            if current_path:
                x, y = current_path[-1]
        current_path.append((x, y)) # adds the current x, y position to path
        visited.append((x, y)) # also adds visited position.
    if (current_path[-1] == goal): # if last element in list is same position as goal, return path.
        return current_path
        

        
def can_move(x, y):
    if ((x >= 0 and x < sizeGrid) and (y >= 0 and y < sizeGrid ) and ((x,y) not in obstacles)): # checks so that the robot doesnt go off grid, in this case it would crash the program if the robot goes outside of the gridsize
        return True
    return False

def can_visit(x, y, visited): # check if the position is already visited and returns a value if the position can be visited.
    if ((x, y) in visited): 
        return False
    return True
path = move(start, end) # saves the return path from the function move. 
grid = np.zeros((sizeGrid, sizeGrid)) # creates a grid full of zeros, this represent white color.
for (x, y) in obstacles:
    grid[y, x] = 2 # sets the cordinates in the grid to a value of 2, which will represent black color. 
if path: # if there is a path, we will set the path color to blue
    for (x, y) in path:
        grid[y, x] = 1  # reverse y, x because imshow uses (row, col)
colormap = colors.ListedColormap(["white", "blue", "black"]) # saves the colors in an array
plt.imshow(grid, cmap=colormap, origin="lower") # using origin lower will make so that 0 , 0 is in the bottom left.
plt.xticks(range(sizeGrid)) # removes extra info like 0.5 between numbers.
plt.yticks(range(sizeGrid))

plt.show() # display the plot