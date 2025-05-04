grid = [list(map(int, input().split())) for _ in range(4)]


start= tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))\

def list1(start, goal, grid):
    neighbor = []
    open_list = [start]
    close_list = []

    while open_list:
        open_list.sort()
        current = open_list.pop(0)
        close_list.append(current)
        print(open_list)
        print(close_list)

       
	for neighbor in get_neighbors(grid,current):
		#print(neighbor)
		if grid(neighbor)==0:
			path.append(neighbor)
		else:
			continue
		print(neighbor)			
			


def get_neighbors(grid, pos):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        new_x, new_y = pos[0] + dx, pos[1] + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
            neighbors.append((new_x, new_y))
    return neighbors
    
    		
list1(start,goal,grid)		
