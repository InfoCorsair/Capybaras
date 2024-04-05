from flask import Flask, render_template, request, redirect, url_for, jsonify, after_this_request, send_file
import json
from pymongo import MongoClient
import os

app = Flask(__name__, '/static')

myclient = MongoClient('localhost', 27017)

mydb = myclient["CapyCookin"]

mycol = mydb["Ingredients"]
#mycol.drop();

#adapted from ex.py

def add(name, ingred, serva, cooka, datea):
  mydict = {"name": name, "numIngredients": ingred, "numServings": serva, "cookTime": cooka, "date": datea}
  x = mycol.insert_one(mydict)
def flatten(x):
  oldid = x['_id']
  x['_id'] = str(oldid)
  return x

def getNames():
  b = mycol.find()
  n = []
  for f in b:
    n.append(f)
  return n;
#i"""
#def delete():
#  mycol.drop()
#  mycol = mydb["Ingredients"]

#def delete(mycol):
#mycol.drop()
#mycol = mydb["Ingredients"]
#"""


@app.route("/recipes")
def recipes():
  return render_template('recipe.html', names = getNames())
@app.route("/recipe_template")
def recipe_template():
  return render_template('recipe_template.html')
@app.route("/process_form", methods=["GET", "POST"])
def form():
  namea = request.form.get('name')
  inga = request.form.get('numIngredients')
  serva = request.form.get('numServings')
  cooka = request.form.get('cookTime')
  datea = request.form.get('date')
  add(namea, inga, serva, cooka, datea);
  return redirect(url_for('show_form'))
@app.route("/form")

#def delete(mycol):
#mycol.drop()
#mycol = mydb["Ingredients"]

def show_form():
  return render_template("form.html", mycol=mycol)
#@app.route("/form/delete")
@app.route('/getData', methods=["GET"])
def getData():
  def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

  n = list(map(flatten, getNames()))

#names = EJSON.seralize(mydb.mycol.find().toArray())
  print(n)
  return n
# res = jsonify({'requests':list(n)})
# return (res)
#  print(n)
# y = json.loads(n)
#jsonResp = {'Jack': 4091, 'sape': 4139}
#return jsonify([n.to_json() for a in n])
#return jsonify(n['name'])
# return y

#adapted from send_check_and_ingr.py

@app.route("/tags")
def tags():
#return redirect(url_for('ingredient_form'))
  return render_template('ingredients.html')

@app.route("/ingredients", methods=["GET", "POST"])
def ingredients(): 
  if request.method == 'POST':
    print(request.form.getlist('check'))
  return 'DONE'

#main page

@app.route("/")
def front():
  return render_template('main.html')


#@app.route("/front")
#def front():
#  return render_template('main.html')

#adapted from export.py

collection = mydb["Recipe"]

# Function to retrieve recipe data from MongoDB
def get_recipes():
  recipes = list(collection.find())
  return recipes

# Function to generate LaTeX code for the recipes
def generate_latex(recipes):
  latex_code = """
\\documentclass{article}
\\begin{document}
"""

  for recipe in recipes:
        latex_code += "\\begin{center}\n"
        latex_code += f"\\section*{{{recipe['Name']}}}\n"
        latex_code += "\\end{center}\n"
        latex_code += "\\textbf{Ingredients:}\\newline\n"
        for i, ingredient in enumerate(recipe['Ingredients'], start=1):
            latex_code += f"{i}. {ingredient}\\newline\n"
        latex_code += "\\textbf{Cook Time:} " + recipe['Cook_Time'] + "\\newline\n"
        latex_code += "\\textbf{Servings:} " + recipe['Servings'] + "\\newline\n"
        latex_code += "\\textbf{Recipe:} " + recipe['Recipe'] + "\\newline\n"
        latex_code += "\n"

  latex_code += "\\end{document}"
  return latex_code

# Route to render the main page with recipes
@app.route("/getpages")
def getpages():
  recipes = get_recipes()
  return render_template("export.html", recipes=recipes)

# Route to export selected recipes to PDF
# Route to export selected recipes to PDF
@app.route("/export", methods=["POST"])
def export():
  selected_recipes = request.form.getlist('recipe')
  recipes = get_recipes()

  # Filter selected recipes
  selected_recipe_objects = []
  for recipe in recipes:
      if str(recipe['_id']) in selected_recipes:
          selected_recipe_objects.append(recipe)

  # Generate LaTeX code
  latex_code = generate_latex(selected_recipe_objects)

  # Write LaTeX code to a file
  filename = 'exported_recipes.tex'
  latex_file_path = os.path.join('latex', filename)
  os.makedirs(os.path.dirname(latex_file_path), exist_ok=True)
  with open(latex_file_path, 'w') as f:
      f.write(latex_code)

  # Convert LaTeX to PDF
  pdf_file_path = os.path.join('pdfs', 'exported_recipes.pdf')
  os.makedirs(os.path.dirname(pdf_file_path), exist_ok=True)
  os.system(f'pdflatex -output-directory=pdfs {latex_file_path}')

  # Open PDF in browser
  return send_file(pdf_file_path, as_attachment=False)


#RUN the program
if __name__ == '__main__':
  app.run()

