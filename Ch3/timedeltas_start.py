#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, minutes= 4, seconds=3))

# print today's date
now = datetime.now()
print("today's date is " + str(now))
# print today's date one year from now
print("date after one year is " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument

print(str(now + timedelta(days=365, weeks=2, minutes=12, seconds=10)))

# calculate the date 1 week ago, formatted as a string
print(str(now - timedelta(weeks=1)))

### How many days until April Fools' Day?
t = date.today()
today = date(t.year, 3, 1)
afd = date(t.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if(afd < today):
    print("april fool gone by " % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)
# Now calculate the amount of time until April Fool's Day 
daysafter =  afd-today
print("after april foll" , daysafter.days)