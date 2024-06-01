import datetime

presentDay = datetime.datetime.now().strftime("%A")
dateTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") 

print()
print(f"Today is {presentDay}")
print(dateTime, end = "\n")
