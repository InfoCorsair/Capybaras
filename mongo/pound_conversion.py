##Script that accepts a quanity and converts it either from pounds to ounces or ounces to pounds
import re

def to_ounces(pounds):
  return float(pounds)*16

def to_pounds(ounces):
  return float(ounces)/16

quantity = input("Enter quantity: ")
  
amount = ''.join((ch if ch in '0123456789.' else '') for ch in quantity)
print("Amount is: " + str(amount))

measurement = ''.join((x for x in quantity if not x.isdigit()))
measurement = measurement.replace('.','')
print("Type is: " + str(measurement))

float(amount)
if measurement == "oz":
  retval = to_pounds(amount)
  print(retval)

if measurement == "lb":
  retval = to_ounces(amount)
  print(retval)


