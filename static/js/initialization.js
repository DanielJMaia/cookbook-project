$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
});

document.getElementById("back_icon").addEventListener("click", goBack)

function goBack(){
    window.history.back();
}