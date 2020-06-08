class Package:
    """Constructor"""
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes="", status="In Hub", delivery_time="", truck_number=-1, delivery_start_time=""):
        self._package_id = int(package_id)
        self._address = address
        self._deadline = deadline
        self._city = city
        self._state = state
        self._zip_code = zip_code
        self._weight = weight
        self._status = status
        self._notes = notes
        self._delivery_time = delivery_time
        self._truck_number = truck_number
        self._delivery_start_time = delivery_start_time

    """Setters and getters"""

    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, new_package_id):
        self.package_id = new_package_id

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, new_deadline):
        self._deadline = new_deadline

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        self._city = new_city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code):
        self._zip_code = new_zip_code

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, new_notes):
        self._notes = new_notes

    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, new_delivery_time):
        self._delivery_time = new_delivery_time

    @property
    def truck_number(self):
        return self._truck_number

    @truck_number.setter
    def truck_number(self, new_truck_number):
        self._truck_number = new_truck_number

    @property
    def delivery_start_time(self):
        return self._delivery_start_time

    @delivery_start_time.setter
    def delivery_start_time(self, new_delivery_start_time):
        self._delivery_start_time = new_delivery_start_time