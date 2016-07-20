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
        "moveClass":"move"
    };
}]);

myCtrls.controller('changeSay', ['$scope','$http','$interval', function($scope,$http,$interval){
    $scope.req = function(){
        $http.get('/one/').success(function(response){
            $scope.content = response;
        }).error(function(){
            $scope.content = "「风筝的线你随时可以放开，只是别盼望我会回来。」"
        });
    };
    $scope.req();
    $interval(function(){
        $scope.req();
    },15000);
}]);

myCtrls.controller('revShuo', ['$scope','$http', function($scope,$http){
    $http.get('/shuo/').success(function(response){
        $scope.list_content = response['data_list'];
        // console.log($scope.list_content)
    }).error(function(){
        console.log("报错了！")
    })
}])

myCtrls.controller('revArticle', ['$scope','$http', function($scope,$http){
    $http.get('/wechet_article/').success(function(response){
        $scope.list_content = new Array();
        var len = response[0]["fields"].length;
        for (var i=0;i<response.length;i++){
            var myarr = new Object();
            for(var j=0;j<1;j++){
                var str = "/static/";
                var img = str + response[i]["fields"]["img"];
                myarr.title = response[i]["fields"]["title"];
                myarr.article = response[i]["fields"]["article"];
                myarr.createTime = response[i]["fields"]["createTime"];
                myarr.img = img;
                myarr.tag = response[i]["fields"]["tag"];
                myarr.user = response[i]["fields"]["author"];
            }
             $scope.list_content.push(myarr)
        }
        console.log($scope.list_content)
    }).error(function(){
        console.log("报错了!")
    })
}])