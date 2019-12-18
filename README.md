Smoothie Category Image: https://beamingbaker.com/triple-berry-smoothie-5-ingredient-paleo-vegan-gluten-free-dairy-free/
Quote Background Image : https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/
Spicy Chicken Rice Recipe Image: https://www.tablespoon.com/recipes/mexican-chicken-and-rice-skillet/eda0017c-42a8-404b-bc47-22eebcd0586c
Placeholder Image location - https://woodworkersbelfast.com/placeholder-png/
I got a LOT of my images from this website - https://www.pexels.com/
library used: sweetalert: https://sweetalert.js.org/guides/

Errors Encountered: Clashing between Materialize styles and my own. 
Initializing materialize elements wasn't always working.
The for loop that populates the navbar doesn't function at the same time as the for loop that populates index.html. No idea why.
The categories dropdown on the add recipe page also breaks when the for loop gets introduced to the base html page. 
How to do environment variables?
Can't use jinja in JS, so I had to improvise for the delete button which uses sweetalert

### Celiac Haven - As someone with Celiac's disease it can be very challenging to adapt to the Gluten Free diet. Going out for meals becomes a lot more restritive, and cooking at home can become extremely monotonous. Finding recipes online becomes disheartening once you realise that nearly all of them require multiple ingredients to be replaced. Celiac Haven was created to approach that problem. It's a collection of entirely gluten free, yet delicious, recipes that people everywhere can contriubute to.

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
- 
### Wireframes
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
## Technologies used
### Languages
- HTML
- CSS
- JavaScript
- JQuery
- Python
### Additional Technologies
This includes frameworks, libraries and services.
- Backend Frameworks
    - Jinja
    - Flask
- Database and Hosting Services
    - MongoDB
    - Heroku
- Front end styling frameworks
    - Materialize
- Version Control
    - GitHub
    - Git
- IDE
    - GitPod
    - AWS Cloud9 

## Testing

## Deployment
## Credits
### Content
### Media
### Acknowledgements

 


Tutor Support: Xavier, Antonija, Tim, Kevin