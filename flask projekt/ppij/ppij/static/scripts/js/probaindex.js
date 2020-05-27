function showOption1() {
    document.getElementById('option1').style.display = "block";
    document.getElementById('option2').style.display = "none";
}

function showOption2() {
    document.getElementById('option2').style.display = "block";
    document.getElementById('option1').style.display = "none";
}

$('#datetimepicker1').datetimepicker({
    locale: 'fr'
});	