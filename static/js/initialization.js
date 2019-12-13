$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
});

document.getElementById("back_icon").addEventListener("click", goBack)
document.getElementById("delete_button").addEventListener("click", showAlert)

function goBack() {
    window.history.back();
}

$('[name="url"]').on('change', function() {
    $('img.image').prop('src', this.value);
});

function showAlert() {
    swal({
            title: "Are you sure?",
            text: "This will permanently delete this recipe!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                swal("The recipe has been deleted!", {
                    icon: "success",
                });
            }
            else {
                swal("Action Cancelled");
            }
        });
}
