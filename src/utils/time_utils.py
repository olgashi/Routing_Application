def calculate_current_time(start_time, distance):
    start_time_split = start_time.split(' ')
    start_time = start_time_split[0]
    am_pm = start_time_split[1]
    start_time = start_time.split(':')
    hour = int(start_time[0])
    mins = int(start_time[1])

    if distance < 18:
        mins = int(mins + ((distance / 18) * 60))
    else:
        time_to_add = divmod(distance, 18)
        hour = int(hour + time_to_add[0])
        mins = int(mins + (60 * (time_to_add[1] / 10)))

    if mins >= 60:
        hour = int(hour + divmod(mins, 60)[0])
        mins = int(mins - 60)
    elif mins < 10:
        mins = int('0' + str(mins))

    if hour > 11 and am_pm == "AM":
        am_pm = 'PM'
    else:
        am_pm = 'AM'

    return str(hour) + ':' + str(mins).zfill(2) + ' ' + am_pm