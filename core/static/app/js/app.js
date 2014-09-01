'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'ngResource',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers'
]).

config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/shopinglist', {templateUrl: 'static/app/partials/shopinglist.html', controller: 'ShoppingCtrl'});
  $routeProvider.when('/archive', {templateUrl: 'static/app/partials/archive.html', controller: 'ArchiveCtrl'});
  $routeProvider.otherwise({redirectTo: '/shopinglist'});
}]).

run(function($rootScope, $location) {

    $rootScope.getClass = function(path) {
	    if ($location.path().substr(0, path.length) == path) {
	      return "active"
	    } else {
	      return ""
	    }
	}

});
