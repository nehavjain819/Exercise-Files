#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime
def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print(today)
  # print out the date's individual components
  print(today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  weekday = today.weekday()
  print(weekday)
  days = ["mon", "tues", "wed", "thus", "fri", "sat", "sun"]
  print("today date day is:", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  todays = datetime.now()
  print(todays)
  print()
  # Get the current time
  print(datetime.time(datetime.now()))
 

  
if __name__ == "__main__":
  main()
  