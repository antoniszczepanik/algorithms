from collections import namedtuple
import heapq

graph = {
    "a": {"b": 4, "e": 1, "f": 3},
    "b": {"c": 5},
    "c": {"d": 8},
    "d": {},
    "e": {"b": 1},
    "f": {"d": 2},
}

Node = namedtuple("Node", ("min_distance", "name", "previous"))


infinity = 99999999

def dijkstra(graph, start, end):
    min_distances = []
    nodes_to_process = graph
    previous_nodes = {}

    heapq.heappush(min_distances, Node(0, start, None))

    while min_distances:
        min_node = heapq.heappop(min_distances)
        previous_nodes[min_node.name] = min_node.previous
        print(min_distances)
        for adjacent_node, distance_from_min_node in graph[min_node.name].items():
            new_node = Node(min_node.min_distance + distance_from_min_node,
                            adjacent_node,
                            min_node.name,
                            )

            # if new node already in heap:
                # check if new is smaller
                # push smaller and remove the old one

            heapq.heappush(min_distances, new_node)

    print("min_distances: ", min_distances)
    print("previous nodes: ", previous_nodes)

dijkstra(graph, 'a', 'd')
