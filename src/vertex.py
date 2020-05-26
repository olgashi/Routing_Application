class Vertex:
    # Constructor for a Vertex object
    def __init__(self, label):
        self.label = label
        self.distance = float("inf")
        self.prev = None

