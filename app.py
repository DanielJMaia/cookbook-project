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
    
@app.route('/get_recipes/<recipe_category>')
def get_recipes(recipe_category):
    return render_template("recipes.html",
    categories=mongo.db.categories.find(),
    recipes=mongo.db.recipes.find({"category": recipe_category}))
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
    categories=mongo.db.categories.find(),
    difficulty=mongo.db.difficulty.find())
    
@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    _categories = mongo.db.categories.find()
    _difficulty = mongo.db.difficulty.find()
    category_list = [category for category in _categories]
    return render_template('edit_recipe.html', recipe=_recipe, categories=category_list, difficulty=_difficulty)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'title' : request.form.get('title'),
        'category' : request.form.get('category'),
        'gf_ingredient' : request.form.get('gf_ingredient'),
        'prep_duration' : request.form.get('prep_duration'),
        'difficulty' : request.form.get('difficulty'),
        'method' : request.form.get('method'),
        'ingredients' : request.form.get('ingredients'),
        'description' : request.form.get('description'),
        'tips' : request.form.get('tips')
    })
    return redirect(url_for('home'))
    
    
# Test Page Route

@app.route('/testing')
def test():
    return render_template("testing.html",
    recipes=mongo.db.recipes.find())

if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)