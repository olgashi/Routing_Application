from src.utils.time_utils import parse_time


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



def display_packages_in_list(list):
    if len(list) == 0:
        print("None")
    else:
        for package in list:
            print("Package number: " + str(package.package_id) + ", actual delivery time: " + str(package.delivery_time))
    # print("\n")


def combine_packages_by_time(time_str, packages_h):
    hour, mins, am_pm = parse_time(time_str)
    delivered = []
    in_transit = []
    in_hub = []

    if am_pm.lower() == 'pm':
        hour += 12
        if hour >= 24:
            hour -= 12
    for package_id in range(1, 41):
        package = packages_h.search(package_id)
        hour_package_delivered, mins_package_delivered, am_pm_package_delivered = parse_time(package.delivery_time)
        hour_delivery_started, mins_delivery_started, am_pm_delivery_started = parse_time(package.delivery_start_time)
        if am_pm_package_delivered.lower() == 'pm':
            hour_package_delivered += 12
            if hour_package_delivered >= 24:
                hour_package_delivered -= 12
            """If provided time is before the delivery started, place package in in_hub list"""
        if hour < hour_delivery_started or (hour == hour_delivery_started and mins < mins_delivery_started):
            in_hub.append(package)
            """If provided time is after or at the time delivery started"""
        elif hour > hour_delivery_started or (hour == hour_delivery_started and mins > mins_delivery_started):
            if hour > hour_package_delivered or (hour == hour_package_delivered and mins > mins_package_delivered):
                delivered.append(package)
            elif hour < hour_package_delivered or (hour == hour_package_delivered and mins < mins_package_delivered):
                in_transit.append(package)

    return [delivered, in_transit, in_hub]


def display_result_time_command(time_str, packages_h):
    delivered, in_transit, in_hub = combine_packages_by_time(time_str, packages_h)

    print("Status for all packages at " + time_str)
    print("\n")
    print("Delivered packages:")
    print("\n")
    display_packages_in_list(delivered)

    print("Packages in transit:")
    print("\n")
    display_packages_in_list(in_transit)

    print("Packages in hub:")
    print("\n")
    display_packages_in_list(in_hub)