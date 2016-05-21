$(document).ready(function(){
	$(".nav").removeClass("current_page");
	$(".nav").eq(2).addClass("current_page");

	$(".article_img").hover(function(){
		index = $(".article_img").index($(this)[0]);
		$(".title").eq(index).css("color","#4db2ec");
	},function(){
		$(".title").eq(index).css("color","#111");
	})

	$(".title").hover(function(){
		$(this).css("color","#4db2ec");
	},function(){
		$(this).css("color","#111");
	});
});
