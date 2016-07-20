var myDirectives = angular.module('myDirectives', ['myCtrls']);

//轮播图指令
myDirectives.directive('move',function($interval){
	var timer= null;
	return {
		restrict: 'A',
		scope: true,
		link: function($scope,element,attrs){
			var timer = $interval(function(){
				for(i=1;i<6;i++){
					$scope.state["li"+i] = false;
				};
				$scope.state.index ++;
				if ($scope.state.index >= 6){
					$scope.state.index = 1;
				};
				$scope.state["li"+$scope.state.index] = true;	
			},10000)
		}
	}
})
