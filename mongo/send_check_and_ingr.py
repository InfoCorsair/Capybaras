from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__, '/static')
myclient = MongoClient('localhost', 27017)
mydb = myclient["CapyCookin"]

@app.route('/')

def index():
#if request.method == 'POST':
#   print(request.form.getlist('check'))
# return 'Done'
  return render_template('ingredients.html')
@app.route("/ingredients", methods=["GET", "POST"])
def show(): 
  if request.method == 'POST':
    print(request.form.getlist('check'))
  return 'DONE'

if __name__ =='__main__':
  app.run()
