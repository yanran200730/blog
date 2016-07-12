$(document).ready(function(){
	$("#btn").on("click",function(){
		alert($("body").width())
	})
	console.log($("body").width());
});