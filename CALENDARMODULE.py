import calendar
a = input().split()

weekday = calendar.weekday(int(a[2]), int(a[0]), int(a[1]))

print(calendar.day_name[weekday].upper())

