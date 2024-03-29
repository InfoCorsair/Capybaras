## This script asks for an ingredient name, and returns the measurement type (Weight, Amount, Etc)
import csv

with open("better_ingredients.csv",newline='') as csvfile:
  data = list(csv.reader(csvfile))

ingredient = input("Insert Ingredient Name: ")

for i in data:
  if ingredient in i:
    print(i[2])
#print(data)
