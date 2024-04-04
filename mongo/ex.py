from flask import Flask, render_template, request, redirect, url_for, jsonify, after_this_request
import json
import ejson
from pymongo import MongoClient

app = Flask(__name__, '/static')

myclient = MongoClient('localhost', 27017)

mydb = myclient["CapyCookin"]

mycol = mydb["Ingredients"]
#mycol.drop();
def add(name, ingred, serva, cooka, datea):
  mydict = {"name": name, "numIngredients": ingred, "numServings": serva, "cookTime": cooka, "date": datea}
  x = mycol.insert_one(mydict)

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


@app.route("/")
def list():
  return render_template('recipe.html', names = getNames())

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

# n = getNames()
  names = EJSON.seralize(mydb.mycol.find().toArray())
  print(names)
  return names
# res = jsonify({'requests':list(n)})
# return (res)
#  print(n)
# y = json.loads(n)
#jsonResp = {'Jack': 4091, 'sape': 4139}
#return jsonify([n.to_json() for a in n])
#return jsonify(n['name'])
# return y
if __name__ == '__main__':
  app.run()

