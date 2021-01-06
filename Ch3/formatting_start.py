#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 

  now = datetime.now()
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("the current year is %Y"))
  print(now.strftime("%a %d %B %Y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("locale date and time is : %c"))
  print(now.strftime("locale date is: %x"))
  print(now.strftime("locale time is: %X"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("current hr min sec is: %H %M %S %p"))

if __name__ == "__main__":
  main();
