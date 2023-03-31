from collections import deque

def bfs(graph, start, stop):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        visited.add(node)

        if node == stop:
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
