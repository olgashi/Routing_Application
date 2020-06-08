from src.utils.time_utils import calculate_current_time

"""There are n^2/2 edges (where 1/2 is dropped and we end up with just n^2) in the graph, 
 where n is the number of unique addresses;
 worst case for determining the path between two given destinations is O(n^2);
 worst case for delivering all packages is O(n^2 * m) 
 where m is the total number of packages and n is the number of unique addresses
 """

def deliver_packages(truck, packages_h, locations_g):
    truck.current_time = truck.start_time
    for package in truck.packages:
        full_address = packages_h.search(package.package_id).address + ' ' + packages_h.search(
            package.package_id).zip_code
        route = (truck.current_location, full_address)
        if truck.current_location == full_address:
            packages_h.search(package.package_id).status = "Delivered"
            packages_h.search(package.package_id).delivery_time = truck.current_time
        else:
            for edge in locations_g.edge_distances:
                if route == edge:
                    truck.current_location = full_address
                    truck.add_new_distance(locations_g.edge_distances[edge])
                    packages_h.search(package.package_id).status = "Delivered"
                    packages_h.search(package.package_id).delivery_time = calculate_current_time(truck.current_time,
                                                                                                 locations_g.edge_distances[
                                                                                                     edge])
                    truck.current_time = calculate_current_time(truck.current_time, locations_g.edge_distances[edge])
                    break