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
  print(now.strftime("%y %Y %b %A"))
  print(now.strftime("It was %A afternoon. I asked him what year it was and he replied %Y. The day of month was %d"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print("The locale's date and time is: ", now.strftime("%c"))
  print("The locale's date is: ", now.strftime("%x"))
  print("The locale's time is: ", now.strftime("%X"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Current time: %I:%M:%S %p"))
  print(now.strftime("24-hour time: %H:%M"))



if __name__ == "__main__":
  main()
