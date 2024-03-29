# REFERENCE: https://www.youtube.com/watch?v=FVVOaCOAMFU
from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		name = request.form['name']
		ingredients = request.form['ingredients']
		amounts = request.form['amounts']
		cook_time = request.form['cook_time']
		tags = request.form['tags']
		servings = request.form['servings']
		recipe = request.form['recipe']
		recipes.insert_one({'Name': name, 'Ingredients': ingredients, 'Amounts': amounts, 'Cook_Time': cook_time, 'Tags': tags, 'Servings': servings, 'Recipe': recipe})
		return redirect(url_for('index'))
	all_recipes = recipes.find()
	return render_template('../recipe/main.html', recipes=all_recipes)


# This is a mongodb database
db = client.flask_database
# This is a Recipes collection
recipes = db.Recipes

if __name__ == "__main__":
	app.run(debug=True)
