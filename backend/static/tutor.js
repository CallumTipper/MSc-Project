console.log("hello tutor js")

function showForm(questionId){
    // var questionId = this.id.replace(/^\D+/g, '')
    console.log(typeof questionId)
    if (typeof questionId === "number") {
        console.log(111,questionId)
        console.log(222,typeof questionId)
        var Aform = document.getElementById("Aform-hidden-"+questionId)
        Aform.style.display = "block"
        Aform.id = "Aform-block-"+questionId
  
        button = document.getElementById("add-button-"+questionId)
        button.onclick = hideForm
        button.innerHTML = "Cancel"
        console.log("dfone")
    } else {
        questionId = questionId.target.id.replace(/^\D+/g, '')
        console.log(111,questionId)
        console.log(222,typeof questionId)
        var Aform = document.getElementById("Aform-hidden-"+questionId)
        Aform.style.display = "block"
        Aform.id = "Aform-block-"+questionId
    
        button = document.getElementById("add-button-"+questionId)
        button.onclick = hideForm
        button.innerHTML = "Cancel"
        console.log("dfone")
    }
}

function hideForm(){
    console.log(this.id)
    var questionId = this.id.replace(/^\D+/g, '')
    console.log(questionId)
    questionId = questionId.toString()
    console.log(333,questionId)
    console.log(444,typeof questionId)
    var Aform = document.getElementById("Aform-block-"+questionId)
    console.log(555,Aform)
    Aform.style.display = "none"
    Aform.id = "Aform-hidden-"+questionId

    button = document.getElementById("add-button-"+questionId)
    button.onclick = showForm
    button.innerHTML = "Answer This Question"
}