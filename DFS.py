def dfs(graph, start):
    
    stack = [start]
    visited = set()  
    
    while stack:
       
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)  
            print(node, end=" ")  
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

dfs(graph, 0)

