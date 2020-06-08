from src.classes.graph import Graph
from src.classes.hashtable import HashTable
from src.classes.truck import Truck
from src.utils.time_utils import calculate_current_time
from src.utils.input_data_utils import read_packages_csv_file
from src.utils.input_data_utils import read_locations_csv_file

MAX_NUM_PACKAGES_PER_TRUCK = 18
TOTAL_NUM_PACKAGES = 40


def start_daily_delivery():
    # Tracks current time throughout the day
    current_time = "8:00 AM"
    packages_hash = HashTable()
    locations_graph = Graph()
    packages_truck1 = [14, 15, 16, 34, 20, 21, 19, 1, 7, 29, 37, 30, 13, 39, 27, 35]
    packages_truck2 = [26, 22, 24, 28, 4, 40, 31, 32, 17, 6, 36, 12, 18, 23, 11, 25]
    packages_truck2_second_round = [2, 33, 10, 5, 38, 8, 9, 3]
    # Read and parse packages data from file
    read_packages_csv_file('src/data/package-data.csv', packages_hash)
    # Read and parse data for locations between shipping destinations
    read_locations_csv_file('src/data/distances-between-locations.csv', locations_graph)
    # Initialize truck instances
    truck1 = Truck()
    truck2 = Truck()
    # Set start time
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
    truck1.deliver_packages(packages_hash, locations_graph)
    #  total distance once truck 1 completed last delivery
    total_distance += truck1.distance
    # set package status to "In Transit" once delivery starts
    truck2.set_delivery_status(packages_hash, "In Transit")
    # start delivery
    truck2.deliver_packages(packages_hash, locations_graph)
    total_distance += truck2.distance
    current_time = calculate_current_time(truck2.start_time, truck2.distance)
    route_to_hub = (truck2.current_location, "HUB")
    distance_to_hub = 0
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
    # load truck2 with remaining packages
    truck2.load_truck(packages_truck2_second_round, packages_hash)
    truck2.start_time = current_time
    truck2.distance = 0
    # set package status to "In Transit" once delivery starts
    truck2.set_delivery_status(packages_hash, "In Transit")
    # start delivery, truck 2 makes second round of deliveries
    truck2.deliver_packages(packages_hash, locations_graph)
    total_distance += truck2.distance
    current_time = calculate_current_time(truck2.start_time, truck2.distance)

    return [current_time, format(total_distance, '.2f'), packages_hash]

