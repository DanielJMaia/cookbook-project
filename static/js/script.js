$(document).on("keydown", ":input:not(textarea)" && "input:not(#searchbar_input)", function(event) {
    return event.key != "Enter";
});

$('[name="url"]').on('change', function() {
    $('img.image').prop('src', this.value);
});


document.getElementById("search_icon_click").addEventListener('click', searchRecipes);
function searchRecipes() {
    document.getElementById("search_button").click();
}
/*
document.getElementById("searchbar_input").addEventListener('keypress', function(e) {
    var key = e.which || e.keyCode;
    if (key === 13) {
        document.getElementById("search_recipe_form").submit();
    }
});


*/

