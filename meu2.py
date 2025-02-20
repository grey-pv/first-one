def add_time(start, duration, start_day=''):

    start_day = start_day.capitalize()

    days_passed = 0
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    s_time, s_AM_PM = start.split()
    s_hrs, s_mins = s_time.split(":")
    d_hrs, d_mins = duration.split(":")

    for y in range(int(d_mins)):
        s_mins = int(s_mins) + int(1)
        if int(s_mins) > 59:
            s_hrs = int(s_hrs) + int(1)
            s_mins = 0
            if int(s_hrs) == 12 and s_AM_PM == "AM":
                s_AM_PM = "PM"
            elif int(s_hrs) == 12 and s_AM_PM == "PM":
                s_AM_PM = "AM"
                days_passed = days_passed + 1 
                
            if s_hrs > 12:
                s_hrs = 1

    for x in range(int(d_hrs)):
        s_hrs = int(s_hrs) + int(1)
       
        if int(s_hrs) == 12 and s_AM_PM == "AM":
            s_AM_PM = "PM"
        elif int(s_hrs) == 12 and s_AM_PM == "PM":
            s_AM_PM = "AM"
            days_passed = days_passed + 1 
            
        if s_hrs > 12:
            s_hrs = 1
        

    
    if start_day in week:
        start_count = week.index(start_day)

        final_day = week[(start_count + days_passed) % 7]
    s_mins = int(s_mins)

    new_time = f"{s_hrs}:{s_mins:02.0f} {s_AM_PM}"
    if start_day in week:
            new_time += f", {final_day}"
    if days_passed == 1:
        new_time += " (next day)"

    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    print(new_time)
    return new_time


add_time('2:59 AM', '24:00') 