
(function($){
    $.receive = function(ele){
		$.ajax({
			type:"POST",
			url: "/say/",
			dataType:"text",
			success:function(data){
				if (data){
					ele.html(data);
				}
			},
			error:function(){
				ele.html(cont_text);
			}
		})
    }
})(jQuery);

(function($){
    $.rev_count = function(count,content,index,elev){
		$.ajax({
			type:"POST",
			data:{"count":count,"content":content},
			url: "/like_count/",
			dataType:"text",
			success:function(data){
				if (data){
					$(".count").eq(index).html(data);
					elev.attr("style","color:#e14d4c")
				}
			},
			error:function(){
				// count.html(cont_text);
			}
		})
    }
})(jQuery);

//说说tab 切换 ajax请求函数
(function($){
    $.rev = function(ele1,ele2,parameter){
    	var current_page = parseInt($("#next").attr("name"));
			$.ajax({
				data:{"data":parameter,"current_page":current_page},
				type:"POST",
				url: "/talk/",
				dataType:"json",
				success:function(data){
					var len =5;
					if (data){
						var talk = data["talks"];
						var count = data["counts"];
						var page_len = data["page_len"];
						var init1,init2;
						$("#previous").attr("name",page_len.toString())

						if (parameter == "next"){
							if (current_page == page_len){
								return false
							}else{
								init1 = current_page+1;
								$("#next").attr("name",init1.toString());
							}
						}else if(parameter == "previous"){
							if (current_page == 1){
								parseInt($("#next").attr("name","1"))
							}else{
								init1 = parseInt($("#next").attr("name"))-1;
								$("#next").attr("name",init1.toString());
							}
						}
						for (var i=0;i<len;i++){
							ele1.eq(i).html(talk[i]);
							ele2.eq(i).html(count[i]);
						};
					};

				},
				error:function(){
					//ele.html(cont_text);
				}
			})
		// }
    }
})(jQuery);

//一言 ajax 请求
$(document).ready(function(){
	var butt = $("#change");
	var cont = $("#saying");
	cont_text = cont.html();

	setInterval(function(){
		$.receive(cont)
	},50000)

	butt.click(function(){
		$.receive(cont)
	});
});


//说说
$(document).ready(function(){
	var previous = $("#previous");
	var next = $("#next");
	var talk_about  = $(".talk_about");
	var counts = $(".count");

	// var count_ele = $(".count");
	// var talk_about  = $(".talk_about");
	var favorite = $(".favorite")

	favorite.click(function(){
		var that = $(this)
		index = favorite.index($(this)[0]);
		count = counts.eq(index).html();
		content = talk_about.eq(index).html();

		if ($(".favorite").eq(index).attr("style")){
		}else{
			$.rev_count(count,content,index,that);
		}
	})

	next.click(function(){
	    var length = $("#previous").attr("name")
		var current_page = parseInt($("#next").attr("name"));
		if (current_page < length){
			if (current_page == length-1){
				next.addClass("opacity")
			};
			favorite.removeAttr("style");
			previous.removeClass("opacity");
			$.rev(talk_about,counts,"next");
		};
	});

	previous.click(function(){
		var current_page = parseInt($("#next").attr("name"));
		if (current_page >1){
			if (current_page == 2){
				previous.addClass("opacity");
			};
			favorite.removeAttr("style");
			next.removeClass("opacity");
			$.rev(talk_about,counts,"previous")
		}
	});
});

// $(document).ready(function(){
// 	$(".body").each(function(){
// 		var max_width = 90;
// 		if($(this).text().length>max_width){
// 			$(this).text($(this).text().substring(0,max_width));
// 			$(this).html($(this).html()+"......");
// 		}
// 	});
// });


