def get_value(x,y,grid):
  try:
    if grid[x+1][y] == None:
      get_value(x+1, y, grid)
  except IndexError:
    grid[x][y] = 1
    return
  try:
    if grid[x][y+1] == None:
      get_value(x,y+1,grid)
  except IndexError:
    grid[x][y] = 1
    return
  grid[x][y] = grid[x+1][y] + grid[x][y+1]

grid = [[None for x in range(21)] for y in range(21)]
get_value(0,0,grid)
print(grid[0][0])

#Recursively find how many paths to the end there are
#by adding the number of paths of the next 2 possible
#locations. At each edge of the grid there is only open
#possible path to the end
