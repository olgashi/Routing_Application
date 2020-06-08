from src.utils.time_utils import calculate_current_time


class Truck:
    """Constructor"""
    _distance: int
    """'_packages' is a list of package ids that are loaded on the truck"""
    """'_distance' tracks distance for all deliveries over the course of a single trip"""

    def __init__(self, truck_id):
        self._id = truck_id
        self._packages = []
        self._start_time = ""
        self._distance = 0
        self._current_location = "HUB"
        self._current_time = ""

    """Setters and getters"""

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def packages(self):
        return self._packages

    @packages.setter
    def packages(self, new_packages):
        self._packages = new_packages

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, new_start_time):
        self._start_time = new_start_time

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, new_distance):
        self._distance = new_distance

    @property
    def current_location(self):
        return self._current_location

    @current_location.setter
    def current_location(self, new_current_location):
        self._current_location = new_current_location

    @property
    def current_time(self):
        return self._current_time

    @current_time.setter
    def current_time(self, new_current_time):
        self._current_time = new_current_time

    """Add packages to list of packages that are on the truck, takes package_id as int """

    def add_package(self, package_id: object):
        self._packages.append(package_id)

    """Remove all packages from the truck"""

    def remove_all_packages(self):
        self._packages = []

    def add_new_distance(self, new_distance):
        self._distance += new_distance

    def load_truck(self, packages_l: list, packages_h: hash):
        for index in range(0, len(packages_l)):
            package = packages_h.search(packages_l[index])
            if package is not None:
                package.truck_number = str(self._id)
                self.add_package(package)


    def set_delivery_status(self, packages_h, status):
        for package in self.packages:
            packages_h.search(package.package_id).status = status

    """Deliver packages, update time of delivery and status for each package"""
    def deliver_packages(self, packages_h, locations_g):
        self.current_time = self.start_time
        for package in self.packages:
            full_address = packages_h.search(package.package_id).address + ' ' + packages_h.search(
                package.package_id).zip_code
            route = (self.current_location, full_address)
            if self.current_location == full_address:
                packages_h.search(package.package_id).status = "Delivered"
                packages_h.search(package.package_id).delivery_time = self.current_time
            else:
                for edge in locations_g.edge_distances:
                    if route == edge:
                        self.current_location = full_address
                        self.add_new_distance(locations_g.edge_distances[edge])
                        packages_h.search(package.package_id).status = "Delivered"
                        packages_h.search(package.package_id).delivery_time = calculate_current_time(self.current_time,
                                                                                                     locations_g.edge_distances[
                                                                                                         edge])
                        self.current_time = calculate_current_time(self.current_time, locations_g.edge_distances[edge])
                        break
            # print("Package delivered at " + package.delivery_time)
