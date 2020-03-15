import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
#import bson library because mongoDB uses JSON like data format
from bson.objectid import ObjectId 

#configuration settings for our Flask application- database name and URL linking to that database
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root1:r00tUser@myfirstcluster-1osp5.mongodb.net/task_manager?retryWrites=true&w=majority'

#an instance of PyMongo using the constructor method
mongo = PyMongo(app)

#a function with a decorator that includes a route to that function
#default root below
@app.route('/')
#remember routing is a strin that, when we attach to a URL, will redirect to a particular function in our Flask application
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)