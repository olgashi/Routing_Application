import csv
import re

from src.classes.package import Package


def read_packages_csv_file(file_name, h):
    with open(file_name, newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=",")
        for row in file_reader:
            package = Package(int(row[0]), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip(), row[5], row[6], row[7])
            h.insert(package.package_id, package)


def read_locations_csv_file(file_name, g):
    with open(file_name, newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=",")
        location_matrix = []
        # the loop removes () from zip code values
        for row in file_reader:
            row_address = re.sub('[()]', ' ', row[1])
            row_address = row_address.replace('\n', '').strip()
            sliced_dist = row[2:]
            sliced_dist.insert(0, row_address)
            location_matrix.append(sliced_dist)
        counter = 1
        # O(n), n number of unique locations (vertices)
        for row in location_matrix:
            g.add_vertex(row[0])
        # populate locations graph with routes (edges) between any two points/addresses,
        # with corresponding distances between points
        # O(N(N-1))/2 or O(n^2)
        for row in range(0, len(location_matrix)):
            for index in range(counter, len(location_matrix)):
                g.add_undirected_edge(location_matrix[row][0], location_matrix[index][0],
                                      float(location_matrix[row][index + 1]))
            counter += 1
