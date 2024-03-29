from flask import Flask, Response
import pymongo
import json
app = Flask(__name__)

try:
  mongo = pymongo.MongoClient(
    host = "localhost",
    port = 27017,
    serverSelectionTimeoutMS = 1000)
  db = mongo.company
  mongo.server_info() # Trigger exception if cannot connect
except:
  print("ERROR - Cannot connect")

@app.route("/users", methods=["POST"])
def create_user():
  try:
    user = {"name":"A", "lastname":"AA"}
    dbResponse = db.users.insert_one(user)
    print(dbResponse.inserted_id)
    return Response(
      response = {"message":"user created", "id":f"{dbResponse.inserted_id}"},
      status=200,
      mimetype="application/json")
  except Exception as ex:
    print("***\n", ex, "\n***\n")
    
