var myapp = angular.module('myapp', ['ngAnimate']);

myapp.controller('myctrl', ['$scope', function($scope){
	$scope.hide = "hidden";
	$scope.show = "active"; 
	$scope.mycheck = false;
	$scope.str = "str";
	$scope.change = function(){
		console.log($scope.mycheck)
		if ($scope.mycheck){
			$scope.mycheck = false;
			console.log($scope.mycheck)
		}else{
			$scope.mycheck = true;			
		}
		console.log($scope.mycheck)
	}
}])


// myapp.directive('change', ['', function(){
// 	// Runs during compile
// 	return {
// 		// name: '',
// 		// priority: 1,
// 		// terminal: true,
// 		// scope: {}, // {} = isolate, true = child, false/undefined = no change
// 		// controller: function($scope, $element, $attrs, $transclude) {},
// 		// require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
// 		// restrict: 'A', // E = Element, A = Attribute, C = Class, M = Comment
// 		// template: '',
// 		// templateUrl: '',
// 		// replace: true,
// 		// transclude: true,
// 		// compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
// 		link: function($scope, element,, attrs) {
			
// 		}
// 	};
// }]);
