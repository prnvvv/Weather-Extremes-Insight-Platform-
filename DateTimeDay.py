import datetime

# Get the current day of the week
presentDay = datetime.datetime.now().strftime("%A")

# Get the current date and time
dateTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") 

# Print the results
print()
print(f"Today is {presentDay}")
print(dateTime, end="\n")
