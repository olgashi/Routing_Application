class Graph:
    def __init__(self):
        self.edge_list = {}
        self.edge_distances = {}

    def add_vertex(self, new_address):
        self.edge_list[new_address] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_distances[(from_vertex, to_vertex)] = weight
        self.edge_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, address_a, address_b, weight=1.0):

        self.add_directed_edge(address_a, address_b, weight)
        self.add_directed_edge(address_b, address_a, weight)

    def find_vertex(self, address):
        return self.edge_list.index(address)

