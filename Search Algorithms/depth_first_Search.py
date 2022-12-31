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


# Iterative approach
def depth_first_search_1(graph: dict, start_node):
    visited = []
    is_visited = dict(zip(graph.keys(), [False]*len(graph)))
    _stack = [start_node]
    while _stack:
        current_node = _stack.pop()
        if not is_visited[current_node]:
            visited.append(current_node)
            is_visited[current_node] = True
            for neighbour in graph[current_node]:
                if not is_visited[neighbour]:
                    _stack.append(neighbour)
    return visited


# Recursive version
def depth_first_search_2(graph: dict, start_node):
    visited = dict(zip(_graph.keys(), [False]*len(_graph)))

    def dfs(_start_node):
        visited[_start_node] = True
        neighbours_path = []
        for neighbour in graph[_start_node]:
            if not visited[neighbour]:
                neighbours_path += dfs(neighbour)
        return [_start_node] + neighbours_path
    return dfs(start_node)


print(depth_first_search_1(_graph, "9"))
print(depth_first_search_2(_graph, "9"))
