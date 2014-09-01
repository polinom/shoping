'use strict';

/* Services */

angular.module('myApp.services', [])

  .factory('ItemList', ['$resource', function($resource){
      return $resource('/api/1.0/itemslist/:_id/ ', {_id:'@id'}, {
			    update: {
			      method: 'PUT'
			    }
			})
  }])

  .factory('Grocery', ['$resource', function($resource){
      return $resource('/api/1.0/groceries/ ', {_id:'@id'}, {filter: {method: 'GET'}}
      )
  }])

 .factory('Grocery', ['$resource', function($resource){
      return $resource('/api/1.0/groceries/ ', {_id:'@id'}, {filter: {method: 'GET'}}
      )
  }])
