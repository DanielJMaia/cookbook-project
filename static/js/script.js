document.getElementById("back_icon").addEventListener("click", goBack)

function goBack() {
    window.history.back();
}

$(document).on("keydown", ":input:not(textarea)", function(event) {
    return event.key != "Enter";
});

$('[name="url"]').on('change', function() {
    $('img.image').prop('src', this.value);
});

document.getElementById("searchbar_input").addEventListener("keypress", function(e) {
    var key = e.which || e.keyCode;
    if (key === 13) {
        console.log("this is working");
        //document.getElementById("search_recipe_form").submit();
    }});


document.getElementById("delete_button").addEventListener("click", showAlert);

function showAlert() {
    swal({
            title: "Are you sure?",
            text: "This will permanantly delete this recipe.",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                swal("The recipe has been deleted", {
                    icon: "success",
                    buttons: false
                });
                setTimeout(function() {
                    document.getElementById("delete_form_trigger").submit();
                }, 2000);
            }
            else {
                swal("The recipe is safe!");
            }
        });
}
