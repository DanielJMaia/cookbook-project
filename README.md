TO DO LIST: Python and JS Validation?

Smoothie Category Image: https://beamingbaker.com/triple-berry-smoothie-5-ingredient-paleo-vegan-gluten-free-dairy-free/
Quote Background Image : https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/
Spicy Chicken Rice Recipe Image: https://www.tablespoon.com/recipes/mexican-chicken-and-rice-skillet/eda0017c-42a8-404b-bc47-22eebcd0586c
Chorizo Image - https://www.taste.com.au/recipes/chorizo-pasta/6871b2f9-5686-4354-974d-d7aca8e94388
Sticky soy chicken recipe image - https://www.bbc.co.uk/food/recipes/asian-style_sticky_23400
Placeholder Image location - https://woodworkersbelfast.com/placeholder-png/
I got a LOT of my images from this website - https://www.pexels.com/
library used: sweetalert: https://sweetalert.js.org/guides/

Errors Encountered: Clashing between Materialize styles and my own. 
Initializing materialize elements wasn't always working.
The for loop that populates the navbar doesn't function at the same time as the for loop that populates index.html. No idea why.
The categories dropdown on the add recipe page also breaks when the for loop gets introduced to the base html page. 
How to do environment variables?
Can't use jinja in JS, so I had to improvise for the delete button which uses sweetalert


!!!!! SOLUTION TO DOUBLE VARIABLE ISSUE
"In relation to the two variables and one collection, the issue has to do with the cursor object which is the way your app takes the information from the database. in short, it can only be done one which is why using the same for both is breaking it."

### Celiac Haven - As someone with Celiac's disease it can be very challenging to adapt to the Gluten Free diet. Going out for meals becomes a lot more restritive, and cooking at home can become extremely monotonous. Finding recipes online becomes disheartening once you realise that nearly all of them require multiple ingredients to be replaced. Celiac Haven was created to approach that problem. It's a collection of entirely gluten free, yet delicious, recipes that people everywhere can contriubute to.

---

## UX
### User Stories 
Users of the site are able to:
- Access a list of recipe categories to narrow down their search through the navigation menu or on the home screen. This is useful for users who want to cook a specific meal i.e. dinner and want to easily access all the meals they can cook.
- View recipes of a single category including a brief description. Building upon the previous user story, this allows the user to view specific recipes that might appeal to them.
- Edit a recipe from the list of recipes, and edit/delete it from the recipe page itself. This is useful if a recipe changes, was incorrectly uploaded in the first place or the user wants to add some tips they've picked up.
- Create a new recipe and add it to a specific category.
- Preview the image they want to add by adding the link and having show them. This allows the user to make sure that it's a working URL, as well as preview the image to make sure they're happy with it.  
- Navigate the page without ever having to use page navigation offered by the browser. The navbar on the right is permanant and the back arrow appears on all pages except the home page.
- Navigate the website on any device they want. It's fully functional on mobile, tablets and desktops. If a user is out and wants to access their recipes on their phone it's easy, and if they want to upload a new one they learn on the road it's not more difficult on mobile devices. 
- Use the search bar to search for specific recipes or type in keywords such as "pasta" to bring up a list, or give an error if there's no results returned. This allows users to easily find recipes they want when they have something in mind without having to access a speific category and browse the lists. 

