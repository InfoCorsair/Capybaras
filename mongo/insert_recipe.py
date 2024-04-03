###################################
#
#	INSERT_RECIPE.PY
# 
# The purpose of this file is simply to demonstrate
# how an insert_recipe request must be handled
#
###################################
from pymongo import MongoClient

# Establish connection to the database
mongo_url = "mongodb://localhost:27017"
mongo_db = MongoClient(mongo_url)

#print(mongo_db.list_database_names())

# Create the database
db = mongo_db["CapyCookin"]
# Create Collections
coll = db.create_collection("Ingredients")

# Create document
data = dict()

# Read in new recipe name
data["Name"] = input("What is the name of your recipe?\n")

# Input goes into a list until it sees "STOP"
lst = []
ingredient = ""
while (ingredient != "STOP"):
  ingredient = input("Ingredient: ")
  lst.append(ingredient)
data["Ingredients"] = lst
lst.clear()

# Input cook time
data["Cook_Time"] = input("How long does this recipe take to prepare?")

# Input goes into a list until it sees "STOP"
lst = []
tag = ""
while (tag != "STOP"):
  tag = input("Tag: ")
  lst.append(tag)
data["Tags"] = ["Vegetarian", "Breakfast", "Stovetop", "Frying Pan"]
lst.clear()

# Input number of servings
data["Servings"] = input("How many people does this recipe serve?")

# Input recipe
data["Recipe"] = input ("Type your recipe:\n")

# Insert recipe
x = coll.insert_one(data).inserted_id
