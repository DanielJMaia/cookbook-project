import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

USER = os.getenv('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')

app.config["MONGO_DBNAME"] = 'milestone-project-cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-bgp7f.mongodb.net/milestone-project-cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template("index.html",
    categories=mongo.db.categories.find())
    
@app.route('/get_recipes')
def get_recipe():
    return render_template("recipes.html",
    recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
    recipes=mongo.db.recipes.find(),
    categories=mongo.db.categories.find(),
    difficulty=mongo.db.difficulty.find())
    
@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('/'))
    
# Test Page Route

@app.route('/testing')
def test():
    return render_template("testing.html",
    recipes=mongo.db.recipes.find())

if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)