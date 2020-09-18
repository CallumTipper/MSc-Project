console.log("hello tutor js")

function showForm(){
    var Aform = document.getElementById("Aform-hidden")
    Aform.style.display = "block"
    Aform.id = "Aform-block"
  
    button = document.getElementById("add-button")
    button.onclick = hideForm
    button.innerHTML = "Cancel"
}

function hideForm(){
    var Aform = document.getElementById("Aform-block")
    Aform.style.display = "none"
    Aform.id = "Aform-hidden"

    button = document.getElementById("add-button")
    button.onclick=showForm
    button.innerHTML = "Add Answer"
}