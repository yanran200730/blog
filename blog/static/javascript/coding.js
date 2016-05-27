$(document).ready(function(){
	$(".nav").removeClass("current_page");
	$(".nav").eq(4).addClass("current_page");

	$("#zan").bind("click",function(){
		var count = $("#zan").attr("name");
		var text = $("#init").html();
		
		if (text.length == 1){
			$.ajax({
				data:{"content_type":"code","count":count},
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
	})		
});
