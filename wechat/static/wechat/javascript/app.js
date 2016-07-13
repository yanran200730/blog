var myapp = angular.module('myapp', [
    'ui.router', 'ngAnimate', 'myCtrls', 'myFilters',
    'myServices', 'myDirectives','ngTouch'
]);

myapp.config(['$stateProvider',function($stateProvider) {
    $stateProvider

        .state('home',{
            url:'',
            templateUrl: "/static/wechat/angular-templates/wechat.html",
            controller: "myCtrl"

        }).state('blog.detail',{
            // url:'/:blogID',
            // views:{
            //     'container':{templateUrl:'templates/blog_detail.html'}
            // }
        });
}])