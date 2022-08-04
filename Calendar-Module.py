import calendar
x = list(map(int, input().split(' ')))
m, d, y = x[0], x[1], x[2]
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
