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
	  site: {method:'GET', params: {pId: '@pId'}},
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

.factory('SalaryRecord', ['$resource', function($resource){
	return $resource('/dashboard/employee-salary/:eId', {}, {
	  query: {method:'GET', params:{eId: '@eId'}},
	  update: {method:'PUT', params: {eId: '@eId'}},
	  player: {method:'GET', params: {eId: '@eId'}},
	  save: {method:'POST', params: {eId: '@eId'}},
	});
}])

.factory('EmployeePayments', ['$resource', function($resource){
	return $resource('/dashboard/employee-payments/:eId', {}, {
	  query: {method:'GET', params:{eId: '@eId'}},
	  update: {method:'PUT', params: {eId: '@eId'}},
	  player: {method:'GET', params: {eId: '@eId'}},
	  save: {method:'POST', params: {eId: '@eId'}},
	});
}])

.factory('SalaryPayments', ['$resource', function($resource){
	return $resource('/dashboard/salary-payments/:spId', {}, {
	  query: {method:'GET', params:{spId: '@spId'}},
	  update: {method:'PUT', params: {spId: '@spId'}},
	  player: {method:'GET', params: {spId: '@spId'}},
	  save: {method:'POST', params: {spId: '@spId'}},
	});
}])

.factory('Salary', ['$resource', function($resource){
	return $resource('/dashboard/salary/:sId', {}, {
	  query: {method:'GET', params:{sId: ''}},
	  update: {method:'PUT', params: {sId: '@sId'}},
	  employee: {method:'GET', params: {sId: '@sId'}},
	  save: {method:'POST', params: {sId: ''}},
	});
}])

.factory('Employee', ['$resource', function($resource){
	return $resource('/dashboard/employee/:eId', {}, {
	  query: {method:'GET', params:{eId: ''},isArray:true},
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

.factory('User', ['$resource', function($resource){
	return $resource('/user/:uId', {}, {
	  query: {method:'GET', params:{uId: ''}, isArray:true},
	  update: {method:'PUT', params: {uId: '@uId'}},
	  employee: {method:'GET', params: {uId: '@uId'}},
	  save: {method:'POST', params: {uId: ''}},
	});
}])
.factory('Item', ['$resource', function($resource){
	return $resource('/inventory/items/:itemId', {}, {
	  query: {method:'GET', params:{itemId: ''}, isArray:true},
	  update: {method:'PUT', params: {itemId: '@itemId'}},
	  employee: {method:'GET', params: {itemId: '@itemId'}},
	  save: {method:'POST', params: {itemId: ''}},
	});
}])

.factory('Category', ['$resource', function($resource){
	return $resource('/inventory/categories/:cId', {}, {
	  query: {method:'GET', params:{cId: ''}, isArray:true},
	  update: {method:'PUT', params: {cId: '@cId'}},
	  employee: {method:'GET', params: {cId: '@cId'}},
	  save: {method:'POST', params: {cId: ''}},
	});
}])

.factory('InventoryAccount', ['$resource', function($resource){
	return $resource('/inventory/account/:Id', {}, {
	  query: {method:'GET', params:{Id: ''}, isArray:true},
	  update: {method:'PUT', params: {Id: '@Id'}},
	  employee: {method:'GET', params: {Id: '@Id'}},
	  save: {method:'POST', params: {Id: ''}},
	});
}])

.factory('SiteDemands', ['$resource', function($resource){
	return $resource('/inventory/site-demands/:siteID', {}, {
	  query: {method:'GET', params:{siteID: '@siteID'}},
	  update: {method:'PUT', params: {siteID: '@siteID'}},
	  player: {method:'GET', params: {siteID: '@siteID'}},
	  save: {method:'POST', params: {siteID: '@siteID'}},
	});
}])

.factory('SitePayroll', ['$resource', function($resource){
	return $resource('/employee/site-payrolls/:siteID', {}, {
	  query: {method:'GET', params:{siteID: '@siteID'}},
	  update: {method:'PUT', params: {siteID: '@siteID'}},
	  player: {method:'GET', params: {siteID: '@siteID'}},
	  save: {method:'POST', params: {siteID: '@siteID'}},
	});
}])


.factory('Demand', ['$resource', function($resource){
	return $resource('/inventory/demand/:Id', {}, {
	  query: {method:'GET', params:{Id: ''}, isArray:true},
	  update: {method:'PUT', params: {Id: '@Id'}},
	  employee: {method:'GET', params: {Id: '@Id'}},
	  save: {method:'POST', params: {Id: ''}},
	});
}])

.factory('Voucher', ['$resource', function($resource){
	return $resource('/employee/payroll/:Id', {}, {
	  query: {method:'GET', params:{Id: ''}, isArray:true},
	  update: {method:'PUT', params: {Id: '@Id'}},
	  employee: {method:'GET', params: {Id: '@Id'}},
	  save: {method:'POST', params: {Id: ''}},
	});
}])

.factory('DemandRows', ['$resource', function($resource){
	return $resource('/inventory/demands-rows/:Id', {}, {
	  query: {method:'GET', params:{Id: ''}, isArray:true},
	  update: {method:'PUT', params: {Id: '@Id'}},
	  employee: {method:'GET', params: {Id: '@Id'}},
	  save: {method:'POST', params: {Id: ''}},
	});
}])

.factory('Tasks', ['$resource', function($resource){
	return $resource('/progress/tasks/:Id', {}, {
	  query: {method:'GET', params:{Id: ''}, isArray:true},
	  update: {method:'PUT', params: {Id: '@Id'}},
	  employee: {method:'GET', params: {Id: '@Id'}},
	  save: {method:'POST', params: {Id: ''}},
	});
}])

.factory('SiteTasks', ['$resource', function($resource){
	return $resource('/progress/site-tasks/:siteID', {}, {
	  query: {method:'GET', params:{siteID: '@siteID'}},
	  update: {method:'PUT', params: {siteID: '@siteID'}},
	  player: {method:'GET', params: {siteID: '@siteID'}},
	  save: {method:'POST', params: {siteID: '@siteID'}},
	});
}])





