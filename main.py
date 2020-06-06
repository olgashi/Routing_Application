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


def calculate_current_time(start_time, distance):
    am_pm = ''
    start_time = start_time.split(' ')[0]
    start_time = start_time.split(':')
    hour = int(start_time[0])
    mins = int(start_time[1])
    if distance < 18:
        mins = int(mins + ((distance/18) * 60))
    else:
        time_to_add = divmod(distance, 18)
        hour = int(hour + time_to_add[0])
        mins = int(mins + (60 * (time_to_add[1] / 10)))

    if mins >= 60:
        hour = int(hour + divmod(mins, 60)[0])
        mins = int(mins - 60)
    elif mins < 10:
        mins = '0' + str(mins)
    if hour > 11:
        am_pm = 'PM'
    else:
        am_pm = 'AM'
    updated_time = str(hour) + ':' + str(mins) + ' ' + am_pm
    return updated_time


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
# Just passed with 68.7 miles. Very similar to Ryan K's solution.
# Truck 1 delivers 14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35.
pkgs_truck1 = [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]
pkgs_truck2 = [26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 23, 11, 25]
pkgs_truck2_second_round = [2, 33, 10, 5, 38, 8, 9, 3]
# Truck 2 delivers 25, 26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 23, 11.
# Returns to HUB and then delivers 2, 33, 10, 5, 38, 8, 9, 3.

# includes packages on truck 2 and those that have to be delivered together
packages_delivered_together = [3, 6, 9, 13, 14, 16, 18, 19, 20, 25, 28, 32, 36, 38]

read_packages_csv_file('package-data.csv', h, packages_to_deliver)
read_locations_csv_file('distances-between-locations.csv', g, h)

truck1 = Truck()
truck1.start_time = "8:00 AM"
truck2 = Truck()
truck2.start_time = "8:00 AM"

# current_location = "HUB"

current_time = "8:00 AM"
total_distance = 0
# load trucks
for i in range(1, len(pkgs_truck1)):
    truck1.packages.append(h.search(pkgs_truck1[i]))

for i in range(1, len(pkgs_truck2)):
    truck2.packages.append(h.search(pkgs_truck2[i]))

# add zipcode to package destination to match address of locations in
# full_address_package = h.search(4).address + ' ' + h.search(4).zip_code
# pair = ''
# deliver all packages on truck 1
for pkg in truck1.packages:
    full_address_package = h.search(pkg.package_id).address + ' ' + h.search(pkg.package_id).zip_code
    pair = (full_address_package, truck1.current_location)
    for edge in g.edge_weights:
        # print(edge)
        if pair == edge:
            truck1.current_location = full_address_package
            truck1.distance += g.edge_weights[edge]
            pkg.status = "Delivered"


#  total distance once truck 1 completed last delivery
total_distance += truck1.distance
# update current time
current_time = calculate_current_time(truck1.start_time, truck1.distance)
print("Truck 1 finished delivery at " + current_time)

# deliver all packages in truck 2
for pkg in truck2.packages:
    full_address_package = h.search(pkg.package_id).address + ' ' + h.search(pkg.package_id).zip_code
    pair = (full_address_package, truck2.current_location)
    pair2 = (full_address_package, "HUB")
    for edge in g.edge_weights:
        # print(edge)
        if pair == edge:
            truck2.current_location = full_address_package
            truck2.distance += g.edge_weights[edge]
            pkg.status = "Delivered"
        if pair2 == edge:
            print(g.edge_weights[edge])
total_distance += truck2.distance
current_time = calculate_current_time(truck2.start_time, truck2.distance)

print("Truck 2 finished delivery at " + current_time)

route_to_hub = (truck2.current_location, "HUB")

for edge in g.edge_weights:
    if route_to_hub == edge:
        truck2.current_location = "HUB"
        total_distance += g.edge_weights[edge]
        print(g.edge_weights[edge])

current_time = calculate_current_time(truck2.start_time, truck2.distance)

print("Truck 2 is back at the HUB")
print("Total distance " + str(total_distance))
# reset truck2 distance and packages, update time
truck2.start_time = current_time
truck2.distance = 0
truck2.packages = []
# load truck to with remaining packages
for i in range(1, len(pkgs_truck2_second_round)):
    truck2.packages.append(h.search(pkgs_truck2_second_round[i]))

#  truck 2 makes second round of deliveries
for pkg in truck2.packages:
    full_address_package = h.search(pkg.package_id).address + ' ' + h.search(pkg.package_id).zip_code
    pair = (full_address_package, truck2.current_location)
    for edge in g.edge_weights:
        # print(edge)
        if pair == edge:
            truck2.current_location = full_address_package
            truck2.distance += g.edge_weights[edge]
            pkg.status = "Delivered"
total_distance += truck2.distance
current_time = calculate_current_time(truck2.start_time, truck2.distance)
print("Truck 2 finished delivery at " + current_time)
print("Total distance travelled by all trucks: " + str(round(total_distance, 2)))

