var myDirectives = angular.module('myDirectives', ['myCtrls']);

myDirectives.directive('change',function(){
	var index = 0;
	return {
		restrict: 'A',
		link: function($scope,element,attrs){
			setInterval(function(){

			},2000)
		}
	}
})