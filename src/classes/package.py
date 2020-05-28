class Package:
    def __init__(self, package_id, address, deadline, city, zip_code, weight, status):
        self.package_id = int(package_id)
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
