$(document).ready(function(){
	$(".nav").removeClass("current_page");
	$(".nav").eq(2).addClass("current_page");

	$("#zan").bind("click",function(){
		var count = $("#zan").attr("name");
		var text = $("#init").html();

		if (text.length == 1){
			$.ajax({
				data:{"content_type":"blog","count":count},
				url:"/zan/",
				type:"POST",
				dataType:"html",
				success:function(data){
					if (data){
						$("#init").html("已赞"); 
					}	
				},
				error:function(){

				}
			})
		}	
	});

	var img_width  = $(".preview > img").width()/2;
	var img_height = $(".preview > img").height()/2;
	var width = $(document).width()/2-img_width;
	var height = $(window).height()/2-img_height;
	$(".preview").css({"left":width,"top":height});

	$("#img").on("click",function(){
		$(".shade").css({"opacity":"1","z-index":100});
		$(".shade").on("click",function(){
			$(this).css({"opacity":"0","z-index":-1})
		})
	});		
});
