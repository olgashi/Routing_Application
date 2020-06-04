import operator
import csv
import re

from src.classes.vertex import Vertex
from src.classes.graph import Graph
from src.classes.hashtable import HashTable
from src.classes.package import Package
from src.classes.truck import Truck


def shortest_between_two_points(g, start_vertex, end_vertex):
    print((start_vertex, end_vertex))
    print('--------------')
    for edge in g.edge_weights:
        # print((start_vertex, end_vertex))
        print(edge)
        if edge == (start_vertex, end_vertex):
            return g.edge_weights[edge]


# package_id, address, city, state, zip_code, deadline, weight, notes="", status="In Hub"
def read_packages_csv_file(file_name, h, packages_list):
    with open(file_name, newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=",")
        for row in file_reader:
            # print(row)
            package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            # print(package.address, package.zip_code)
            h.insert(package.package_id, package)
            packages_list.append(package)


def read_locations_csv_file(file_name, g, h):
    with open(file_name, newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=",")
        location_matrix = []
        vertex_a = None
        vertex_b = None
        for row in file_reader:
            row_address = re.sub('\(|\)', ' ', row[1])
            row_address = row_address.replace('\n', '').lstrip().rstrip()
            sliced_dist = row[2:]
            sliced_dist.insert(0, row_address)
            location_matrix.append(sliced_dist)
            counter = 1
        for row in location_matrix:
            # vertex_a = Vertex(location_matrix[row][0])
            g.add_vertex(row[0])

        for row in range(0, len(location_matrix)):
            for i in range(counter, len(location_matrix)):
                #     vertex_b = Vertex(location_matrix[i][0])
                # #     g.add_vertex(vertex_b)
                g.add_undirected_edge(location_matrix[row][0], location_matrix[i][0],
                                      float(location_matrix[row][i + 1]))
            counter += 1


h = HashTable()
g = Graph()
packages_to_deliver = []
packages_delivered_together = [3, 6, 9, 13, 14, 16, 18, 19, 20, 25, 28, 32, 36, 38]

read_packages_csv_file('package-data.csv', h, packages_to_deliver)
read_locations_csv_file('distances-between-locations.csv', g, h)

truck1 = Truck()
truck1.start_time = "8:00 am"
truck2 = Truck()

for i in range(1, 41):
    print(packages_to_deliver[i])
    if packages_to_deliver[i].package_id not in packages_delivered_together and len(truck1.packages) < 16:
        truck1.packages.append(packages_to_deliver[i])
        del packages_to_deliver[i]
for pkg in packages_to_deliver:
    print(pkg.package_id)
    if len(truck2.packages) < 16:
        truck2.packages.append(pkg)
        packages_to_deliver.remove(pkg)


print(len(truck1.packages))
print(len(truck2.packages))
print(len(packages_to_deliver))

