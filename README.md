<h1 align="center">
  <a href="http://gf-cookbook.herokuapp.com/" target="_blank"><img src="https://i.imgur.com/4M00e3p.png" alt="Home Page"/></a>
</h1>

### Celiac Haven 
This project is my submission for my Data Centric milestone project as part of my training to become a Full Stack Web Developer. The purpose is to apply skills learnt during the Python and Data Centric Development modules. This website uses what I learnt, specifically CRUD operations with the MongoDB database, and rendering data with Jinja and communicating with the backend using flask. The course is provided by the Code Institute. 

As someone with Celiac's disease it can be very challenging to adapt to the Gluten Free diet. Going out for meals becomes a lot more restrictive, and cooking at home can become extremely monotonous if you're always making the same three things. Finding recipes online becomes disheartening once you realize that nearly all of them require multiple ingredients to be replaced. Celiac Haven was created to approach that problem. It's a collection of gluten free, yet delicious, recipes that people everywhere can contribute to. The only gluten free replacements are ingredients that all celiacs already have at home!

---


## UX
### User Stories 
Users of the site are able to:
- Use the search bar to search for specific recipes or type in keywords such as "pasta" to bring up a list, or give an error if there's no results returned. This allows users to easily find recipes they want when they have something in mind without having to access a specific category and browse the lists.
- Access a list of recipe categories to narrow down their search using the navigation menu or by browsing the home screen. This is useful for users who want to cook a specific meal i.e. dinner and want to easily access all the meals they can cook.
- View recipes of a single category including a brief description. Building upon the previous user story, this allows the user to view specific recipes that might appeal to them.
- Access a recipe editing page from the list of recipes and recipe page itself. This is useful if a recipe changes, was incorrectly uploaded in the first place or the user wants to add some tips they've picked up.
- Delete a recipe from the recipe editing page. This was initially an option alongside the "edit" button on the recipe page, but it felt important to make deleting less easy to accidentally press.
- Create a new recipe and add it to a specific category.
- Preview the image they want to add by adding the link and having show them. This allows the user to make sure that it's a working URL, as well as preview the image to make sure they're happy with it.  
- Navigate the page without ever having to use page navigation offered by the browser. The navbar on the right is permanent and the back arrow appears on all pages except the home page.
- Navigate the website on any device they want. It's fully functional on mobile, tablets and desktops. If a user is out and wants to access their recipes on their phone it's easy, and if they want to upload a new one they learn on the road it's not more difficult on mobile devices. 

