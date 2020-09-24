console.log("hello student js")

var studentid = null

// document.onload(function(){
//     studentid = 
// })

function showForm(){
    var Qform = document.getElementById("Qform-hidden")
    Qform.style.display = "block"
    Qform.id = "Qform-block"
  
    button = document.getElementById("add-button")
    button.onclick = hideForm
    button.innerHTML = "Cancel"
}

function hideForm(){
    var Qform = document.getElementById("Qform-block")
    Qform.style.display = "none"
    Qform.id = "Qform-hidden"

    button = document.getElementById("add-button")
    button.onclick=showForm
    button.innerHTML = "Add Question"
}

function vote(questionId){
    console.log(questionId)
    document.getElementById(questionId+"-flag").style.color= "red"
    $.post( "ajax/test.html", function( data ) {
        $( ".result" ).html( data );
      });

}