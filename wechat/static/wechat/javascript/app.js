var myapp = angular.module('myapp', [
    'ui.router', 'ngAnimate', 'myCtrls', 'myFilters',
    'myServices', 'myDirectives','ngTouch'
]);

myapp.config(['$stateProvider',function($stateProvider) {
    $stateProvider

        .state('home',{
            url:'',
            templateUrl: "/static/wechat/angular-templates/wechat.html",
            controller: "slideCtrl"

        }).state('blog.detail',{
            // url:'/:blogID',
            // views:{
            //     'container':{templateUrl:'templates/blog_detail.html'}
            // }
        });
}])


myapp.animation('.view-slide-in', function () {
    return {
        enter: function(element,done){
            var width = element.width();
            element.css({
                opacity:0
            })
            .animate({
                opacity:1
            },200,done)
        },
        leave:function(element,done){
            // element.css({

            // })
        }
    }
});