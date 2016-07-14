var myDirectives = angular.module('myDirectives', ['myCtrls']);

myDirectives.directive('move',function($timeout){
	var timer= null;
	return {
		restrict: 'A',
		link: function($scope,element,attrs){
			var index = 0;
			setInterval(function(){
				
			},1000)
		}
	}
})