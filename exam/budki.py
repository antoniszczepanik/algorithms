# n x m (0, 10_000)
# l budek (100, 1_000_000)
# r_i promień (0, 50)
# maksymalnie 15 budek w pasie o szerokości 100 (n)

from collections import namedtuple
from random import choices
from pprint import pprint

Node = namedtuple('Node', ('n', 'm', 'r'))


def get_number_of_connections(nodes):
    # informacja o "najstarszym przodku" każdej budki (początkowo każda
    # wskazuje na siebie)
    roots = list(range(len(nodes)))
    adjacency_list = {}
    for node in nodes:
        adjacency_list[node] = []

    # posortuj budki względem pierwszej współrzędnej
    nodes_sorted = sorted(nodes)

    for i, current_node in enumerate(nodes_sorted):
        # możemy spokojnie patrzeć tylko na 15 kolejnych budek - jeżeli na
        # odcinku o dł. 100 jest ich maksymalnie 15 to nie musimy sprawdzać
        # więcej (maksymalny promień to 50 -> maksymalna liczba sąsiadów = 15)
        if i + 16 >= len(nodes_sorted):
            next_nodes = nodes_sorted[i+1:]
        else:
            next_nodes = nodes_sorted[i+1:i+16]

        for j, next_node in enumerate(next_nodes):
            # co najwyżej 15 O(n), więc nadal liniowo
            next_node_ix = i + j + 1
            # pomiń jeżeli mają wspólnego przodka (już są połączone)
            if roots[next_node_ix] != roots[i]:
                if calculate_distance(current_node, next_node) < min(next_node.r, current_node.r):
                    # zapisujemy wiadomość o "najstarszym przodku"
                    roots[next_node_ix] = roots[i]
                    # dodajemy sąsiadującą budkę
                    adjacency_list[current_node].append(next_node)

    return get_number_of_connected_components(adjacency_list) -1

def get_number_of_connected_components(adjacency_list):
    # bfs zliczający liczbę połączonych komponentów
    queue = []
    # sprawdzaj czy dany node był już odwiedzony
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

def calculate_distance(node_1, node_2):
    return ((node_1.n - node_2.n)**2 + (node_1.m - node_2.m)**2) ** (1/2)


if __name__ == '__main__':
    # dane testowe
    l = 10
    ns = choices(range(1, 100), k=l)
    ms = choices(range(1, 100), k=l)
    rs = choices([50 for x in range(l)], k=l)
    nodes = [Node(n, m, r) for n, m, r, in zip(ns, ms, rs)]
    print(nodes)

    print(get_number_of_connections(nodes))
