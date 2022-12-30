_graph = {
    "0": ["1", "2", "3"],
    "1": ["0", "6"],
    "2": ["0"],
    "3": ["0", "5", "4"],
    "4": ["3", "6", "7"],
    "5": ["3", "8"],
    "6": ["4", "1"],
    "7": ["4"],
    "8": ["5", "9", "10", "11"],
    "9": ["8"],
    "10": ["8"],
    "11": ["8"]
}


def shortest_path(graph: dict, start_node, end_node):
    queue = [start_node]
    visited = []
    parents = {}
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
                parents[neighbour] = current_node

    path = [end_node]
    current_node = end_node
    while current_node != start_node:
        current_node = parents[current_node]
        path.append(current_node)
    path.reverse()
    return path


print("2 size paths: " + str(sum([len(i) for i in _graph.values()])))


def generate_all_paths(graph:dict):
    paths = []
    n_nodes = len(graph)
    for i in range(0, n_nodes):
        for j in range(i+1, n_nodes):
            paths.append(shortest_path(graph, str(i), str(j)))
    paths.sort(key=lambda p: len(p))
    for i, p in enumerate(paths):
        print(i+1, p)


generate_all_paths(_graph)


