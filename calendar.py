"""
This is a basic calendar that the user
can interact with from the command line.
"""

from time import sleep, strftime

user_first_name = input("Please enter your first name: ")

calendar = {}

# create a welcome message function
def welcome():
  print("Welcome, " + user_first_name + ".")
  print("Opening calendar...")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y"))
  print("Current time: " + strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do?")

# start to build the functionality of calendar
def start_calendar():
  # first welcome the user
  welcome()
  start = True
  while start:
    user_choice = input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()

    if user_choice == "V":  
      if len(calendar.keys()) < 1:
        print("Calendar is empty.")
      else:
        print(calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter the update: ")
      # modify code to check if date is valid for update or if it already exists
      calendar[date] = update

      print("Calendar updated.")
      print(calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      # this calendar will not allow you to schedule something for a year in the past
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print("That is an invalid date.")
        try_again = input("Try Again? Y for Yes; N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print("Event successfully added.")
        print(calendar)
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("Calendar is empty.")
      else:
        event = input("What event? ") 
        for date in calendar.keys():
            if event == calendar[date]:
                del calendar[date]
                print("Event was deleted.")
            else:
                print("Incorrect event specified.")
    elif user_choice == "X":
      start = False
    else:
      print("Invalid command entered.")
      start = False

start_calendar()

