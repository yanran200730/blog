var myapp = angular.module('myapp', ['animate']);

myapp.controller('myctrl', ['$scope', function($scope){
	$scope.hide = "hidden";
	$scope.show = "active"; 
	$scope.mycheck = false;
	$scope.str = "str";
	$scope.change = function(){
		if ($scope.mycheck){
			$scope.mycheck = false;
		}else{
			$scope.mycheck = true;			
		}
	}
}]);

myapp.directive('change',function(){
	var index = 0;
	var left = "-10rem";
	return {
		restrict: 'A',
		link: function($scope, element, attrs){		
			setInterval(function(){
				index ++;
				index = index % 5;
				element.css("left",left);
				left = (parseInt(left) - parseInt("10rem")) + "rem";
				if ((element.css("left") == "-40rem")){
					// element.css('transform','translate3d(20rem,0,0)');
					left = "-10rem";
				}
									alert(element.css("left"));
			},2000)
		}
	}
})