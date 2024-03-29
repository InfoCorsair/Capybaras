
____________________________________________
sqlite3 recipe.db
.headers ON

____________________________________________
		Updating Database
____________________________________________

How To Run: python3 update_table.py

What it does:
   -  It can add new rows to the table.
   -  Alters the table.
   -  Updates column names in the table.
   - Updates information in the rows based off of other columns.

____________________________________________
		Table Schema
____________________________________________
Appliance (appliance string, id string);
	
Dietary(dietary string);

meal_types(mealtype string, recipe text);

Ingredients(string ingredient name, ingredient_number string);

Cook Time(recipe text, cook_time floating point);

Serving Size:  serving size amd and recipe 

