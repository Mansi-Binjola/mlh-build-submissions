document.getElementById("calculate").addEventListener("click", function() {
    var person = document.getElementById("person").value;
    var total = document.getElementById("total").value;
    var split = total / person;
    alert("Each person should pay " + split);
    document.getElementById("result").innerHTML = split;
});