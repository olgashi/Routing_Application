def parse_time(time_str):
    start_time, am_pm = time_str.split(' ')
    hour, mins = start_time.split(':')
    return [int(hour), int(mins), am_pm]


def calculate_current_time(start_time, distance):
    hour, mins, am_pm = parse_time(start_time)

    if distance < 18:
        mins = int(mins + ((distance / 18) * 60))
    else:
        time_to_add = divmod(distance, 18)
        hour = int(hour + time_to_add[0])
        mins = int(mins + (60 * (time_to_add[1] / 10)))

    if mins >= 60:
        hour = int(hour + divmod(mins, 60)[0])
        mins = divmod(mins, 60)[1]

    if mins < 10:
        mins = int('0' + str(mins))

    if hour > 12:
        hour -= 12
        am_pm = "PM"

    if hour == 12:
        am_pm = "PM"

    return str(hour) + ':' + str(mins).zfill(2) + ' ' + am_pm


def display_packages_in_list(list):
    if len(list) == 0:
        print("None")
    else:
        for package in list:
            print("Package number: " + str(package.package_id))
            print("Delivered at: " + str(package.delivery_time))
    print("\n")


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
    print("Delivered packages:")
    display_packages_in_list(delivered)

    print("Packages in transit:")
    display_packages_in_list(in_transit)

    print("Packages in hub:")
    display_packages_in_list(in_hub)




