import datetime

"""
#Accessing the currnt date time using datetime date time object
current_date = datetime.datetime.now()
print("Currebt date is => ", current_date)
print("Currebt date is => ", current_date.year)
print("Currebt date is => ", current_date.month)
print("Currebt date is => ", current_date.day)
print("Currebt date is => ", current_date.hour)
print("Currebt date is => ", current_date.minute)
print("Currebt date is => ", current_date.second)
print("Currebt date is => ", current_date.strftime("%A"))

"""

#Creating Date Objects

x = datetime.datetime(2022, 12, 13, 13,54)
print("Current datetime is => ", x)
print("Current datetime is => ", x.strftime("%B"))
