from collections import namedtuple, deque


Vertex = namedtuple('Vertex', ['children', 'already_seen'])

class Graph:
    def __init__(self, graph_dict: dict):
        self.vertices = {}
        for vertex, children in graph_dict.items():
            self.append(Vertex(children=children, already_seen=False))



def breadth_find_path(graph, start, find):
     q = deque()
     for vertex in graph.vertices:
         q.append(vertex)




if __name__ == "__main__":
    graph_dict = {
        1: [2, 3],
        2: [3, 4],
        3: [4, 5],
    }
    graph = Graph(graph_dict)
    breadth_find_path(graph, start=1, find=4)
