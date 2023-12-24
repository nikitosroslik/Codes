def convert_time(time_str):
    if 'AM' in time_str.upper() or 'PM' in time_str.upper():
        hours, minutes = map(int, time_str[:-2].split(':'))
        is_pm = time_str.upper().endswith('PM') 
        if hours == 12:
            hours = 0 if is_pm else 12
        else:
            hours = hours + 12 if is_pm else hours
        return '{:02d}:{:02d}'.format(hours, minutes)
    else:
        hours, minutes = map(int, time_str.split(':'))
        
        if hours < 12:
            suffix = 'AM'
            if hours == 0:
                hours = 12
        else:
            suffix = 'PM'
            if hours > 12:
                hours = hours - 12
        return '{:02d}:{:02d} {}'.format(hours, minutes, suffix)
time_12h = '10:30 PM'
time_24h = convert_time(time_12h)
print(time_24h)

time_24h = '09:45'
time_12h = convert_time(time_24h)
print(time_12h)
