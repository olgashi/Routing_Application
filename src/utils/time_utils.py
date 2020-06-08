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





