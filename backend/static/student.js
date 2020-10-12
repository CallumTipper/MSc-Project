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

function flag(questionId){
    console.log(questionId)
    document.getElementById(questionId+"-flag").style.color= "red"

    $.ajax({
        type: "POST",
        url: "/student",
        data: {"post-origin": "flag", "questionId": questionId},
        success: function() {   
            setTimeout(function(){
                location.reload();
            }, 300);
              
        }
    });   
}

function like(questionId){
    console.log(questionId)
    document.getElementById(questionId+"-like").style.color= "red"

    $.ajax({
        type: "POST",
        url: "/student",
        data: {"post-origin": "like", "questionId": questionId},
        success: function() {   
            setTimeout(function(){
                location.reload();
            }, 300);
              
        }
    });   
}

function query(questionId){
    console.log(questionId)
    document.getElementById(questionId+"-query").style.color= "red"

    $.ajax({
        type: "POST",
        url: "/student",
        data: {"post-origin": "query", "questionId": questionId},
        success: function() {   
            setTimeout(function(){
                location.reload();
            }, 300);
              
        }
    });   
}