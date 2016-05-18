$(document).ready(function(){
		// $.ajaxSetup({
		// // data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
		// });

	$("#form").submit(function(){
	 	var name = $("#id_name").val();
	 	var password = $("#id_password").val();

	 	$.ajax({
	 		type:"POST",
	 		data: {"username":name,"password":password},
	 		url: "/login/",
	 		cache: false,
	 		dataType: "json",
	 		success: function(data){
	 			if (data["msg"]){
	 				$("#msg").html(data["msg"]);
	 			}
	 			else{
	 				location.href = "http://www.qxfun.com/mood_category/one-thousand-and-one-letters/page/2"
	 				// location.href = "http:/www.baidu.com"//data["url"];
	 			}
	 		},
	 		error: function(){
	 			return false;
	 		}
	 	});
	 	return false;
	})


	$("#register").submit(function(){
		var register_name = $("#register_name").val();
		var register_password = $("#register_passwd").val();
		var email = $("#register_email").val();

		$.ajax({
			type:"POST",
			data: {"username":register_name,"password":register_password,"email":email},
			url: "/register/",
			cache: false,
			dataType: "json",
			success: function(data){
				if(data["msg"]){
					$("#register_msg").html(data["msg"]);
				}else{
	 				// location.href = data["url"];
	 			}
			},
			error: function(){
				alert("false")
			}
		});
		return false;
	});
});
