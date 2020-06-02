function showOption1() {
    document.getElementById('option1').style.display = "block";
    document.getElementById('option2').style.display = "none";
    var element = document.querySelector("#option1");
    element.scrollIntoView({ behavior: 'smooth' });
}
function options() {
    var element = document.querySelector("#optionsp");
    element.scrollIntoView({ behavior: 'smooth' });
}

function newDate() {
    var element = document.querySelector("#option1");
    element.scrollIntoView({ behavior: 'smooth' });
}

function newDest() {
    var element = document.querySelector("#option2");
    element.scrollIntoView({ behavior: 'smooth' });
}


function showOption2() {
    document.getElementById('option2').style.display = "block";
    document.getElementById('option1').style.display = "none";
    var element = document.querySelector("#option2");
    element.scrollIntoView({ behavior: 'smooth' });
}


function month1() {
    document.getElementById('month1res').style.display = "block";
    var element = document.querySelector("#month1res");
    element.scrollIntoView({ behavior: 'smooth' });
}

function month2() {
    document.getElementById('month2res').style.display = "block";
    var element = document.querySelector("#month2res");
    element.scrollIntoView({ behavior: 'smooth' });
}

function month3() {
    document.getElementById('month3res').style.display = "block";
    var element = document.querySelector("#month3res");
    element.scrollIntoView({ behavior: 'smooth' });
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