### Colour Scheme
I wanted to take a very neutral approach to this website. It's not meant to distract the user from the any of the images of the food, nor detract from them.
- The primary background color was ![#faebd7](https://placehold.it/15/faebd7/faebd7) `#faebd7`. I found that this was very easy on the eyes, and reminded me of baking and coffee shops.
- The secondary color was actually the default materialize turquoise colour found on buttons and inputs. This was originally just a placeholder colour but as the website came together I began to really like it, and other colours weren't doing it for me so I decided to stick to it. 
### Wireframes
Wireframes were done using Paint3D since I don't currently own any professional wireframe software. They can be found [here](https://github.com/DanielJMaia/cookbook-project/issues/1)

### General Design Principles
The idea was to make a very minimalistic but functional website that allowed users to CREATE, READ, UPDATE and DELETE recipes. It was important that at all times the user could jump to any category of recipe which is why the navigation menu displays the different categories available. I chose to stick with the hamburger icon even on large screens since it looked and felt very sleek, and I didn't want to take away from the main content on the page.

It was also important that users never need to navigate the page using the browser navigation which led to the addition of a back arrow on the website.

---


## Features
### Existing Features
- Site Wide Features
    - Site title which links to the home page. This is common practice across all websites.   
    - Responsive Navbar: This extremely minimalistic navbar displays when the user presses the hamburger icon. It links to
        - Home page where the user can view all the recipe categories.
        - The recipe creation page which allows users to submit a new recipe.
        - All the available categories so that the user can go to a specific category no matter what page they're on.
        - The search field that can be used to search for specific recipes, or simply type in keywords.
    - A footer with information about the author of the website and the technologies used, as well as links to the authors' GitHub and LinkedIN pages. 
The navigation bar is scalable, for it uses a for loop to load the different categories. This was chosen over hard coding the 6 categories so a customer with very limited knowledge of coding can simply add a new category to the list in the database, add a picture URL, and everything on the website automatically updates to reflect this. This scalable approach was used in the edit recipe and add recipe pages for the categories dropdown for the same reason.
- The Home Page 
    - It has a large banner image with a slogan in the middle of it. This is meant to be eye catching and appealing to look at, and makes it immediately clear what the exact purpose of the website is.
    - A list of category cards including an image:
        - Breakfast
        - Easy Meals
        - Smoothies & Shakes
        - Fancy Dishes on a Budget
        - No Oven Needed
        - Deserts
- Selected Category Page
    - A header informing the user which category they selected.
    - A grid of cards displaying different recipes in the selected category.
        - Each card has an image of the recipe, its title, a brief description of the recipe and an edit button.
    - A back arrow button.
- Specific Recipe Page
    - The recipe title and description.
    - The image showing the dish.
        - A box in the top left of the image which contains the recipe difficulty, preparation duration and the category.
    - Ingredients - To display the ingredients array items, a for loop is used.
    - Gluten Free Replacements when needed
    - Allergens
    - Cooking Instructions - A similar for loop is used here as with the ingredients to display all the items in the method array.
    - Additional Tips
    - Edit recipe button
- Add submission page
It was important to me that the user couldn't submit this form by pressing enter, or if required fields weren't filled out. To ensure that enter didn't submit the form, the enter button was disabled unless the user was typing in the search bar or in the textareas (new lines are important in the text area, they each represent an array item). The required keyword was added to all input fields except for tips, as I didn't deem that very important.
This page contains a form that the user can use to create a new recipe. The inputs are as follows:
    - Recipe Title
    - Description
    - Category selection - This is a dropdown which allows the user to select one of the 6 categories available. Like mentioned previously, instead of hard-coding the list items a for loop was created for future scalability.
    - Difficulty selection - This is also a dropdown that uses a for loop, although it's much less likely that the owner of the website will need to add more categories in addition to the existing three. 
    - Ingredients - This is a text box which allows the user to press enter for each new ingredient and in the database it stores each new line as an array item.
    - Duration
    - Method - This is also a text box, the same approach was taken as with the ingredients page.
    - Gluten Free Replacement Ingredients
    - Extra Tips
    - Allergens
    - Image URL Input
        - The placeholder image automatically updates when the user inserts a URL as a preview. If no image is displayed, an image alt tag informs the user no image was found.
    - Submit button which submits the form and redirects the user to the recipe page for the recipe they just created. 
- Edit Recipe Page
This is very similar to the submission page, except all the fields are already filled out with the values for the recipes.

The edit recipe page contains an additional delete button that removes the recipe and redirects the user to the home page. This delete button displays a custom popup which was created using SweetAlert. Because I wanted to ensure that the user clicked delete and then confirmed they wanted to delete the page before the form was submitted, I couldn't wire up the form submission to the delete button in the way I'd done with the rest of the form submission buttons. Instead, clicking the delete button ONLY runs the JavaScript function for the alert, and submitting the form is handled using the form.submit() method in Javascript when the user presses yes after the warning message is displayed.
### To-Do List
- User profile
    - If a user can tie entries to their profile, it'd allow for extra security. They'd only be able to delete and edit recipes they've created.
- Additional Filtering
    - Potential options include filtering based of difficulty, allergens etc.

---


## Technologies used
### Languages
- HTML - The language used to create the structure of the pages.
- CSS - The language used to style pages.
- JavaScript - The language used to create dynamic content such as the delete button popup.
- Python - The language used to handle everything relating to the backend, including Jinja routing and database access using PyMongo.
### Additional Technologies
This includes frameworks, libraries and services.
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - Web Template engine for Python.
- [Flask](http://flask.palletsprojects.com/en/1.1.x/) - Python Micro Framework that allowed for routing between my various pages.


- [MongoDB](https://www.mongodb.com) - The database service where all text data for this project was hosted. MongoDB is a cross-platform document-oriented database program classified as a NoSQL database program.
- [Heroku](https://heroku.com/) - Cloud platform service which was used to host the final version of the website.
- [Imgur](https://imgur.com/) - Image hosting service.


- [JQuery](https://jquery.com/) - JavaScript library used to initialize Materialize elements and the image preview section of edit_recipe.html and create_recipe.html.
- [SweetAlert](https://sweetalert.js.org/guides/) - This was used to create the custom delete alert when a user tried to delete a recipe. 
- [MaterializeCSS](https://materializecss.com/) - Based on material design, MaterializeCSS was used for the design of this website. It handles responsive web design and provides classes for a large quantity of elements.
- [GitHub](https://github.com/) - GitHub provides a remote repository with git control.
- [GitPod](https://gitpod.io) - An online cloud-based IDE built with deep GitHub integration, I switched to this after deep frustrations using AWS Cloud9 near the end of my project. The environment sharing feature was particularly useful, as well as the built-in bash terminal.
- AWS Cloud9 - An Amazon cloud based IDE with an integrated bash terminal. I switched from this because it crashes all the time on Firefox Developer Edition, signs you out randomly regardless of whether you're in the middle up typing a line of code or currently pushing something to GitHub or flask, which requires you to go through the tedious login process, and just generally had a series of migraine inducing issues.

---


## Testing
Testing was done in the Chrome Browser, and due to time constraints there was no automatic unit-testing. 
### Debugging in Chrome Dev Tools
The Chrome Dev Tools were the single most useful debugging resource throughout the creation of this website. The most important features were
- Console logging. This allowed me to view the value of variables and data from the DB in the console. If incorrect values, or no values, were being returned, I could pinpoint the exact issue.
- Network logs were useful when I was creating all my routes. They allowed me to check that all my external files were loading.
- Responsive Layout. This project was created using a mobile first mentality. Viewing the page on a large amount of sizes and screen ratio ensured that at no point the project wasn't accessible on all devices.
#### Other Browsers Used For Testing
I do not have any devices that can run Safari. In a professional environment I assume I'd have colleagues who own Macs. If not, I'd have to run Macintosh (or perhaps just Safari) in a virtual environment on Windows or Linux.
- Firefox Developer Edition
- Microsoft Edge

### Manual Testing
On all browsers:
- The mobile version scales as intended, and provides 100% of the functionality of the desktop one.
- Each navigation item was pressed from the index, category, recipe, edit recipe and add recipe pages. This includes the title which redirects to the home page. 
- The searchbar was used on each of these pages.
- An incorrect entry was typed in i.e. "asdasd" to make sure that the error message appeared. 
- Partial words were types in to make sure they still returned results. 
    - chicken - This returns all the recipes with chicken in their title.
    - thie - This returns the banana and blueberry smoothie.
    - OATS - This returns the berries, oats and yoghurt cereal recipe. 
    - a - This returns all recipes with the letter a in their title.
- The view recipe page displays the ingredients and method arrays on new lines for each array item.
- On the add recipe page, I ensured that a recipe couldn't be submitted without the required field.
- An error message correctly displays if there wasn't a picture associated with the URL the user typed in for the recipe image.
- The image preview displays instantly  in the image preview box when the user types in a valid URL.
- Deleting a recipe actually deletes it, and adding one adds it to the correct category.
- The edit recipe button displays the edit page with each input autofilled with the correct values.
- The delete button properly displays a functioning alert.
- Each category displays the appropriate recipes, and clicking a recipe displays the appropriate page.
- The social media links open in a new tab and direct to the correct github and LinkedIN profiles

### Validators
HTML, CSS, JS and Python validators were used to ensure that the code was syntactically correct. For CSS, everything came back 100% correct. However, for the HTML files that wasn't the case, and this is due to Jinja. The W3 Validator returned all instances of {{}} as errors. The solution was to simply go through each error carefully and confirm that each one was directly related to instances of Jinja templating. I checked that my JS code was syntactically correct using [esprima](https://esprima.org/demo/validate.html) by pasting the contents of one JS file at a time.
- HTML Validator - [W3] (https://validator.w3.org/) - This only displayed errors with Jinja, and by going through the code carefully I ensured there were no other syntax mistakes.
- CSS Validator - [W3] (https://jigsaw.w3.org/css-validator/) - No syntax errors were detected.
- Python Validator - [extendsclass.com](https://extendsclass.com/python-tester.html) - No syntax errors were detected. I also was able to run the code successfully without any console errors.
- JS Validator - [JSLint](https://www.jslint.com/) - No syntax errors were  detected.

---


## Deployment
### Local Setup
Ensure that the following is installed on your system
- Python3
- PIP3
- PyMongo
- Flask
- Git

The steps to deploying this website on your system are as follows:
1. Download this repository from GitHub, or type the command
```
git clone https://github.com/DanielJMaia/cookbook-project.git
```
2. Add the following environment variables: IP - 0.0.0.0, PORT - 5000 and MONGO_URI you'll get in a moment. You can create these in a .env file, or if you're using GitPod simply add them to your environment variables in the dashboard.
3. Add a requirement.txt file by running the following command 
```
pip3 freeze –local > requirements.txt
```
4. Create a database in MongoDB called milestone-project-cookbook
5. Add the following collections: categories, difficulty, recipes.
6. Populate the difficulty collection with the following documents: 
```
_id: <ObjectID>
difficulty: "Easy"

_id: <ObjectID>
difficulty: "Medium"

_id: <ObjectID>
difficulty: "Hard"
```
7. Populate the categories collection with the following documents:
```
_id: <ObjectID>
title: "Breakfast"
url: "https://i.imgur.com/bnodfjl.jpg"

title: "Easy Meals"
url: "https://i.imgur.com/N1MmIXr.jpg"

title: "Smoothies & Shakes"
url: "https://i.imgur.com/XdGfkfs.jpg"

title: "Fancy Dishes On A Budget"
url: "https://i.imgur.com/h4Yvo9d.jpg"

title: "No Oven Needed"
url: "https://i.imgur.com/JX323Oa.jpg"

title: "Deserts"
url: "https://i.imgur.com/aP70sED.jpgsd"

```

Images of the three catalogues can be found [here](https://github.com/DanielJMaia/cookbook-project/issues/2)

The recipes collection can be populated using the website.

8. In MongoDB find the connect button for the Cluster and press connect  your application. Select Python from the list of Drivers and your current version of Python. Copy the connection string and use that as your MONGO_URI environment variable. Remember to replace "root":"password" with your MongoDB user username and password. 
9. In the bash terminal type python3 app.py to run the application, and preview the running application in a browser or IDE preview window. 

### Deployment
1. Create a Procfile by typing 
```
echo web: python run.py > Procfile 
```
You must ensure that it's pointing to the correct file, in this case the Procfile says "web: python3 app.py"
2. Create an account for the web service hosting platform Heroku. 
3. Install Heroku by typing in the terminal
```
npm install -g heroku
```
4. Type heroku in the terminal to ensure it's installed correctly, and if so type
```
heroku login
```
5. Create a new heroku project and set the config variables in settings > reveal config vars. They are the same three as set earlier, IP, PORT and MONGO_URI.
6. After ensuring that you have the requirements.txt and Procfile files up to date, add the project to git by typing 
```
git add .
``` 
in the terminal. 
7. Finally, push the project to Heroku by typing in the terminal
```
git push heroku master
```

---


## Bugs, Problems and Difficulties
As is the case with all software projects, there were a series of bugs and issues that I had to overcome. First of all, Materialize styles are very difficult to override. I found that when the materialize defaults weren't cutting it and I wanted to use my own custom CSS, it was sometimes necessary to use !important which I really don't like doing. 

When I initially added the delete button I was using the window alert method. This was extremely rough looking and I wanted to find something else, which led me to SweetAlert. However, after creating the custom warning message I found that clicking the delete button would display the message and then instantly delete the recipe regardless of what the user clicked. This makes sense but it required a clever workaround which was suggested by the tutor Kevin, which was to tie the form submission to the if statement in JS instead of the usual approach taken with my other buttons. 

Another issue I had was that pointer objects such as my categories variable can't looped through more than once per page. I didn't know this. My base.html file loops through the categories to populate the navigation bar. This categories variable is then also used in specific pages such as index.html to create all the categories cards, and edit/create recipe pages to populate the dropdowns. As a result of only being able to loop through the pointer object once, those pages weren't loading those elements. The home page wasn't displaying categories and the edit/create recipe pages dropdowns weren't working. That is to say, all instances of the variable except the very first time it's looped through weren't working because they were trying to start their loop at the end of the collection. The initial solution was simply to create another, identical variable i.e.
```
global_category=mongo.db.categories.find(),
local_category=mongo.db.categories.find())
```
However, this is bad practice and after my mentor meeting I was told I should really try to figure it out. The obvious take the easy way out, in this case to just hard code the 6 navigation bar items. That would have taken 5 minutes and I doubt it'd have affected the overall quality of the page one bit, but after spending far more time than I'd like to admit trying to find a solution I wasn't ready to give up. The final solution was to change the variable from a pointer object to a list object by simply typing
```
local_category=list(mongo.db.categories.find()))
```
I'm glad I spend the extra time on this instead of taking the easy route, I doubt I'll ever forget this issue.

This was my first time working with environment variables, and because of this I wasn't really sure how they worked. I understood the principle of them, but in practice I wasn't up to scratch. As such, when I went to host my project on Heroku I forgot to set the hidden variables there and it simply didn't work. After a very useful chat with Xavier, I now understand them quite nicely. 
Another issue arose when I was hosting my project, and that was that my Procile was incorrect. For some reason, when I created the procfile it didn't say web: python3 app.py, it was another nonexistent python file. This wasn't immediately obvious to me and caused a brief moment of frustration.


## Credits
### Content
Some recipes were taken from [Gousto](https://www.gousto.co.uk/) recipe pamphlets, and the chocolate cake was [Jamie Oliver's Gluten Free Chocolate Cake](https://www.jamieoliver.com/recipes/chocolate-recipes/gluten-free-chocolate-cake/). Some others were personal recipes, such as the smoothie.
### Media
Images retrieved from [Pexels.com](https://www.pexels.com/) unless states otherwise.

Smoothie Category Image found [here](https://beamingbaker.com/triple-berry-smoothie-5-ingredient-paleo-vegan-gluten-free-dairy-free/).

Quote Background Image found [here](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/).

Spicy Chicken Rice Recipe Image found [here](https://www.tablespoon.com/recipes/mexican-chicken-and-rice-skillet/eda0017c-42a8-404b-bc47-22eebcd0586c).

Chorizo Risotto Image found [here](https://www.taste.com.au/recipes/chorizo-pasta/6871b2f9-5686-4354-974d-d7aca8e94388).

Sticky soy chicken recipe image found [here](https://www.bbc.co.uk/food/recipes/asian-style_sticky_23400).

Placeholder upload image found [here](https://woodworkersbelfast.com/placeholder-png/).

My Imgur gallery is currently private and therefore can only be viewed by me.


### Acknowledgements

 I'd like to thank my mentor [Antonija](https://github.com/tonkec) for giving me some helpful advice and sending me some extremely useful reading material during meetings throughout the project. I'd also like to thank the tutor support team, notably [Xavier](https://www.linkedin.com/in/dev-xavier-astor/?originalSubdomain=ie), [Tim](https://github.com/TravelTimN) and [Kevin](https://www.linkedin.com/in/kevinloughrey/?originalSubdomain=ie), for being incredibly helpful when I encountered difficulties. I'd especially like to thank [Xavier](https://www.linkedin.com/in/dev-xavier-astor/?originalSubdomain=ie) for having a meeting with me to help me understand routes in python, then helping me switch over to GitPod and also helping me with putting my project up on Heroku, all in the same day!