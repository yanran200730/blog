$(document).ready(function(){
	$(".nav").removeClass("current_page");
	$(".nav").eq(1).addClass("current_page")

	$("#zan").bind("click",function(){
		var string = $("#title").html();
		var count = string.split(".")[1];
		var text = $("#init").html();
		
		if (text.length == 1){
			$.ajax({
				data:{"content_type":"letter","count":count},
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
