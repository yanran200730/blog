var myCtrls = angular.module('myCtrls', []);

myCtrls.controller('slideCtrl', ['$scope', function($scope){
    //slide 状态配置
    $scope.state = {
        "li1":true,
        "li2":false,
        "li3":false,
        "li4":false,
        "li5":false,
        "index":1,
        "moveClass":"move",  
    };
}]);