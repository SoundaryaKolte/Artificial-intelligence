from collections import deque

def bfs(graph, start):
   
    queue = deque([start])
    visited = set()  
    
    while queue:
       
        node = queue.popleft()
        
            if node not in visited:
            visited.add(node) 
            print(node, end=" ")  
                for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

bfs(graph, 0)

