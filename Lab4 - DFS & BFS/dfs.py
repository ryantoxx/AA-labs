def dfs(graph, start, stop):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node == stop:
            return

        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
