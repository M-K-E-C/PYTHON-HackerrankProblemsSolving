import calendar
a = input().split()

weekday = calendar.weekday(int(a[2]),int(a[0]),int(a[1]))
if weekday==0:
    print("MONDAY")
elif weekday==1:
    print("TUESDAY")
elif weekday==2:
    print("WEDNESDAY")
elif weekday==3:
    print("THURSDAY")
elif weekday==4:
    print("FRİDAY")
elif weekday==5:
    print("SATURDAY")
else :
    print("SUNDAY")
