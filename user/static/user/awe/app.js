'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'ui.bootstrap',
  'ngResource',
  'dashboardServices',
  'myApp.dashboard',
])
.config(function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
})
.config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/dashboard'});
}])
.
config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})
.run(['$route', '$rootScope', '$location', function ($route, $rootScope, $location) {
    var original = $location.path;
    $location.path = function (path, reload) {
        if (reload === false) {
            var lastRoute = $route.current;
            var un = $rootScope.$on('$locationChangeSuccess', function () {
                $route.current = lastRoute;
                un();
            });
        }
        return original.apply($location, [path]);
    };
}])
.filter('rs', ['$filter', function ($filter) {
  return function(input) {
   if(!input){
    return 'RS 0.00';
   }
    input = parseFloat(input);

    input = input.toFixed(2);
    var inputStr = input.toString();
    if(inputStr.length<7){
        return 'RS ' +inputStr;

    }else{
        var lastFive = inputStr.substr(inputStr.length - 6);
        var lastFiveBar = inputStr.substr(0, inputStr.length - 6);
        return 'RS ' + lastFiveBar.replace(/\B(?=(\d{2})+(?!\d))/g, ",")+','+lastFive;


    }
  };
}])

.directive('jqdatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.date = date;
                    scope.$apply();
                }
            });
        }
    };
})
.directive('jqdatepickerdob', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.employee.date_of_birth = date;
                    scope.$apply();
                }
            });
        }
    };
})

.directive('salarydatedatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.newSalary.date = date;
                    scope.$apply();
                }
            });
        }
    };
})

.directive('jqdatepickerjoined', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.employee.date_joined = date;
                    scope.$apply();
                }
            });
        }
    };
})

.directive('demanddatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.demand.date = date;
                    scope.$apply();
                }
            });
        }
    };
})
.directive('voucherdatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.voucher.date = date;
                    scope.$apply();
                }
            });
        }
    };
})
.directive('sitedate', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.site.start_date = date;
                    scope.$apply();
                }
            });
        }
    };
})
.directive('datadatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
//                element.val(date);
                    scope.mainData.date = date;
                    scope.$apply();
                }
            });
        }
    };
});
