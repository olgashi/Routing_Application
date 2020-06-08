from core_algorithm import deliver_packages
from src.classes.graph import Graph
from src.classes.hashtable import HashTable
from src.classes.truck import Truck
from src.utils.time_utils import calculate_current_time
from src.utils.input_data_utils import read_packages_csv_file
from src.utils.input_data_utils import read_locations_csv_file


def start_daily_delivery():
    # initialize packages_hash, as a Hash Table data structure that will hold all packages with all their details
    packages_hash = HashTable()
    # initialize locations_graph, as a Graph data structure that will
    # hold all paths/routes for all given addresses/shipping destinations
    locations_graph = Graph()
    # manually presort packages into three 'buckets',
    # sorting takes into account all assumptions and deadlines specific to each package
    # truck3 will not be used
    packages_truck1 = [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]
    packages_truck2 = [26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 23, 11, 25]
    packages_truck2_second_round = [2, 33, 10, 5, 38, 8, 9, 3]
    # Read and parse packages data from file
    read_packages_csv_file('src/data/package-data.csv', packages_hash)
    # Read and parse data for locations between shipping destinations
    read_locations_csv_file('src/data/distances-between-locations.csv', locations_graph)
    # Initialize truck instances
    truck1 = Truck(1)
    truck2 = Truck(2)
    # Set start time for both trucks
    truck1.start_time = "8:00 AM"
    truck2.start_time = "9:05 AM"
    # Tracks total distance for all trucks throughout the day
    total_distance = 0
    # load trucks
    truck1.load_truck(packages_truck1, packages_hash)
    truck2.load_truck(packages_truck2, packages_hash)
    # set package status to "In Transit" once delivery starts
    truck1.set_delivery_status(packages_hash, "In Transit")
    # start delivery
    deliver_packages(truck1, packages_hash, locations_graph)
    #  total distance once truck 1 completed last delivery
    total_distance += truck1.distance
    # set package status to "In Transit" once delivery starts
    truck2.set_delivery_status(packages_hash, "In Transit")
    # start delivery
    deliver_packages(truck2, packages_hash, locations_graph)
    #  total distance once truck 2 completed last delivery
    total_distance += truck2.distance
    current_time = calculate_current_time(truck2.start_time, truck2.distance)
    # route from current location to HUB
    route_to_hub = (truck2.current_location, "HUB")
    distance_to_hub = 0
    # find path to HUB and determine distance, add to total distance
    for edge in locations_graph.edge_distances:
        if route_to_hub == edge:
            truck2.current_location = "HUB"
            distance_to_hub = locations_graph.edge_distances[edge]
            total_distance += distance_to_hub
    # update current time after truck2 returned to HUB
    current_time = calculate_current_time(current_time, distance_to_hub)
    # reset truck2 distance and packages, update time
    # clear packages from first round of deliveries
    truck2.remove_all_packages()

    package_with_wrong_address = packages_hash.search(9)
    """Package #9 has wrong address listed, the address will be corrected at 10:20am
    Through trial and error we know that truck2 will go out for the second delivery after 10:20am
    Making manual correction of the address for package #9"""
    package_with_wrong_address.address = "410 S State St"
    package_with_wrong_address.zip_code = "84111"
    # load truck2 with remaining packages and update start time and distance
    truck2.load_truck(packages_truck2_second_round, packages_hash)
    truck2.start_time = current_time
    truck2.distance = 0
    # set package status to "In Transit" once delivery starts
    truck2.set_delivery_status(packages_hash, "In Transit")
    # start delivery, truck 2 makes second round of deliveries
    deliver_packages(truck2, packages_hash, locations_graph)
    total_distance += truck2.distance
    current_time = calculate_current_time(truck2.start_time, truck2.distance)

    return [current_time, format(total_distance, '.2f'), packages_hash]

