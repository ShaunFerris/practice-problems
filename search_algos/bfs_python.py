from collections import deque
from typing import Dict, Set, List


class Graph:
    def __init__(self, nodes: Dict[str, Set[str]]):
        self.nodes = nodes

    def add_node(self, node_id: str):
        self.nodes[node_id] = set()

    def add_edge(self, node_id_a: str, node_id_b: str, directed=True):
        # graphs are directed by default, in that case node a is the origin
        if directed:
            self.nodes[node_id_a].add(node_id_b)
        else:
            self.nodes[node_id_a].add(node_id_b)
            self.nodes[node_id_b].add(node_id_a)

    def __str__(self):
        result = ""
        for node, neighbours in self.nodes.items():
            result += f"{node}: {', '.join(neighbours)}\n"
        return result


test_graph = Graph(
    {
        "1": {"2", "3"},
        "2": {"1", "3", "4", "5"},
        "3": {"1", "2"},
        "4": {"2", "5", "6"},
        "5": set(),
        "6": set(),
    }
)

print(test_graph)


def bfs(graph: Graph, start: str, end: str) -> List[str]:
    search_queue = deque()
    for neighbour in graph.nodes[start]:
        search_queue.append((neighbour, [start, neighbour]))
    checked = []

    while search_queue:
        curr_node, steps = search_queue.popleft()
        if not curr_node in checked:
            if curr_node == end:
                return steps
            else:
                checked.append(curr_node)
                for neighbour in graph.nodes[curr_node]:
                    search_queue.append((neighbour, steps + [neighbour]))
    return None


print(bfs(test_graph, "4", "3"))
