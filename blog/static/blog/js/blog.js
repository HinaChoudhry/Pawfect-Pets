function validateForm() {
    event.preventDefault();
    let form = document.getElementById("formcomment");
    if (form.comment.value === "")  { 
      alert("Blank spaces are not allowed");
      return false;
    }
    form.submit();
  }