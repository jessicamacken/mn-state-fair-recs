# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'databaseMN'
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://new-admin:QHeDa0xIHy13tVuY@cluster0.x71ub.mongodb.net/databaseMN?retryWrites=true&w=majority'
mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/activities')
def activities():
    return render_template('activities_main.html')

@app.route('/activities/<acttype>')
def activities_type(acttype):
    thecollection = mongo.db.activities
    myactivities = list(thecollection.find({"type":acttype}))
    # print(myactivities)
    n = len(myactivities)
    # print(n)
    return render_template('activities_type.html', myactivities=myactivities, n=n, acttype=acttype)

@app.route('/food/<foodtype>')
def food_type(foodtype):
    thecollection = mongo.db.food
    myfood = list(thecollection.find({"type":foodtype}))
    # print(myfood)
    j = len(myfood)
    # print(n)
    return render_template('food_type.html', myfood=myfood, j=j)


@app.route('/food')
def food():
    return render_template('food_main.html')