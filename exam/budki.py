# n x m (0, 10_000)
# l budek (100, 1_000_000)
# r_i promień (0, 50)
# maksymalnie 15 budek w pasie o szerokości 100 (n)

from collections import namedtuple
from random import sample, choices

Node = namedtuple('Node', ('n', 'm', 'r'))


def get_number_of_connections(nodes):
    adj_list = {}
    for node in nodes:
        adj_list[node] = []

    # posortuj budki względem pierwszej współrzędnej
    nodes_sorted = sorted(nodes) # (n log(n))
    for i, current_node in enumerate(nodes_sorted):
        # możemy spokojnie patrzeć tylko na 15 kolejnych budek - jeżeli na
        # odcinku o dł. 100 jest ich maksymalnie 15 to nie musimy sprawdzać
        # więcej (maksymalny promień to 50, więc kolejne budki nie będą sąsiadować)
        if i + 16 >= len(nodes_sorted):
            next_nodes = nodes_sorted[i+1:]
            assert len(next_nodes) <= 15
        else:
            next_nodes = nodes_sorted[i+1:i+16]
            assert len(next_nodes) == 15

        for next_node in next_nodes:
            # najwięcej 15 O(n), więc nadal liniowo
            if calculate_distance(current_node, next_node) < min(next_node.r, current_node.r):
                # możemy połączyć obydwa node'y na grafie
                adj_list[current_node].append(next_node)

    return get_number_of_connected_components(adj_list) - 1


def calculate_distance(node_1, node_2):
    return ((node_1.n - node_2.n)**2 + (node_1.m - node_2.n)**2) ** (1/2)


def get_number_of_connected_components(adjacency_list):
    # bfs zliczający liczbę połączonych komponentów
    queue = []
    # sprawdzaj czy dany node był już odwiedzony
    visited = {}
    for node in adjacency_list:
        visited[node] = False

    number_of_components = 0
    for node in adjacency_list:
        if not visited[node]:
            queue.append(node)
            number_of_components += 1
            while queue:
                current_node = queue.pop(0)
                visited[current_node] = True
                for adjacent_node in adjacency_list[current_node]:
                    if not visited[adjacent_node]:
                        queue.append(adjacent_node)

    return number_of_components




# wygeneruj dane
l = 1000
ns = choices(range(1, 1000), k=l)
ms = choices(range(1, 1000), k=l)
rs = choices(range(1, 200), k=l)
nodes = [Node(n, m, r) for n, m, r in zip(ns, ms, rs)]

print(get_number_of_connections(nodes))
