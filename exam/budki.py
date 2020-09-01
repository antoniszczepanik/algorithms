# n x m (0, 10_000)
# l budek (100, 1_000_000)
# r_i promień (0, 50)
# maksymalnie 15 budek w pasie o szerokości 100 (n)

from collections import namedtuple
from random import choices

Node = namedtuple('Node', ('n', 'm', 'r'))


def get_number_of_connections(nodes):
    # informacja o "najstarszym przodku" każdej budki (początkowo każda
    # wskazuje na siebie)
    roots = list(range(len(nodes)))

    # posortuj budki względem pierwszej współrzędnej
    nodes_sorted = sorted(nodes) # n log(n)

    for i, current_node in enumerate(nodes_sorted):
        # możemy spokojnie patrzeć tylko na 15 kolejnych budek - jeżeli na
        # odcinku o dł. 100 jest ich maksymalnie 15 to nie musimy sprawdzać
        # więcej (maksymalny promień to 50 -> maksymalna liczba sąsiadów = 15)
        if i + 16 >= len(nodes_sorted):
            next_nodes = nodes_sorted[i+1:]
            assert len(next_nodes) <= 15
        else:
            next_nodes = nodes_sorted[i+1:i+16]
            assert len(next_nodes) == 15

        for j, next_node in enumerate(next_nodes):
            # co najwyżej 15 O(n), więc nadal liniowo
            next_node_ix = i + j + 1
            # pomiń jeżeli mają wspólnego przodka (już są połączone)
            if roots[next_node_ix] != roots[i]:
                if calculate_distance(current_node, next_node) < min(next_node.r, current_node.r):
                    # zapisujemy wiadomość o "najstarszym przodku"
                    roots[next_node_ix] = roots[i]

    # zlicz unikalnych "najstarszych przodków"
    unique = set()
    for root in roots:
        if root not in unique:
            unique.add(root)

    return len(unique) - 1


def calculate_distance(node_1, node_2):
    return ((node_1.n - node_2.n)**2 + (node_1.m - node_2.m)**2) ** (1/2)


if __name__ == '__main__':
    # dane testowe
    l = 100000
    ns = choices(range(1, 1000), k=l)
    ms = choices(range(1, 1000), k=l)
    rs = [50 for x in range(l)]
    nodes = [Node(n, m, r) for n, m, r, in zip(ns, ms, rs)]

    print(get_number_of_connections(nodes))
