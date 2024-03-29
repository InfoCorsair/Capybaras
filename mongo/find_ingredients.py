#Global list 
ingredient_list = []

#Open the file file and read 
open_file= open('better_ingredients.csv')
from csv import reader
ingredients_data = reader(open_file)
#DO NOT REMOVE "ingredients_data =list(ingredients_data)"
ingredients_data =list(ingredients_data)

def insert_IG():
	print("You have inserted Ingredient")


#Contain the ingredients Provided/Are Ingredients In Database
def find_ingred():
	global ingredient_list

	loop = True
	while loop:
		ingredient_name = input("What ingredient are you Looking for?: ").lower() 

		for row in ingredients_data:
			#If The Ingredient Name In The List/ Lower the Ingredients list
			if ingredient_name == row[1].lower():
				#print(row)
				ingredient_list.append(row)
  			
			elif ingredient_name not in row[1].lower() and ingredients_data is None:
				print("Would you like to insert a new ingredient? Type The Numbers Below:")
				print("1. Yes")
				print("2. No")
				response = input()
				if response == "1":
					print("Yes")
					insert_IG()
				elif response == "2":
					print("No New Ingredients Inserted.")
					return
 

		print("Any Other Ingredients?")
		print("1.Yes")
		print("2. No")
		response = input()
		if response == "1":
			continue
		elif response == "2":
			loop = False
		else:
			loop = False		
def find_by_amount():
	measurement = input("By Amount, Volume, or Weight: ")



#Made by Client With Amount of Each Ingredient They have
print("Select One Of The Following Numbers: ")
print("1. Search by Ingredient")
print("2. Search By Amount")

#Store Ingredients In A list
item_list = []

user_input = input()
if user_input == "1": 
	find_ingred()

elif user_input == "2":
	find_by_amount()

else:
	print("Not Valid")
	
print(ingredient_list)
