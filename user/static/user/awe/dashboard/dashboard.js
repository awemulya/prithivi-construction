'use strict';

angular.module('myApp.dashboard', ['ngRoute'])

.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = djcsrf();
}])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/dashboard', {
    templateUrl: djstatic('user/awe/dashboard/index.html'),
    controller: 'DashboardController'
  })

  $routeProvider.when('/employees/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/employee/employees.html'),
    controller: 'EmployeeController'
  })

 $routeProvider.when('/account/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/account/account.html'),
    controller: 'AccountController'
  })

$routeProvider.when('/inventory/demand-details/:demandId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/demand/demand_details.html'),
    controller: 'DemandDetailController'
  })

$routeProvider.when('/demands/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/demand/demands.html'),
    controller: 'DemandController'
  })

$routeProvider.when('/inventory/item-add/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/item_modify.html'),
    controller: 'AddItemController'
  })

$routeProvider.when('/inventory/item-details/:itemId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/item_details.html'),
    controller: 'AddItemController'
  })

$routeProvider.when('/inventory/item-modify/:itemId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/item_modify.html'),
    controller: 'AddItemController'
  })

$routeProvider.when('/inventories/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/site_inventory.html'),
    controller: 'InventoryController'
  })

  $routeProvider.when('/employees/:siteId/:eId', {
    templateUrl: djstatic('user/awe/dashboard/employee/employees_detail.html'),
    controller: 'EmployeeDetailController'
  })

  $routeProvider.when('/players/:pid', {
    templateUrl: djstatic('user/awe/dashboard/player/player_details.html'),
    controller: 'PlayerDetailController',
    resolve: {
      // I will cause a 1 second delay
      delay: function($q, $timeout) {
        var delay = $q.defer();
        $timeout(delay.resolve, 1000);
        return delay.promise;
      }
    }
  })
}])

.controller('DashboardController', ['$scope', 'Site', '$modal', '$timeout', function($scope, Site, $modal, $timeout) {
 var self = $scope;
 self.sites = Site.query();

}])

.controller('MainController', ['$scope', 'Site', '$modal', '$timeout', function($scope, Site, $modal, $timeout) {
    var self = $scope;
    self.data = {};
    self.data.site_id = '';
    self.sites = [];

    Site.query(null,
            function(data) {
            self.sites = data;
            self.data.site_id = self.sites[0].id;
            },
            function(error) {
                console.log(error);
            });
    self.getActiveSite = function(){
        return self.data.site_id;

    };

}])

.controller('EmployeeDetailController', ['$scope', 'Employee', 'Site', '$modal', '$timeout', '$routeParams',
function($scope, Employee, Site, $modal, $timeout, $routeParams) {

var self = $scope;
self.site =  $routeParams.siteId;
self.employeeId =  $routeParams.eId;
self.emp = {};
var es = new Employee();
    es.$get({eId:self.employeeId},
            function(data) {
            self.emp = data;
            },
            function(error) {
                console.log(error);
            });

}])



