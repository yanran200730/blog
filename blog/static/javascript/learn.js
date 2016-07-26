$(document).ready(function(){
	$(".nav").removeClass("current_page");
	$(".nav").eq(4).addClass("current_page");

	$(".zan").bind("click",function(){
		var index = $(".zan").index($(this)[0]);
		var text = $(".zan-count").eq(index).html();
		var content_id = $(".zan").eq(index).attr("data-id");
		var that = $(this);

		if (text.length == 1){
			$.ajax({
				data:{"content_type":"code","content_id":content_id},
				url:"/zan/",
				type:"POST",
				dataType:"html",
				success:function(data){
					if (data){
						$(".zan-count").eq(index).html("已赞");
						$(".praise_count").eq(index).html(data); 
						that.css("color","#E14D4C")
					}	
				},
				error:function(){

				}
			})
		}	
	})	
});

