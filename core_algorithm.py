from src.utils.time_utils import calculate_current_time

""" Average time to search for a single path is O(1), lookup (and total runtime complexity) for all packages is O(n) where n is a number of packages
 """


def deliver_packages(truck, packages_h, locations_g):
    """deliver_packages takes three arguments
    truck - truck that delivers packages,
    packages_h - all packages (including details for each package) in a form of a HashTable data structure
    locations_g - collection of paths for all locations represented as a Graph data structure,
                    any two locations/addresses have at least 1 path
    """
    truck.current_time = truck.start_time
    for package in truck.packages:
        """We need to combine address and zip code to match format of locations/addresses 
        stored in locations_g (locations Graph)"""
        full_address = packages_h.search(package.package_id).address + ' ' + packages_h.search(
            package.package_id).zip_code
        route = (truck.current_location, full_address)
        """Condition checks if next package has to be delivered to the same location as the one before (current location)"""
        if truck.current_location == full_address:
            packages_h.search(package.package_id).status = "Delivered"
            packages_h.search(package.package_id).delivery_time = truck.current_time
            """If next location is different lookup a route and get the distance, route lookup average case runtime is O(1)"""
        else:
            """if route exists, get distance between two addresses, update package status to 'Delivered',
            update time the package was delivered at, update total time this truck has travelled, update trucks current time"""
            if locations_g.edge_distances[route]:
                truck.current_location = full_address
                truck.add_new_distance(locations_g.edge_distances[route])
                packages_h.search(package.package_id).status = "Delivered"
                packages_h.search(package.package_id).delivery_time = calculate_current_time(truck.current_time,
                                                                                             locations_g.edge_distances[
                                                                                                 route])
                truck.current_time = calculate_current_time(truck.current_time, locations_g.edge_distances[route])
            else:
                raise ValueError("Path does not exist")
