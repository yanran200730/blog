var myCtrls = angular.module('myCtrls', []);

myCtrls.controller('myCtrl', ['$scope', function($scope){
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