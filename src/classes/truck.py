class Truck:
    """Constructor"""
    _distance: int

    def __init__(self):
        """'packages' is a list of package ids that are loaded on the truck"""
        self._packages = []
        self._start_time = ""
        self._distance = 0
        self._current_location = "HUB"

    """Setters and getters"""
        
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

    # Add packages to list of packages that are on the truck, takes package_id as int
    def add_packages(self, package_id):
        self._packages.append(package_id)
