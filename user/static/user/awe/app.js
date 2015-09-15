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
});