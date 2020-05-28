import operator

from src.classes.vertex import Vertex
from src.classes.graph import Graph


def dijkstra_shortest_path(g, start_vertex):
    unvisited_queue = []
    # print(g.adjacency_list)
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    start_vertex.distance = 0

    while len(unvisited_queue) > 0:

        smallest_index = 0
        # this loop just finds the shortest distance from the given node for all the nodes in the list
        for i in range(1, len(unvisited_queue)):
            # if the next nodes distance to previous node is smaller than distance of the previous node
            # then remember the index
            # repeat for all elements in the unvisited queue, which is a list of all the nodes in g.adjacency list
            # print(unvisited_queue[i])
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        #         remove that node with the smallest distance from array and assign to current_vertex
        current_vertex = unvisited_queue.pop(smallest_index)
        # adjacency_list is the list of nodes that are connected to it, for example from the output
        # <src.classes.vertex.Vertex object at 0x10e08b670>: [<src.classes.vertex.Vertex object at 0x10e147f70>,
        # <src.classes.vertex.Vertex object at 0x10e183820>, <src.classes.vertex.Vertex object at 0x10e1838b0>]

        # these are the nodes connected [<src.classes.vertex.Vertex object at 0x10e147f70>,
        #  <src.classes.vertex.Vertex object at 0x10e183820>, <src.classes.vertex.Vertex object at 0x10e1838b0>]

        for adj_vertex in g.adjacency_list[current_vertex]:
            # g.adjacency_list[current_vertex] is all the nodes that are connected to current_vertex
            # edge_weight is the distance between two nodes
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            # edge_weight is a property of a graph
            # each edge weight represents a distance for a particular pair of nodes, for example:
            # (< src.classes.vertex.Vertex object at 0x10d62a670 >, < src.classes.vertex.Vertex object at 0x10d6e6f70 >): 8,
            alternative_path_distance = current_vertex.distance + edge_weight

            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = " -> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path


g = Graph()

vertex_a = Vertex("A")
vertex_b = Vertex("B")
vertex_c = Vertex("C")
vertex_d = Vertex("D")
vertex_e = Vertex("E")
vertex_f = Vertex("F")
vertex_g = Vertex("G")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)
g.add_vertex(vertex_e)
g.add_vertex(vertex_f)
g.add_vertex(vertex_g)

g.add_undirected_edge(vertex_a, vertex_b, 8)
g.add_undirected_edge(vertex_a, vertex_c, 7)
g.add_undirected_edge(vertex_a, vertex_d, 3)
g.add_undirected_edge(vertex_b, vertex_e, 6)
g.add_undirected_edge(vertex_c, vertex_d, 1)
g.add_undirected_edge(vertex_c, vertex_e, 20)
g.add_undirected_edge(vertex_d, vertex_f, 15)
g.add_undirected_edge(vertex_d, vertex_g, 12)
g.add_undirected_edge(vertex_e, vertex_f, 40)
g.add_undirected_edge(vertex_f, vertex_g, 10)

# Run Dijkstra's algorithm first.
dijkstra_shortest_path(g, vertex_a)

# Sort the vertices by the label for convenience; display shortest path for each vertex
# from vertex_a.
for v in sorted(g.adjacency_list, key=operator.attrgetter("label")):
    if v.pred_vertex is None and v is not vertex_a:
        print("A to %s: no path exists" % v.label)
    else:
        print("A to %s: %s (total weight: %g)" % (v.label, get_shortest_path(vertex_a, v), v.distance))