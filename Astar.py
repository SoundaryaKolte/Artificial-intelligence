# Heuristic: Manhattan Distance
def heuristic(state, goal):
    distance = 0
    for i in range(1, 9):  # Only tiles 1 to 8
        if i in state:
            x1, y1 = divmod(state.index(i), 3)
            x2, y2 = divmod(goal.index(i), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

# A* algorithm
def a_star(start, goal):
    open_list = [(start, [start], 0)]
    visited = []

    while open_list:
        open_list.sort(key=lambda x: x[2] + heuristic(x[0], goal))
        current, path, cost = open_list.pop(0)

        if current == goal:
            return path

        visited.append(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                open_list.append((neighbor, path + [neighbor], cost + 1))
    return None

# Print 3x3 board
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# MAIN
print("Enter initial state (use 0 for the blank):")
try:
    start_input = list(map(int, input("Enter 9 numbers (0-8) separated by spaces: ").split()))
    
    if sorted(start_input) != list(range(9)):
        raise ValueError("Input must contain all numbers from 0 to 8 exactly once.")
    
    start_state = tuple(start_input)

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    solution = a_star(start_state, goal_state)

    if solution:
        print("\nSteps to reach goal:")
        for step in solution:
            print_board(step)
    else:
        print("No solution found.")

except Exception as e:
    print(f"ERROR: {e}")
