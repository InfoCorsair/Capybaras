from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

myclient = MongoClient('localhost', 27017)

mydb = myclient["CapyCookin"]
mycol = mydb["Ingredients"]

mydict = { "name": "Fried Egg", "Ingredients": ["Egg", "Oil"], "Amounts": ["1", "1"], "Cook_Time": "240"}

x = mycol.insert_one(mydict)
mydict = { "name": "Chicken", "Ingredients": ["Flour", "Chicken"], "Amounts": ["1", "1"], "Cook_Time": "240"}

x = mycol.insert_one(mydict)

b = mycol.find()
f = b.next();
names = []
names.append(f['name'])

f = b.next();
names.append(f['name'])
@app.route("/")
def list():
  return render_template('ex.html', names = names)
if __name__ == '__main__':
  app.run()

