// Targets alphanumeric characters and if the length of the string is greater 0, 
// exluding non-alphanumeric, the form is submitted. 

let form = document.getElementById("blogcomment");
function validateCode(event) {
    event.preventDefault(); 
    var comment = document.getElementById("id_comment").value;
    comment = comment.replace(/[^0-9a-z]/gi, '');
    if (comment.length > 0) { 
        form.submit();
        }
    else {
        alert("Only Alphanumeric characters are allowed");
      }
    }
form.addEventListener("submit", validateCode);



