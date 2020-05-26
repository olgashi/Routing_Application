import operator
from src.graph import Graph
from src.vertex import Vertex


def dijkstra_shortest_path(g, start_vertex):
    unvisited_queue = []
    for current_vertex in g.ajancesy_list:
        unvisited_queue.append(current_vertex)

    start_vertex.distance = 0

