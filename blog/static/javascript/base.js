// 返回顶部
$(document).ready(function(){
	$(window).scroll(function(){
		if ($(window).scrollTop() >= 800){
			$("#top").show();
		}else{
			$("#top").hide();
		}
	});

	$("#to_top").bind("click",function(){
		$("body,html").animate({ scrollTop:0 },1000)
		return false;
	});

	$(".back_to_top ").hover(
		function(){
			$("#prompt_content").fadeIn(200);
			$("#prompt").fadeIn(200);
		},function(){
			$("#prompt_content").fadeOut(400);
			$("#prompt").fadeOut(400);
	})

})

// 返回顶部提示 + 向上滚动设置nav为固定定位
$(document).ready(function(){
	$("body,html").bind("mousewheel",function(event,delta){
		if ($(window).scrollTop() >= 120 && delta > 0){
			$("#header").attr("class","head_scroll");
			$("#logo").attr("class","logo_scroll");
			$("#ulist").css("top","0px");
			$("#ulist li").css({"lineHeight":"40px","height":"40px"})
		}else{
			$("#header").attr("class","header");
			$("#logo").attr("class","logo");
			$("#ulist").css("top","59px");
			$("#ulist li").css({"lineHeight":"48px","height":"48px"});			
		}
	});
})