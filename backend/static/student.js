console.log("hello js")

function showForm(){
    var Qform = document.getElementById("Qform-hidden")
    Qform.style.display = "block"
    Qform.id = "Qform-block"
  
    button = document.getElementById("add-button")
    button.onclick = hideForm
    button.innerHTML = "Hide Form"
}

function hideForm(){
    var Qform = document.getElementById("Qform-block")
    Qform.style.display = "none"
    Qform.id = "Qform-hidden"

    button = document.getElementById("add-button")
    button.onclick=showForm
    button.innerHTML = "Add Question"
}