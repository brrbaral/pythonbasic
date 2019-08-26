import calendar
cal=calendar.Calendar(firstweekday=1)
for x in cal.iterweekdays():
    print(x)
print("______________________________")


cal1=calendar.Calendar()
for x in cal1.itermonthdates(2019,4):

    print(x)