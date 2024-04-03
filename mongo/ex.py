from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__, '/static')

myclient = MongoClient('localhost', 27017)

mydb = myclient["CapyCookin"]

mycol = mydb["Ingredients"]
#mycol.drop();
def add(name, ingred):
  mydict = {"name": name, "numIngredients": ingred}
  x = mycol.insert_one(mydict)

def getNames():
  b = mycol.find()
  n = []
  for f in b:
    n.append(f)
  return n;
"""
def delete():
  mycol.drop()
  mycol = mydb["Ingredients"]

def delete(mycol):
mycol.drop()
mycol = mydb["Ingredients"]
"""


@app.route("/")
def list():
  return render_template('recipe.html', names = getNames())

@app.route("/process_form", methods=["GET", "POST"])
def form():
  namea = request.form.get('name')
  inga = request.form.get('numIngredients')
  add(namea, inga);
  return redirect(url_for('show_form'))
@app.route("/form")

#def delete(mycol):
#mycol.drop()
#mycol = mydb["Ingredients"]

def show_form():
  return render_template("form.html", mycol=mycol)
#@app.route("/form/delete")
if __name__ == '__main__':
  app.run()

