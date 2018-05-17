def dijkstra(edges, neighbors, initial, end):
    visited = {initial: 0}
    passed = set()
    path = {}

    while visited.keys() > passed:
        visited_without_passed = {key: visited[key] for key in visited.keys() if key not in passed}
        if not visited_without_passed:
            break
        min_path_node = min(visited_without_passed, key=visited_without_passed.get)
        passed.add(min_path_node)

        for adjacent_node in neighbors.get(min_path_node, []):
            weight = visited[min_path_node] + edges[(min_path_node, adjacent_node)]
            if adjacent_node not in visited or weight < visited[adjacent_node]:
                visited[adjacent_node] = weight
                path[adjacent_node] = min_path_node

    node = end
    path_list = [node]
    while node != initial:
        node = path.get(node, None)
        if not node:
            return None
        path_list.append(node)
    result_weight = find_result_weight(edges, initial, path_list)
    return path_list[::-1], result_weight


def find_result_weight(edges, initial, path_list):
    result_weight = 1
    prev_node = initial
    for step in path_list[::-1][1:]:
        result_weight *= edges[(prev_node, step)]
        prev_node = step
    return result_weight


def make_edges(input):
    """
    :param input: массив массивов вида [[вершина, вес, ...], ...]
    :return: возвращает словарь ребер {(нач. вершина, кон. вершина), вес}
    """
    edges = {}
    for i in range(len(input)):
        for j in range(0, len(input[i]), 2):
            edges.update({(input[i][j], i+1): input[i][j+1]})
    return edges


def group_by_neighbors(edges):
    """
    :param edges: словарь ребер {(нач. вершина, кон. вершина), вес}
    :return: словарь соседей {вершина: [соседи], ...}
    """
    neighbors = dict()
    for x, y in edges:
        if neighbors.get(x):
            neighbors[x].append(y)
        else:
            neighbors[x] = [y]
    return neighbors


def main():
    lines = [a for a in open("in.txt").read().splitlines()]
    end = int(lines.pop())
    initial = int(lines.pop())
    nodes = [[int(b) for b in a.split()[:-1:]]
             for a in lines[1::]]
    edges = make_edges(nodes)
    neighbors = group_by_neighbors(edges)
    result = dijkstra(edges, neighbors, initial, end)

    if result:
        open("out.txt", "w").write("Y\n{}\n{}".format(" ".join(map(str, result[0])), str(result[1])))
    else:
        open("out.txt", "w").write("N")


if __name__ == '__main__':
    main()
