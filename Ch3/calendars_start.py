#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2019, 5, 0, 0)
print(st)

# create an HTML formatted calendar
c2 = calendar.HTMLCalendar(calendar.SUNDAY)
st2 = c2.formatmonth(2019, 5)
print(st2)


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2019, 5):
    print(i)

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

print("Team meetings will be on:")
for x in range(1, 13):
    month = calendar.monthcalendar(2019, x)
    
    weekone = month[0]
    weektwo = month[1]
    if(weekone[calendar.FRIDAY] != 0):
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print("%10s %2d" %(calendar.month_name[x], meetday))