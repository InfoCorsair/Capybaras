from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
myclient = MongoClient('localhost', 27017)
mydb = myclient["CapyCookin"]

@app.route('/', methods=['GET','POST'])

def index():
  if request.method == 'POST':
    print(request.form.getlist('check'))
  return 'Done'
@app.route("/ingredient")
def show(): 
  return render_template('ingredients.html')

if __name__ =='__main__':
  app.run()
