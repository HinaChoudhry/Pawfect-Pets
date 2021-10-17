let form = document.getElementById("blogcomment");

let comment = document.getElementById("comment");

function validateCode(event) {
  event.preventDefault(); 
  var comment = document.getElementById("id_comment").value;
  console.log(comment);
comment = comment.replace(/[^0-9a-z]/gi, '');

if (comment.length > 0) { 
    form.submit() 
  }
  else {
  alert("Alphanumeric inputs are only allowed");
    
    }
  }
  form.addEventListener("submit", validateCode);

 


  