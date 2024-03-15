import pymongo
from flask import Flask, render_template, request, redirect, flash
from bson.objectid import ObjectId

app = Flask('contactmanager')
app.secret_key='a1h2k3jh145h4J*7^9#'

connectionstring = open("connectionstring.txt", "r")
cluster = pymongo.MongoClient(connectionstring.read().strip())
database = cluster.contactmanager
collection = database.contacts

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="GET":
        contacts=list(collection.find({}))
        # print(contacts)
        return render_template('index.html', contacts = contacts)
    else:
        record = {}
        record["name"]=request.form["name"]
        record["phone"]=request.form["phone"]
        collection.insert_one(record)
        flash('Added Contact Successfully!','success')
        return redirect('/')
    
@app.route('/deletecontact')
def delete():
    # print("deleting contact")
    contactid=request.args["contactid"]
    # print(contactid)
    # print(request.args)
    collection.delete_one({"_id":ObjectId(contactid)})
    flash('Deleted Contact Successfully!','danger')
    return redirect('/')

app.run (debug = True)
