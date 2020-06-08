def user_input():
    command = input("""
    id - look up details for a specific package;
    time - display package status of all packages at a specific time (only accepts am/pm format, for example 8:25 am);
    distance - display total distance for all trucks;
    clear - clear screen;
    exit - to exit;\n >>>\t""")

    return command


def display_package_details(package_id, packages_hash):
    package = packages_hash.search(int(package_id))
    print("Package details: ")
    print("-------------------------------")
    print("Id: " + str(package.package_id))
    print("Address: " + package.address)
    print("City: " + package.city)
    print("State: " + package.state)
    print("Zip code: " + package.zip_code)
    print("Weight: " + package.weight)
    print("Status: " + package.status)
    print("Notes: " + package.notes)
    print("Delivered on truck: " + package.truck_number)
    print("Delivery started at: " + package.delivery_start_time)
    print("Delivered at: " + package.delivery_time)
    print("-------------------------------")