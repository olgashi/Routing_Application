class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes="", status="In Hub"):
        self.package_id = int(package_id)
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.notes = notes
