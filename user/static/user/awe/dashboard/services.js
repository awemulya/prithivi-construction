angular.module('dashboardServices', ['ngResource'])

.factory('Game', ['$resource', function($resource){
	return $resource('/app/games/', {}, {
	  query: {method:'GET', params:{}, isArray:true},
	  update: {method:'PUT', params: {gameId: '@gameId'}},
	  save: {method:'POST', params: {gameId: ''}},
	});
}])

.factory('Clubs', ['$resource', function($resource){
	return $resource('/app/clubs/:clubId', {}, {
	  query: {method:'GET', params:{clubId: ''}, isArray:true},
	  update: {method:'PUT', params: {clubId: '@clubId'}},
	  save: {method:'POST', params: {clubId: ''}},
	});
}])

.factory('Site', ['$resource', function($resource){
	return $resource('/dashboard/sites/:pId', {}, {
	  query: {method:'GET', params:{pId: ''}, isArray:true},
	  update: {method:'PUT', params: {pId: '@pId'}},
	  player: {method:'GET', params: {pId: '@pId'}},
	  save: {method:'POST', params: {pId: ''}},
	});
}])

.factory('Fixture', ['$resource', function($resource){
	return $resource('/app/fixtures/:pId', {}, {
	  query: {method:'GET', params:{pId: ''}, isArray:true},
	  update: {method:'PUT', params: {pId: '@pId'}},
	  fixture: {method:'GET', params: {pId: '@pId'}},
	  save: {method:'POST', params: {pId: ''}},
	});
}])

.factory('Video', ['$resource', function($resource){
	return $resource('app/create/videos/:videoId', {}, {
//	  query: {method:'GET', params:{}, isArray:true},
	  post: {method:'POST',  params: {}},
        update: {method:'PUT', params: {videoId: '@videoId'}},
	});
}]);


