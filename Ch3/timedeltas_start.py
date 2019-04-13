#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=4, minutes=34))

# print today's date
today = date.today()
print(today.day)
# print today's date one year from now
print(today + timedelta(days=365))
one_year = today + timedelta(days=365)
print(one_year.strftime("Today's date one year from now will be: %D"))

# create a timedelta that uses more than one argument
print("IN 2 weeks and 3 days it will be: " + str(today + timedelta(weeks=2, days=3)))


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%a %d %B %Y")
print("One week ago it was ", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April Fools day already went by %d days ago " %(today-afd).days)
    afd = afd.replace(year=today.year + 1)

# Now calculate the amount of time until April Fool's Day  
new_afd = afd - today
print("It's just", new_afd.days, "days until the next april fools day")

