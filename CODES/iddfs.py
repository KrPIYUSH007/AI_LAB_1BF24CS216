
def depth_limited_search(graph, node, goal, limit, path):
    if node == goal:
        return path + [node]

    if limit == 0:
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = depth_limited_search(
                graph, neighbor, goal,
                limit - 1, path + [node]
            )

            if result:
                return result

    return None


def iterative_deepening(graph, start, goal):
    depth = 0

    while True:
        result = depth_limited_search(
            graph, start, goal, depth, []
        )

        if result:
            return result

        depth += 1


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

path = iterative_deepening(graph, start, goal)
print("Path found:", path)
