'use strict';

/* Controllers */

angular.module('myApp.controllers', ['ui.bootstrap'])

  .controller('ArchiveCtrl', ['$scope', 'List', function($scope, List) {

  	$scope.lists = List.query({archived: 1});
    
  }])

  .controller('ShoppingCtrl', ['$scope', 'ItemList', 'Grocery', 'List', function($scope, Item, Grocery, List) {
    $scope.items = Item.query();

    $scope.groceries = Grocery.query();
    $scope.lists = List.query({archived: 0})

    $scope.updateGroceries = function(typed){
    	$scope.new_groceries = Grocery.query(typed).$promise;
    	$scope.new_groceries.then(function(groceries){
    		$scope.groceries = groceries;
    	})
    }

    $scope.add_grocery = function(gr) {
        	var root_id = $scope.lists[0].id;
        	var new_item = new Item({grocery: gr, items: 1, root_list: root_id});
        	var item_to_save = new Item({grocery: gr.id, items: 1, root_list: root_id});
        	item_to_save.$save().then(function(resp){
        		new_item.id = resp.id;
                $scope.items.unshift(new_item);
        	});
    }

    $scope.add = function(){
        if(typeof($scope.title) === 'object') {
        	var gr = $scope.title;
            $scope.add_grocery(gr);
        } else {
        	var gr = new Grocery({title: $scope.title, price: 0, unit: 2});
        	gr.$save().then(function(resp){
                $scope.groceries.push(gr);
                $scope.add_grocery(gr);
        	})
        }
    }

    $scope.deleteItem = function(item){
        item.$remove();
        $scope.items.splice($scope.items.indexOf(item), 1);
    }

    $scope.purchasedItem = function(item){
    	item.purchased = item.purchased ? false : true;
    	var item_to_save = new Item({id: item.id,
    	                            purchased: item.purchased,
    	                            grocery: item.grocery.id,
    	                            root_list: item.root_list })
    	item_to_save.$update();
    }

    $scope.listArchive = function(){
    	var root_id = $scope.lists[0].id;
    	var lst = new List({id: root_id})
    	lst.archived = true;
    	lst.$update().then(function(){
    		var new_list = new List({archived: false})
    		new_list.$save().then(function(){
    			$scope.items = Item.query();
    		})
    	})
    }

  }]);