### Colour Scheme
I wanted to take a very neutral approach to this website. It's not meant to distract the user from the any of the images of the food, nor detract from them.
- The primary background color was ![#faebd7](https://placehold.it/15/faebd7/faebd7) `#faebd7`. I found that this was very easy on the eyes, and reminded me of baking and coffee shops.
- The secondary color was actually the default materialize turquoise colour found on buttons and inputs. This was originally just a placeholder colour but as the website came together I began to really like it, and other colours weren't doing it for me so I decided to stick to it. 
### Wireframes
### General Design Principles
The idea was to make a very minimalistic but functional website that allowed users to CREATE, READ, UPDATE and DELETE recipes. It was important that at all times the user could jump to any category of recipe which is why the navigation menu displays the different categories available. I chose to stick with the hamburger icon even on large screens since it looked and felt very sleek, and I didn't want to take away from the main content on the page.

It was also important that users never need to navigate the page using the browser navigation which led to the addition of a back arrow on the website.

---

## Features
### Existing Features
- Site Wide Features
    - Responsive Navbar: This extremely minimalistic navbar displays when the user presses the hamburger icon. It links to
        - Home page
        - The recipe creation page 
        - All the available categories so that the user can go to a specific category no matter what page they're on.
    - The search field that the user can use to search specific recipes. 
    - A footer with information about the author of the website and the technologies used, as well as links to the authors GitHub and LinkedIN pages. 
- The navbar has a search field so that user can 
- The Home Page 
    - It has a large banner image with a slogan in the middle of it.
    - A list of category cards including an image:
        - Breakfast
        - Easy Meals
        - Smoothies & Shakes
        - Fancy Dishes on a Budget
        - No Oven Needed
        - Deserts
- Specific Category Page
    - A header informing the user which category they selected.
    - A grid of cards displaying different recipes in the selected category.
        - Each card has an image of the recipe, its title, a brief description of the recipe and an edit button.
    - A back arrow button.
- Specific Recipe Page
    - The recipe title and description.
    - The image showing the dish.
        - A card in the top left of the image which contains the recipe difficulty, preparation duration and the category.
    - Ingredients
    - Gluten Free Replacements when needed
    - Allergens
    - Cooking Instructions
    - Additional Tips
    - Edit recipe button
- Add a recipe page
This page contains a form that the user can use to create a new recipe. The inputs are as follows:
    - Recipe Title
    - Description
    - Category selection  
    - Difficulty selection
    - Ingredients 
    - Duration
    - Method
    - Gluten Free Replacement Ingredients
    - Extra Tips
    - Allergens
    - Image URL Input
        - The placeholder image automatically updates when the user inserts a URL as a preview. 
    - Submit button which redirects the user to the recipe page for the recipe they just created. 
- Edit Recipe Page
        - This is very similar to the submission page, except all the fields are already filled out with the values for the recipes.
        - An additional delete button that removes the recipe and redirects the user to the home page.
### Potential Features
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
- Python
### Additional Technologies
This includes frameworks, libraries and services.
- Backend Frameworks
    - Jinja - Web Template engine for Python.
    - Flask - Python Micro Framework that allowed for routing between my various pages.
- Database and Hosting Services
    - MongoDB - The database service where all text data for this project was hosted.
    - Heroku - Web Hosting service which was used to host the final version of the website
    - Imgur - Image hosting since MongoDB has DB size restrictions.
- Front end framework and libraries
    - JQuery - JavaScript framework used to initialize Materialize elements and the image preview section of edit_recipe.html and create_recipe.html.
    - SweetAlert - This was used to create the custom delete alert when a user tried to delete a recipe. 
- Front end styling frameworks
    - Materialize - This framework created by google was used for the design of this website. It handles responsive web design and provides classes for a large quantity of elements.
- Version Control
    - GitHub - Remote repository with git control
- IDE
    - GitPod - An online cloud-based IDE built with deep GitHub integration, I switched to this after deep frustrations using AWS Cloud9 near the end of my project. The environment sharing feature was particularly useful, as well as the built-in bash terminal.
    - AWS Cloud9 - An Amazon cloud based IDE with an integrated bash terminal. I switched from this because it crashes all the time on Firefox Developer Edition, signs you out randomly regardless of whether you're in the middle up typing a line of code or currently pushing something to GitHub or flask, which requires you to go through the tedious login process, and just generally had a serious of migrane inducing issues.

---

## Testing
Testing was done in the Chrome Browser, and due to time constraintss there was no automic unit-testing. 
### Chrome Dev Tools
The Chrome Dev Tools were the single most useful resource throughout the creation of this website. The most important features were
- Console logging. This allowed me to view the value of variables and data from the DB in the console. If incorrect values, or no values, were being returned, I could pinpoint the exact issue.
- Network logs were useful when I was creating all my routes. They allowed me to check that all my external files were loading.
- Responsive Layout. This project was created using a mobile first mentality. Viewing the page on a large amount of sizes and screen ratio ensured that at no point the project wasn't accessible on all devices.
#### Other Browsers Used For Testing
I do not have any devices that can run Safari. In a professional environment I assume I'd have colleagues who own Macs. If not, I'd have to run Macintosh (or perhaps just Safari) in a virtual environment on Windows or Linux.
- Firefox Developer Edition
- Microsoft Edge
### Validators
HTML, CSS, JS and Python validators were used to ensure that the code was syntatically correct. For CSS, everything came back 100% correct. However, for the HTML files that wasn't the case, and this is due to Jinja. The W3 Validator returned all instances of {{}} as errors. The solution was to simply go through each error carefully and confirm that each one was direcltly related to isntances of Jinja templating. 
- HTML Validator - [W3] (https://validator.w3.org/)
- CSS Validator - [W3] (https://jigsaw.w3.org/css-validator/)
- Python Validator - 
- JS Validator - 
### Clickthrough Testing on all Browsers
On all browsers:
- Each link was clicked and it was ensured that _blank links worked when present.
- Recipes were Created, Read, Updated and Deleted.
- It was ensured that navigation was working as intended.

---

## Deployment

## Credits
### Content
### Media
### Acknowledgements

 


Tutor Support: Xavier, Antonija, Tim, Kevin