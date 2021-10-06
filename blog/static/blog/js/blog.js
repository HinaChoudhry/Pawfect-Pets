document.getElementById('delete-modal').on("click", function() {
	document.querySelector('.comment-modal').style.display = "flex";
});

document.querySelector('.close').on("click", function() {
	document.querySelector('.comment-modal').style.display = "none";
});