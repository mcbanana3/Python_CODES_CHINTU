from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

graph = {
    0: [1, 3, 8],
    1: [0, 7],
    2: [3, 5, 7],
    3: [0, 2, 4],
    4: [3, 8],
    5: [2, 6],
    6: [5],
    7: [1, 2],
    8: [0, 4],
}

start_node = 0
goal_node = 6

path = bfs(graph, start_node, goal_node)

if path:
    print(f"Path from node {start_node} to node {goal_node}: {path}")
else:
    print(f"No path found from node {start_node} to node {goal_node}")