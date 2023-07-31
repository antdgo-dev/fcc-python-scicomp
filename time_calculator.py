# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

# For public execution and test
# https://replit.com/@ToniG4/boilerplate-time-calculator


def add_time(start, duration, day_of_week = None):

    start_hours, _string = start.split(":")
    start_minutes, meridiem = _string.split()

    duration_hours, duration_minutes = duration.split(":")


    # Change the time format to 24h
    if meridiem == "PM" and start_hours != "12" : start_hours = int(start_hours) + 12
    else : start_hours = int(start_hours)


    # Convert the "start" time and "duration" to minutes
    start_hours_to_min = start_hours * 60
    start_minutes = start_hours_to_min + int(start_minutes)

    duration_hours_to_min = int(duration_hours) * 60
    duration_minutes = duration_hours_to_min + int(duration_minutes)


    # Calculate the new time in minutes to convert it to time format 12h
    total_minutes = start_minutes + duration_minutes

    minutes = total_minutes % 60
    hours = total_minutes // 60

    days = 0

    days = hours // 24
    hours = hours % 24


    # Determine AM or PM
    if hours > 12 :
        hours = hours - 12
        meridiem = "PM"
    elif hours == 12 :
        meridiem = "PM"
    else :
        meridiem = "AM"
        if hours == 0 : hours = 12


    # Format minutes with 2 digits
    if minutes < 10 : minutes = "0" + str(minutes)
    else : minutes = str(minutes)


    new_time = str(hours) + ":" + minutes + " " + meridiem


    # Determine whether there is a new day of the week
    if day_of_week != None :

        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        day_of_week = day_of_week.lower()

        i = 0
        while day_of_week != days_of_week[i] : i = i + 1

        i = (i + days) % 7
        new_day_of_week = days_of_week[i][0].upper() + days_of_week[i][1:] # USE STR.CAPITALIZE

        new_time = new_time + ", " + new_day_of_week


    if days == 1 : new_time = new_time + " (next day)"
    if days > 1 : new_time = new_time + " (" + str(days) + " days later)"

    
    return new_time


# Example execution and tests

print( add_time("3:30 PM", "2:12") )
print( add_time("11:55 AM", "3:12") )
print( add_time("9:15 PM", "5:30") )
print( add_time("11:40 AM", "0:25") )
print( add_time("2:59 AM", "24:00") )
print( add_time("11:59 PM", "24:05") )
print( add_time("8:16 PM", "466:02") )
print( add_time("5:01 AM", "0:00") )
print( add_time("3:30 PM", "2:12", "Monday") )
print( add_time("2:59 AM", "24:00", "saturDay") )
print( add_time("11:59 PM", "24:05", "Wednesday") )
print( add_time("8:16 PM", "466:02", "tuesday") )

