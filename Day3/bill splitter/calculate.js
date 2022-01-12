function calculate(){
    var person = document.getElementById("person").value;
    var total = document.getElementById("bill").value;
    var split = total / person;
    alert("Each person should pay " + split.toFixed(2) + ".");
}