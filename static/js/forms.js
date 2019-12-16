$(document).on("keydown", ":input:not(textarea)" && "input:not(#searchbar_input)", function(event) {
    return event.key != "Enter";
});