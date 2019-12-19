import os
from os import path
if path.exists("env.py"):
   import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone-project-cookbook'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', "Env value not loaded")

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template("index.html",
                            local_category=list(mongo.db.categories.find()))
    
@app.route('/get_recipes/<recipe_category>')
def get_recipes(recipe_category):
    return render_template("recipes.html",
                            local_category=mongo.db.categories.find(),
                            current_category=recipe_category,
                            recipes=mongo.db.recipes.find({"category": recipe_category}))
    
@app.route('/search_recipes/', methods=["GET", "POST"])
def search_recipes():
    if request.method == "POST":
        post_request = request.form.get('searchbar_input')
        print(post_request)
    return render_template("search_recipe.html",
                            local_category=mongo.db.categories.find(), 
                            recipes=mongo.db.recipes.find({"title" : {"$regex": post_request, "$options": "i"}}),
                            recipe_count=mongo.db.recipes.find({"title" : {"$regex": post_request, "$options": "i"}}).count())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
                            local_category=list(mongo.db.categories.find()),
                            difficulty=mongo.db.difficulty.find())
    
@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    method_string = request.form.get('method')
    method_array = [m for m in method_string.split("\n") if m]
    ingredients_string = request.form.get('ingredients')
    ingredients_array = [i for i in ingredients_string.split("\n") if i]
    data = {
        'title' : request.form.get('title'),
        'category' : request.form.get('category'),
        'gf_ingredient' : request.form.get('gf_ingredient'),
        'prep_duration' : request.form.get('prep_duration'),
        'difficulty' : request.form.get('difficulty'),
        'method' : method_array,
        'ingredients' : ingredients_array,
        'description' : request.form.get('description'),
        'tips' : request.form.get('tips'),
        'allergens'  : request.form.get('allergens'),
        'url' : request.form.get('url')
    }
    _id = recipes.insert_one(data)
    return render_template('view_recipe.html',
                            local_category=mongo.db.categories.find(),
                            recipes = mongo.db.recipes.find({"_id": _id.inserted_id}))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    difficulty = mongo.db.difficulty.find()
    category_list = [category for category in categories]
    return render_template('edit_recipe.html', 
                            recipe=recipe, local_category=category_list,
                            difficulty=difficulty)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    method_string = request.form.get('method')
    method_array = [m for m in method_string.split("\n") if m]
    ingredients_string = request.form.get('ingredients')
    ingredients_array = [i for i in ingredients_string.split("\n") if i]
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'title' : request.form.get('title'),
        'category' : request.form.get('category'),
        'gf_ingredient' : request.form.get('gf_ingredient'),
        'prep_duration' : request.form.get('prep_duration'),
        'difficulty' : request.form.get('difficulty'),
        'method' : method_array,
        'ingredients' : ingredients_array,
        'description' : request.form.get('description'),
        'tips' : request.form.get('tips'),
        'allergens'  : request.form.get('allergens'),
        'url' : request.form.get('url')
    })
    return render_template('view_recipe.html',
                            recipes = mongo.db.recipes.find({"_id": ObjectId(recipe_id)}), 
                            local_category=mongo.db.categories.find())
    
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    return render_template('view_recipe.html',
                            recipes = mongo.db.recipes.find({"_id": ObjectId(recipe_id)}),
                            local_category=mongo.db.categories.find())
  
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('home'))

if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=False)