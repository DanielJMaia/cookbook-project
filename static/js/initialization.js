$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
});

$(document).on("keydown", ":input:not(textarea)", function(event) {
    return event.key != "Enter";
});

document.getElementById("back_icon").addEventListener("click", goBack)


$('[name="image_url"]').on('change', function() {
    $('img.image').prop('src', this.value);
});

function goBack() {
    window.history.back();
}

document.getElementById("delete_button").addEventListener("click", showAlert)

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
                });
                setTimeout(function() {
                    document.getElementById("delete_form_trigger").submit();
                }, 3000);
            }
            else {
                swal("The recipe is safe!");
            }
        });
}
