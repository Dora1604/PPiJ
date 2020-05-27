function showOption1() {
    document.getElementById('option1').style.display = "block";
    document.getElementById('option2').style.display = "none";
}

function showOption2() {
    document.getElementById('option2').style.display = "block";
    document.getElementById('option1').style.display = "none";
}

new Litepicker({
    element: document.getElementById('datepicker'),
    singleMode: false,
    firstDay: 1,
    format: "DD.MM.YYYY.",
    onSelect(date1, date2) {
        document.getElementById('showstartdate').innerText = date1.toDateString();
        document.getElementById('showenddate').innerText = date2.toDateString();
    }
})