$(document).ready(function(){
	$(".nav").removeClass("current_page");
	$(".nav").eq(4).addClass("current_page")
});

$(document).ready(function(){
	$(".body_content").each(function(){
		var max_width = 180;
		if($(this).text().length>max_width){
			$(this).text($(this).text().substring(0,max_width));
			$(this).html($(this).html()+"......");
		}
	});
});
