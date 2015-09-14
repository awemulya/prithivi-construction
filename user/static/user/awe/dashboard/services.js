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
.factory('SiteEmployee', ['$resource', function($resource){
	return $resource('/dashboard/site-employee/:siteID', {}, {
	  query: {method:'GET', params:{siteID: '@siteID'}},
	  update: {method:'PUT', params: {siteID: '@siteID'}},
	  player: {method:'GET', params: {siteID: '@siteID'}},
	  save: {method:'POST', params: {siteID: '@siteID'}},
	});
}])

.factory('Employee', ['$resource', function($resource){
	return $resource('/dashboard/employee/:eId', {}, {
	  query: {method:'GET', params:{eId: ''}},
	  update: {method:'PUT', params: {eId: '@eId'}},
	  employee: {method:'GET', params: {eId: '@eId'}},
	  save: {method:'POST', params: {eId: ''}},
	});
}])

.factory('Role', ['$resource', function($resource){
	return $resource('/dashboard/role/:roleId', {}, {
	  query: {method:'GET', params:{roleId: ''}, isArray:true},
	  update: {method:'PUT', params: {roleId: '@roleId'}},
	  employee: {method:'GET', params: {roleId: '@roleId'}},
	  save: {method:'POST', params: {roleId: ''}},
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


