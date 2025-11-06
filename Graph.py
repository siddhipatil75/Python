from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node
    result = []  # To store the BFS traversal order

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            result.append(node)  # Add it to the result
            # Enqueue all unvisited neighbors
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
print("BFS Traversal:", bfs(graph, start_node))