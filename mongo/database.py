from pymongo import MongoClient

# Establish connection to the database
mongo_url = "mongodb://localhost:27017"
mongo_db = MongoClient(mongo_url)

#print(mongo_db.list_database_names())

# Create the database
db = mongo_db["CapyCookin"]
# Create Collections
coll = db.create_collection("Recipe")

# Create document
data = dict()
data["Name"] = "Fried Egg"
data["Ingredients"] = ["Egg", "Oil"]
data["Amounts"] = ["1", "1"]
data["Cook_Time"] = "240"
data["Tags"] = ["Vegetarian", "Breakfast", "Stovetop", "Frying Pan"]
data["Servings"] = "1"
data["Recipe"] = "Start with a great egg. I like to buy local eggs, which have the most beautiful golden yellow yolks. Free-range organic eggs are great, too. Cook one or two eggs at a time. I usually just cook one egg at a time in a small skillet because sometimes the two eggs cross paths and stick together. Use a cast iron skillet if you have one. Cast iron is non-toxic and retains heat well. If you warm up the pan as directed before adding the oil, it should offer a great non-stick cooking surface. I use my 8″ cast iron pan (affiliate link) for single eggs, or 12″ pan for two eggs. My next best bet would be stainless steel. I’m hesitant to suggest non-stick pans because high heat can damage the coatings and release toxic PFOA’s into the air. Crack the egg into a bowl first. You can more easily avoid oil splatters this way. I also find that pouring from a bowl yields a more evenly shaped fried egg that cooks a little more evenly. Make sure the oil is hot before you pour in the egg. This helps ensure that the egg doesn’t stick to the bottom of the pan, and yields super crispy edges. Be careful and watch out for hot oil splatters! This recipe is going to leave some tiny oil splatters on your stovetop. You’ll want to step away after you pour in the egg to avoid getting splattered yourself. A note on basting the egg white with oil: Most olive oil fried egg recipes suggest basting the egg white (not the yolk) with the hot olive oil while it cooks. You can do this by tilting the pan and scooping up some of the hot oil with a spoon. However, I can’t do this without burning my hand with oil splatters! My eggs turn out great without basting, so I didn’t include this in my recipe. If you want more firm yolks: For medium eggs, just cook the egg for 30 to 60 more seconds. If you want more firm yolks than that, you can cover the egg for 30 seconds or longer while it cooks. Repeat with additional eggs. You can continue frying eggs in the same skillet. Just add another drizzle of olive oil before each egg. You might need to dial down the heat as time goes on (if you catch the faintest whiff of smoke, it’s too hot). Season as desired. These fried eggs are basically perfect right out of the skillet, but I love to sprinkle them with a little flaky sea salt and freshly ground black pepper. Serve them with a knife and a fork to cut through their crispy undersides!"

# Insert document
x = coll.insert_one(data).inserted_id
data.clear()

data["Name"] = "Brownies"
data["Ingredients"] = ["Sugar", "Flour", "Cocoa Powder", "Powdered Sugar", "Dark Chocolate Chips", "Sea Salt", "Eggs", "Canola Oil", "Vanilla"]
data["Cook_Time"] = "45"
data["Tags"] = ["Vegetarian", "Dessert", "Baked Good", "Oven", "Bakeware"]
data["Servings"] = "16"
data["Recipe"] = "1. Preheat the oven to 325°F.\n2. Lightly spray an 8x8 baking dish with cooking spray and line with parchment paper.\n3. Spray the parchment paper.\n4. In a medium bowl, combine sugar, flour, cocoa powder, powdered sugar, chocolate chips, and seasalt.\n5. In a large bowl, whisk together eggs, oil, water, and vanilla. \n6. Sprinkle the dry mix over the wet mix and stir until combined.\n7. Pour batter into the prepared pan.\n8. When the oven is ready, put the pan into the oven.\n9. Cook for 40 to 48 minutes, or until the toothpick comes out with only a few crumbs attached. \n10. Let the brownies cool completely before you slice." 

# Insert document
x = coll.insert_one(data).inserted_id
data.clear()

# Wait till enter
text = input("Press enter to initiate query")

# Test Query
mycoll = db["Ingredients"]
myquery = { "Name": "Fried Egg" }
mydoc = mycoll.find(myquery)
for x in mydoc:
	print (x)


# Create Types collection
call = db.create_collection("Types")
# Create document
data = dict()
