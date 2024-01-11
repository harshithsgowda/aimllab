def a_star(start, stop):
    open_set, closed_set, g, parents = {start}, set(), {start: 0}, {start: start}
    
    while open_set:
        current = min(open_set, key=lambda node: g[node] + heuristic(node))
        if current == stop or not Graph_nodes[current]:
            break

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, weight in get_neighbors(current) or []:
            if neighbor in closed_set: 
                continue

            tentative_g = g[current] + weight
            if neighbor not in open_set or tentative_g < g[neighbor]:
                open_set.add(neighbor)
                parents[neighbor], g[neighbor] = current, tentative_g

    if current != stop: 
        print('No path found!')
        return None

    path = [current]
    while current != start: 
        path.append(current := parents[current])

    path.reverse()
    print('Optimal Path:', path) 
    return path

def get_neighbors(node): 
    return Graph_nodes.get(node, [])

def heuristic(node): 
    return {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 1000, 'E': 1000, 'G': 0}.get(node, 0)

Graph_nodes = {'S': [['A', 1], ['B', 5], ['C', 8]], 'A': [['D', 3], ['E', 7], ['G', 9]],
               'B': [['G', 4]], 'C': [['G', 5]], 'D': None, 'E': None}

a_star('S', 'G')