from flask import Flask, render_template, request, send_file
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB
mongo_url = "mongodb://localhost:27017"
mongo_client = MongoClient(mongo_url)
db = mongo_client["CapyCookin"]
collection = db["Recipe"]

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
@app.route("/")
def home():
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

if __name__ == "__main__":
    app.run(debug=True)

