$(document).on("keydown", ":input:not(textarea)" && "input:not(#searchbar_input)", function(event) {
    return event.key != "Enter";
});

$('[name="url"]').on('input', function() {
    $('img.image').prop('src', this.value);
});


document.getElementById("search_icon_click").addEventListener('click', searchRecipes);
function searchRecipes() {
    document.getElementById("search_button").click();
}