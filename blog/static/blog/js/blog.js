document.getElementById('delete-modal').addEventListener("click", function() {
	document.querySelector('.comment-modal').style.display = "flex";
});

document.querySelector('.close').addEventListener("click", function() {
	document.querySelector('.comment-modal').style.display = "none";
});