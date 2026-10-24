
import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        f, cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if cost > best_cost.get(node, float('inf')):
            continue

        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight

            if new_cost < best_cost.get(
                neighbor, float('inf')
            ):
                best_cost[neighbor] = new_cost
                new_f = new_cost + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (new_f, new_cost, neighbor,
                     path + [neighbor])
                )

    return None, float('inf')


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 4,
    'E': 2,
    'G': 0
}

path, cost = astar(graph, heuristic, 'A', 'G')

if path:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("No path found")
