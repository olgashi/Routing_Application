def calculate_current_time(start_time, distance):
    # am_pm = ''
    start_time = start_time.split(' ')[0]
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
        mins = '0' + str(mins)
    if hour > 11:
        am_pm = 'PM'
    else:
        am_pm = 'AM'

    return str(hour) + ':' + str(mins) + ' ' + am_pm