.controller('EmployeeAddModalController', function($scope, $modalInstance, site, employeeService, Roles) {
    var newEmployee = $scope;
    newEmployee.employee = {};
    newEmployee.options = ['Male', 'Female', 'Others'];
    newEmployee.$watch('roles', function(roles) {
        newEmployee.roles_list = angular.copy(roles);
        newEmployee.employee.role_id = newEmployee.roles_list[0];
    }, true);

    newEmployee.$watch('date', function(dob) {
       if(!dob == newEmployee.employee.date_of_birth){
       console.log("changed");
        newEmployee.employee.date_of_birth = dob;
       }
    }, true);
     newEmployee.$watch('awedate', function(dob) {
       if(!dob == newEmployee.employee.date_joined){
       console.log("changed");
        newEmployee.employee.date_joined = dob;
       }
    }, true);
    newEmployee.roles = Roles.query();
    newEmployee.employee.date_of_birth =  newEmployee.date;
    newEmployee.employee.date_joined =  newEmployee.awedate;

    newEmployee.ok = function() {
          if(angular.isObject(newEmployee.employee.role_id)){
               newEmployee.employee.role_id = newEmployee.employee.role_id.id;
            }else{
            newEmployee.employee.role_id =  newEmployee.employee.role_id;
            }
        $modalInstance.close(newEmployee.employee);
    };

    newEmployee.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('EmployeeUpdateModalController', function($scope, $modalInstance, employee, Roles) {
    var newEmployee = $scope;
    newEmployee.employee = angular.copy(employee);
    newEmployee.options = ['Male', 'Female', 'Others'];
    newEmployee.$watch('roles', function(roles) {
        newEmployee.roles_list = angular.copy(roles);
        if(!angular.equals(roles),{}){
        for(var i=0; i< newEmployee.roles_list.length; i++){
            if(newEmployee.roles_list[i].id == employee.role_id ){
            newEmployee.employee.role_id = newEmployee.roles_list[i];
            i= newEmployee.roles_list.length;
        }
        }
        }
    }, true);


    newEmployee.roles = Roles.query();
    newEmployee.ok = function() {
        if(angular.isObject(newEmployee.employee.role_id)){
               newEmployee.employee.role_id = newEmployee.employee.role_id.id;
        }else{
            newEmployee.employee.role_id =  newEmployee.employee.role_id;
        }
        $modalInstance.close(newEmployee.employee);
    };

    newEmployee.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('EmployeeHistoryModalController', function($scope, $modalInstance, employee, SalaryRecord, Salary) {
    var self = $scope;
    self.employee = angular.copy(employee);
    self.records = {};
    var salaryRC = new SalaryRecord();
    salaryRC.$query({eId:self.employee.id},
            function(data) {
            self.records = data.employee_salaries;
            },
            function(error) {
                console.log(error);
            });

    self.newSalary  = {};
    self.newSalary.salary = 10000;

    self.save = function() {
        var salaryService = new Salary();
        salaryService.salary = self.newSalary.salary;
        salaryService.date = self.newSalary.date;
        salaryService.employee_id = self.employee.id;
        salaryService.$save({},
            function(data) {
                self.records.splice(0, 0, data);
                alert("salary Saved");
            },
            function(error) {
                console.log(error);
            })
        self.newSalary = {};
        self.newSalary.salary = 10000;
    };

    self.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('EmployeePaymentsModalController', function($scope, $modalInstance, employee, EmployeePayments) {
    var self = $scope;
    self.employee = angular.copy(employee);
    self.records = {};
    var salaryRC = new EmployeePayments();
    salaryRC.$query({eId:self.employee.id},
            function(data) {
            self.records = data.employee_payments;
            },
            function(error) {
                console.log(error);
            });


    self.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('AccountController', ['$scope', 'Employee', 'SiteEmployee', 'Site', 'Role', 'SalaryRecord',
'Salary', 'EmployeePayments','SalaryPayments', '$modal', '$timeout', '$routeParams',
function($scope, Employee, SiteEmployee, Site, Role, SalaryRecord, Salary, EmployeePayments, SalaryPayments, $modal,
$timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;


}])

.controller('DemandController', ['$scope', 'SiteDemands', 'Demand', 'DemandRows', 'Site', 'Item', '$modal', '$timeout', '$routeParams',
function($scope, SiteDemands, Demand, DemandRows, Site, Item, $modal,
$timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;

    self.demands = {};

    var sd = new SiteDemands();
    sd.$query({siteID:self.siteID},
            function(data) {
            self.demands = data.demands;
            },
            function(error) {
                console.log(error);
            });


}])

.controller('DemandDetailController', ['$scope', 'Demand', 'Item', '$timeout', '$routeParams', '$location',
function($scope, Demand, Item, $timeout, $routeParams, $location) {

    var self = $scope;
    var parent = self.$parent;
    var site_id = parent.data.site_id;
    self.$watch('data', function(data) {
        if(!angular.equals(data,{})){
         if(!self.site_id){
         self.site_id = data.site_id;
         }
        }
    }, true);
    self.demandId =  $routeParams.demandId;
    self.initial_id = 1;
    self.items = Item.query();
    self.demand = {};
    if(self.demandId !=0){
        var es = new Demand();
            es.$get({Id:self.demandId},
                    function(data) {
                    self.demand = data;
                    },
                    function(error) {
                        console.log(error);
                    });
    }else{
        self.demand = {date:'', site_id:self.site_id, purpose:'',rows:[]};
    }

    self.saveDemand = function(){
    if(self.demand.id){
        var ds = new Demand();
        ds.id=self.demand.id;
        ds.date=self.demand.date;
        ds.site_id=self.demand.site_id;
        ds.purpose=self.demand.purpose;
        ds.rows = self.demand.rows;
        ds.$update({Id:self.demand.id},
                function(data) {
                self.demand = data;
                  alert("Demand "+self.demand.purpose+" Updated ");
                },
                function(error) {
                    console.log(error);
                });

    }else{
        var ds = new Demand();
        ds.site_id=self.site_id;
        ds.date=self.demand.date;
        ds.purpose=self.demand.purpose;
        ds.rows = self.demand.rows;
        ds.$save(null,
        function(data) {
        self.demand = data;
          alert("Demand "+self.demand.purpose+" Saved ");
                $location.path("/inventory/demand-details/"+data.id);
        },
        function(error) {
            console.log(error);
        });


    }

    };

    self.newItem = function(){

    self.demand.rows.push({'purpose':'',item_id:self.items[0].id,quantity:1,unit:'pieces',fulfilled_quantity:0,status:false});

    };

}])


.controller('InventoryController', ['$scope','Site', 'Item', 'Category', 'InventoryAccount', '$modal', '$timeout', '$routeParams',
function($scope, Site, Item, Category, InventoryAccount, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;
    self.items = Item.query();
    self.categories = Category.query();


}])

.controller('AddItemController', ['$scope','Site', 'Item', 'Category', 'InventoryAccount', '$modal', '$timeout',
'$routeParams', '$location',
function($scope, Site, Item, Category, InventoryAccount, $modal, $timeout, $routeParams, $location){
    var self = $scope;
    var parent = self.$parent;
    self.options = ['consumable', 'non-consumable'];
    self.item_id = $routeParams.itemId | '';
    self.item = {};
    Category.query(null,
            function(data) {
            self.categories = data;
            if(self.item.category==undefined){
                self.item.category=data[0];
            }
            },
            function(error) {
                console.log(error);
            });

    if (self.item_id){
        var itemService = new Item();
        itemService.$get({itemId:self.item_id},
            function(data) {
                self.item = data;
                for(var i=0;i<self.categories.length;i++){
                    if(self.categories[i].id == self.item.category_id){
                        self.item.category = self.categories[i];
                    }
                }
            },
            function(error) {
                console.log(error);
            });


    }
       self.save = function() {
        if (self.item_id){
            var itemService = new Item();
            itemService.name = self.item.name;
            itemService.code = self.item.code;
            itemService.description = self.item.description;
            itemService.type = self.item.type;
            itemService.unit = self.item.unit;
            itemService.category_id = self.item.category.id;
            itemService.$update({itemId:self.item_id},
                function(data) {
                  alert("Item "+self.item.name+" Updated ");
                $location.path("/inventories/"+parent.data.site_id);
                },
                function(error) {
                    console.log(error);
                });


    }else{
        var itemService = new Item();
        itemService.name = self.item.name;
        itemService.code = self.item.code;
        itemService.description = self.item.description;
        itemService.type = self.item.type;
        itemService.unit = self.item.unit;
        itemService.category_id = self.item.category.id;
        //        itemService.account_no = self.item.account_no;
        itemService.$save({},
            function(data) {
                alert("Item "+self.item.name+" Saved");
                $location.path("/inventories/"+parent.data.site_id);
            },
            function(error) {
                console.log(error);
            });
        }
    };

    self.openAddCategory = function() {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/inventory/add_category_modal.html'),
            controller: 'CategoryAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            Category: function() {
                return Category;
            }
            }
        });

        modalInstance.result.then(function(newCategory) {
        if (!angular.equals({},newCategory)){
        var cs = new Category();
            cs.name = newCategory.name;
            cs.description = newCategory.description;
            cs.parent = newCategory.parent.id;
            cs.$save(null,
            function(data) {
                self.item.category = data;
                self.categories.splice(0, 0, data);
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };




}])

.controller('CategoryAddModalController', function($scope, $modalInstance, Category) {
    var self = $scope;
    self.newCategory = {};
    Category.query(null,
        function(data) {
        self.categories = data;
        if(self.newCategory.parent==undefined){
            self.newCategory.parent=data[0];
        }
        },
        function(error) {
            console.log(error);
        });

    self.ok = function() {

        $modalInstance.close(self.newCategory);
    };

    self.cancel = function(){
                $modalInstance.close();

    };
    })


.controller('EmployeeController', ['$scope', 'Employee', 'SiteEmployee', 'Site', 'Role', 'SalaryRecord',
'Salary', 'EmployeePayments','SalaryPayments', '$modal', '$timeout', '$routeParams',
function($scope, Employee, SiteEmployee, Site, Role, SalaryRecord, Salary, EmployeePayments, SalaryPayments, $modal,
$timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;
    self.employees = {};
    self.site = "";
    var employeeService = new SiteEmployee();
    employeeService.$query({siteID:self.siteID},
            function(data) {
            self.employees = data.employee;
            self.site = data.id;
            },
            function(error) {
                console.log(error);
            });
    self.openAddEmployee = function(site) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/employee/add_employee_modal.html'),
            controller: 'EmployeeAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            site: function() {
                return site;
                },
            employeeService: function() {
                return Employee;
            },
            Roles: function() {
                return Role;
            }
            }
        });

        modalInstance.result.then(function(employeeData) {
        if (!angular.equals({},employeeData)){
        var es = new Employee();
            es.name = employeeData.name;
            es.address = employeeData.address;
            es.sex = employeeData.sex;
            es.phone = employeeData.phone;
            es.marital_status = employeeData.marital_status;
            es.status = employeeData.status;
            es.site_id = self.site;
            es.role_id = employeeData.role_id;
            es.date_of_birth = employeeData.date_of_birth;
            es.date_joined = employeeData.date_joined;
            es.$save(null,
            function(data) {
                self.employees.splice(0, 0, data);
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };


    self.openEditEmployee = function(employee) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/employee/add_employee_modal.html'),
            controller: 'EmployeeUpdateModalController',
            windowClass: 'app-modal-window',
            resolve: {
            employee: function() {
                return employee;
                },
            Roles: function() {
                return Role;
            }
            }
        });

        modalInstance.result.then(function(employeeData) {
        if (!angular.equals({},employeeData)){
        var es = new Employee();
            es.name = employeeData.name;
            es.address = employeeData.address;
            es.sex = employeeData.sex;
            es.phone = employeeData.phone;
            es.marital_status = employeeData.marital_status;
            es.status = employeeData.status;
            es.site_id = self.site;
            es.role_id = employeeData.role_id;
            es.date_of_birth = employeeData.date_of_birth;
            es.date_joined = employeeData.date_joined;
            es.$update({eId:employeeData.id},
            function(data) {
                for( var i=0; i< self.employees.length; i++){
                    if(self.employees[i].id == data.id){
                        self.employees[i]= data;

                    }
                }
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };
    self.openHistory = function(employee) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/employee/employee_history_modal.html'),
            controller: 'EmployeeHistoryModalController',
            windowClass: 'app-modal-window',
            resolve: {
            employee: function() {
                return employee;
                },
            SalaryRecord: function() {
                return SalaryRecord;
            },
            Salary: function() {
                return Salary;
            }
            }
        });
    };

    self.openSalaryPayment = function(employee) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/employee/employee_payments_modal.html'),
            controller: 'EmployeePaymentsModalController',
            windowClass: 'app-modal-window',
            resolve: {
            employee: function() {
                return employee;
                },
            EmployeePayments: function() {
                return EmployeePayments;
            }
            }
        });
    };


}])

