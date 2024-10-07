def hourToMinute(hour):
    return hour * 60

def hourToSecond(hour):
    return hour * 3600

def hourToDay(hour):
    return hour / 24

def minuteToHour(minute):
    return minute / 60

hour = int(input("Enter hour: "))
print(f'{hour} hour is equal to {hourToMinute(hour)} minutes')
print(f'{hour} hour is equal to {hourToSecond(hour)} seconds')
print(f'{hour} hour is equal to {hourToDay(hour)} days')

minute = int(input("Enter minute: "))
print(f'{minute} minute is equal to {minuteToHour(minute)} hours')