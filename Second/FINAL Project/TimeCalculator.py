def add_time(start, duration, day=None):
    # List of days for indexing
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Split start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert start time to 24-hour format
    if period.upper() == 'PM':
        if start_hour != 12:
            start_hour += 12
    elif period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Split duration
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add minutes and hours
    end_minute = start_minute + dur_minute
    extra_hour = end_minute // 60
    end_minute %= 60

    end_hour = start_hour + dur_hour + extra_hour
    days_later = end_hour // 24
    end_hour %= 24

    # Determine new period and convert to 12-hour format
    if end_hour >= 12:
        period = 'PM'
        if end_hour > 12:
            end_hour -= 12
    else:
        period = 'AM'
        if end_hour == 0:
            end_hour = 12

    # Format minutes to always show 2 digits
    minute_str = str(end_minute).rjust(2, '0')

    # Compute new day if day is provided
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_str = f", {new_day}"
    else:
        day_str = ""

    # Construct days later message
    if days_later == 1:
        later_str = " (next day)"
    elif days_later > 1:
        later_str = f" ({days_later} days later)"
    else:
        later_str = ""

    # Final result
    new_time = f"{end_hour}:{minute_str} {period}{day_str}{later_str}"
    return new_time
