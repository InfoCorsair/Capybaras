Hey Team!
I found this on mongodb.com, it is a guide to mongo import:
https://www.mongodb.com/developer/products/mongodb/mongoimport-guide/
From Anna

1. Files in the Mongo direcory:
  
  * better_ingredients.csv
    - This file contains all of the available ingredients
      by ingredient number. It also ties the measurement method
      used for each ingredient (Weight, Amount, etc.)
    - Author: Jackson Ornoff

  * pound_conversion.py
    - This Python code translates a quantity either from pounds to
      ounces or ounces to pounds. 
        + To translate ounces to pounds, give "__ oz" as input
	+ To translate pounds to ounces, give "__ lb" as input
    - Author: Jesse Johnsen

  * database.py
    - This Python code initializes the MongoDB and inserts a few
      default recipes into the database
    - It is imperative to run this code prior to running anything
      that queries the database
    - Author: Jackson Ornoff

  * insert_recipe.py
    - This Python code outlines the process for how to insert a
      recipe into the MongoDB while it is running.
    - Author: Jackson Ornoff

  * requirements.txt
    - Not actually sure what this text file accomplishes
    - Author: Jackson Onoff

  * revised_tags.txt
    - This text file outlines all of the tag options that should
      be made available to the user to assign to a recipe on the
      website.
    - Author: Jesse Johnsen and Anna Fox

  * measurement.py
    - This Python script takes an ingredient name and returns the
      measurement type (Weight, Amount, or Volume).
    - Author: Jesse Johnsen

  * tsp_conversion.py
    - This Python code translates a quantity either from teaspoons
      to greater volume measurements or vice versa.
        + To translate tsp to greater, input "__ tsp"
        + To translate greater to tsp, input "__ cup/pint/etc."
    - Author: Anna Fox	
