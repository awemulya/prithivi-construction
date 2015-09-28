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

$routeProvider.when('/users/', {
    templateUrl: djstatic('user/awe/dashboard/users/users.html'),
    controller: 'UserController'
  })

$routeProvider.when('/party/', {
    templateUrl: djstatic('user/awe/dashboard/inventory/party/parties.html'),
    controller: 'PartyController'
  })

$routeProvider.when('/bank/', {
    templateUrl: djstatic('user/awe/dashboard/account/bank/banks.html'),
    controller: 'BankController'
  })

$routeProvider.when('/vendor/', {
    templateUrl: djstatic('user/awe/dashboard/account/vendor/vendors.html'),
    controller: 'VendorController'
  })

$routeProvider.when('/bank-withdraw/:bankId', {
    templateUrl: djstatic('user/awe/dashboard/account/bank/withdraw.html'),
    controller: 'BankWithDrawController'
  })

$routeProvider.when('/vendor-payment/:vendorId', {
    templateUrl: djstatic('user/awe/dashboard/account/vendor/payment.html'),
    controller: 'VendorPaymentController'
  })

$routeProvider.when('/bank-withdraw-list/:bankId', {
    templateUrl: djstatic('user/awe/dashboard/account/bank/withdraw_list.html'),
    controller: 'BankWithDrawListController'
  })

$routeProvider.when('/vendor-payment-list/:vendorId', {
    templateUrl: djstatic('user/awe/dashboard/account/vendor/payment_list.html'),
    controller: 'VendorPaymentListController'
  })
$routeProvider.when('/purchase/', {
    templateUrl: djstatic('user/awe/dashboard/inventory/purchase/purchase.html'),
    controller: 'PurchaseController'
  })

$routeProvider.when('/purchase/:partyId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/purchase/purchase.html'),
    controller: 'PartyPurchaseController'
  })

$routeProvider.when('/payment/:partyId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/party/payments.html'),
    controller: 'PartyPaymentController'
  })

 $routeProvider.when('/account/summary/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/account/account_summary.html'),
    controller: 'AccountSummaryController'
  })

$routeProvider.when('/account/accounts/', {
    templateUrl: djstatic('user/awe/dashboard/account/accounts.html'),
    controller: 'AccountController'
  })

$routeProvider.when('/inventory/demand-details/:demandId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/demand/demand_details.html'),
    controller: 'DemandDetailController'
  })

$routeProvider.when('/inventory/purchase-details/:purchaseId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/purchase/purchase_details.html'),
    controller: 'PurchaseDetailController'
  })

$routeProvider.when('/site/site-details/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/site/site_details.html'),
    controller: 'SiteDetailController'
  })


$routeProvider.when('/employee/voucher-details/:vId', {
    templateUrl: djstatic('user/awe/dashboard/account/payroll/payroll_details.html'),
    controller: 'PayrollDetailController'
  })

$routeProvider.when('/progress/progress-details/:pId', {
    templateUrl: djstatic('user/awe/dashboard/progress/progress_details.html'),
    controller: 'ProgressDetailController'
  })

$routeProvider.when('/demands/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/demand/demands.html'),
    controller: 'DemandController'
  })

$routeProvider.when('/account/payroll/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/account/payroll/payroll.html'),
    controller: 'PayrollController'
  })

$routeProvider.when('/progress/progress/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/progress/progress.html'),
    controller: 'ProgressController'
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

$routeProvider.when('/inventories/account/:siteId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/inventory_account.html'),
    controller: 'InventoryAccountController'
  })

$routeProvider.when('/inventory/item-consumption/:accountId', {
    templateUrl: djstatic('user/awe/dashboard/inventory/inventory_account_consumption.html'),
    controller: 'InventoryAccountConsumptionController'
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
    self.data.is_admin = USER_ADMIN;
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



.controller('EmployeeAddModalController', function($scope, $modalInstance, Role) {
    var newEmployee = $scope;
    newEmployee.employee = {};
    newEmployee.options = ['Male', 'Female', 'Others'];
    Role.query(null,
        function(data) {
        newEmployee.roles = data;
        newEmployee.employee.role_id = newEmployee.roles[0].id;
        newEmployee.employee.sex = newEmployee.options[0];
        },
        function(error) {
            console.log(error);
        });


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
    newEmployee.employee.date_of_birth =  newEmployee.date;
    newEmployee.employee.date_joined =  newEmployee.awedate;

    newEmployee.ok = function() {
        $modalInstance.close(newEmployee.employee);
    };

    newEmployee.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('PartyAddModalController', function($scope, $modalInstance, party) {
    var newParty = $scope;
    newParty.party = angular.copy(party);
    newParty.ok = function() {
        $modalInstance.close(newParty.party);
    };

    newParty.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('BankAddModalController', function($scope, $modalInstance, bank) {
    var self = $scope;
    self.bank = angular.copy(bank);
    self.ok = function() {
        $modalInstance.close(self.bank);
    };

    self.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('VendorAddModalController', function($scope, $modalInstance, vendor) {
    var self = $scope;
    self.vendor = angular.copy(vendor);
    self.ok = function() {
        $modalInstance.close(self.vendor);
    };

    self.cancel = function() {
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

.controller('UserUpdateModalController', function($scope, $modalInstance, user, User) {
    var newUser = $scope;
    newUser.user = angular.copy(user);
    newUser.ok = function() {
        $modalInstance.close(newUser.user);
    };

    newUser.cancel = function() {
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

.controller('PartyAddPaymentModalController', function($scope, $modalInstance, party) {
    var self = $scope;
    self.party = angular.copy(party);

      self.ok = function() {
        self.party.date = self.date;
        $modalInstance.close(self.party);
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

.controller('AccountSummaryController', ['$scope', 'Employee', 'SiteEmployee', 'Site', 'Role', 'SalaryRecord',
'Salary', 'EmployeePayments','SalaryPayments', '$modal', '$timeout', '$routeParams',
function($scope, Employee, SiteEmployee, Site, Role, SalaryRecord, Salary, EmployeePayments, SalaryPayments, $modal,
$timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;


}])

.controller('AccountController', ['$scope', 'LedgerAccount', '$modal', '$timeout', '$routeParams',
function($scope, LedgerAccount, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.accounts = LedgerAccount.query();


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

.controller('PurchaseController', ['$scope', 'Purchase', '$modal', '$timeout', '$routeParams',
function($scope, Purchase, $modal, $timeout, $routeParams){
    var self = $scope;
    self.data_list = Purchase.query();
}])

.controller('BankWithDrawListController', ['$scope', 'BankWithdraw', '$modal', '$timeout', '$routeParams',
function($scope, BankWithdraw, $modal, $timeout, $routeParams){
    var self = $scope;
    self.bankId = $routeParams.bankId;
    self.data_list = {};
    var ps = new BankWithdraw();
    ps.$query({Id:self.bankId},
            function(data) {
            self.data_list = data;
            self.bank_name = data.name;
            },
            function(error) {
                console.log(error);
            });
}])

.controller('VendorPaymentListController', ['$scope', 'VendorPayment', '$modal', '$timeout', '$routeParams',
function($scope, VendorPayment, $modal, $timeout, $routeParams){
    var self = $scope;
    self.vendorId = $routeParams.vendorId;
    self.data_list = {};
    var ps = new VendorPayment();
    ps.$query({Id:self.vendorId},
            function(data) {
            self.data_list = data;
            self.vendor_name = data.name;
            },
            function(error) {
                console.log(error);
            });
}])

.controller('PartyPurchaseController', ['$scope', 'PartyPurchase', '$modal', '$timeout', '$routeParams',
function($scope, PartyPurchase, $modal, $timeout, $routeParams){
    var self = $scope;
    self.partyId = $routeParams.partyId;
    self.data_list = {};
    var ps = new PartyPurchase();
    ps.$query({Id:self.partyId},
            function(data) {
            self.data_list = data.purchase;
            self.party_name = data.name;
            },
            function(error) {
                console.log(error);
            });
}])

.controller('PayrollController', ['$scope', 'SitePayroll', '$routeParams',
function($scope, SitePayroll, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;

    self.payrolls = {};

    var ps = new SitePayroll();
    ps.$query({siteID:self.siteID},
            function(data) {
            self.payrolls = data.payrolls;
            },
            function(error) {
                console.log(error);
            });


}])

.controller('ProgressController', ['$scope', 'SiteTasks', '$routeParams',
function($scope, SiteTasks, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;

    self.tasks = {};

    var ts = new SiteTasks();
    ts.$query({siteID:self.siteID},
            function(data) {
            self.tasks = data.progresses;
            },
            function(error) {
                console.log(error);
            });


}])

.controller('DemandDetailController', ['$scope', 'Demand', 'Item', 'Category', 'NextAccountNo', '$modal', '$timeout', '$routeParams', '$location',
function($scope, Demand, Item, Category, NextAccountNo, $modal, $timeout, $routeParams, $location) {
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    var self = $scope;
    var parent = self.$parent;
    self.site_id = parent.data.site_id;
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
        self.demand = {date:today, site_id:self.site_id, purpose:'',rows:[]};
    }

    self.saveDemand = function(){
    if (!self.demand.purpose){
        alert("please enter demand purpose");
    }else{
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
    }

    };

    self.newItem = function(){

    self.demand.rows.push({'purpose':'',item_id:self.items[0].id,quantity:1,unit:'pieces',fulfilled_quantity:0,status:false});

    };

       self.openAddItem = function(index) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/inventory/add_item_modal.html'),
            controller: 'ItemAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            Item: function() {
                return Item;
            },
            Category: function() {
                return Category;
            },
            NextAccountNo: function() {
                return NextAccountNo;
            }
            }
        });

        modalInstance.result.then(function(newItem) {
        if (!angular.equals({},newItem)){
        var cs = new Item();
            cs.name = newItem.name;
            cs.description = newItem.description;
            cs.category_id = newItem.category_id;
              if(!newItem.account_no){
                    self.next_account_data = NextAccountNo.query(null,
                    function(data) {
                    newItem.account_no = data.ac_no;
                    cs.account_no = newItem.account_no;
                    },
                    function(error) {
                        console.log(error);
                    });
                    }else{
                        cs.account_no = newItem.account_no;
                    }
            cs.type = newItem.type;
            cs.unit = newItem.unit;
            cs.code = newItem.code;
            cs.$save(null,
            function(data) {
                self.items.splice(0, 0, data);
                self.demand.rows[index].item_id = data.id;
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };

}])


.controller('PartyPaymentController', ['$scope', 'PartyPayment', '$modal', '$timeout',
'$routeParams', '$location',
function($scope, PartyPayment, $modal, $timeout, $routeParams, $location) {
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    var self = $scope;
    self.partyId = $routeParams.partyId;
    self.mainData = {};
    var ps = new PartyPayment();
    ps.$query({Id:self.partyId},
            function(data) {
            self.mainData = data;
            },
            function(error) {
                console.log(error);
            });

 self.newPurchase = function(){

    self.mainData.rows.push({'date':today,'voucher_no':1,'amount':0.00});

    };

    self.savePayment = function(){
        var ps = new PartyPayment();
            ps.rows = self.mainData.rows;
            ps.id = self.mainData.id;
                ps.$update({Id:self.mainData.id},
                function(data) {
                self.mainData = data;
                    alert("payment Saved");
                },
                function(error) {
                    console.log(error);
                });


    };

}])

.controller('PurchaseDetailController', ['$scope', 'Purchase', 'Item', 'Category', 'Party', 'NextAccountNo', '$modal', '$timeout',
'$routeParams', '$location',
function($scope, Purchase, Item, Category, Party, NextAccountNo, $modal, $timeout, $routeParams, $location) {
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    var self = $scope;
    var parent = self.$parent;
    self.site_id = parent.data.site_id;
    self.$watch('data', function(data) {
        if(!angular.equals(data,{})){
         if(!self.site_id){
         self.site_id = data.site_id;
         }
        }
    }, true);
    self.purchaseId =  $routeParams.purchaseId;
    self.items = Item.query();
    self.parties = Party.query();
    self.mainData = {};
    if(self.purchaseId && self.purchaseId !=0){
    console.log(self.purchaseId);
        console.log('not zero');
        var ss = new Purchase();
            ss.$get({Id:self.purchaseId},
                    function(data) {
                    self.mainData = data;
                    },
                    function(error) {
                        console.log(error);
                    });
    }else{
        self.mainData = {date:today, party_id:1, voucher_no:'',rows:[]};
    }

    self.savePurchase = function(){
        if(!self.mainData.voucher_no){
            alert("please Enter Voucher NO");
        }else{
    if(self.mainData.id){
        var ps = new Purchase();
        ps.id=self.mainData.id;
        ps.date=self.mainData.date;
        ps.credit=self.mainData.credit;
        ps.party_id=self.mainData.party_id;
        ps.voucher_no=self.mainData.voucher_no;
        ps.rows = self.mainData.rows;
        ps.$update({Id:self.mainData.id},
                function(data) {
                self.mainData = data;
                  alert("Purchase "+self.mainData.voucher_no+" Updated ");
                },
                function(error) {
                    console.log(error);
                });

    }else{
        var ps = new Purchase();
        ps.date=self.mainData.date;
        ps.credit=self.mainData.credit;
        ps.party_id=self.mainData.party_id;
        ps.voucher_no=self.mainData.voucher_no;
        ps.rows = self.mainData.rows;
        ps.$save(null,
        function(data) {
        self.mainData = data;
          alert("Purchase "+self.mainData.voucher_no+" Saved ");
                $location.path("/inventory/purchase-details/"+data.id, false);
        },
        function(error) {
            console.log(error);
        });


    }
    }

    };

    self.newItem = function(){
    var sn_count = self.mainData.rows.length || 0;
    sn_count += 1;
    self.mainData.rows.push({item_id:self.items[0].id,quantity:1,unit:'pieces',rate:0.0,discount:0.0,sn:sn_count});

    };

       self.openAddItem = function(index) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/inventory/add_item_modal.html'),
            controller: 'ItemAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            Item: function() {
                return Item;
            },
            Category: function() {
                return Category;
            },
            NextAccountNo: function() {
                return NextAccountNo;
            }
            }
        });

        modalInstance.result.then(function(newItem) {
        if (!angular.equals({},newItem)){
        var cs = new Item();
            cs.name = newItem.name;
            cs.description = newItem.description;
            cs.category_id = newItem.category_id;
              if(!newItem.account_no){
                    self.next_account_data = NextAccountNo.query(null,
                    function(data) {
                    newItem.account_no = data.ac_no;
                    cs.account_no = newItem.account_no;
                    },
                    function(error) {
                        console.log(error);
                    });
                    }else{
                cs.account_no = newItem.account_no;

                    }

            cs.type = newItem.type;
            cs.unit = newItem.unit;
            cs.code = newItem.code;
            cs.$save(null,
            function(data) {
                self.items.splice(0, 0, data);
                self.mainData.rows[index].item_id = data.id;
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };

    self.openAddParty = function(party) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/inventory/party/add_party_modal.html'),
            controller: 'PartyAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            party: function() {
                return party;
            }
            }
        });

        modalInstance.result.then(function(partyData) {
        if (!angular.equals({},partyData)){
        var ps = new Party();
            ps.name = partyData.name;
            ps.address = partyData.address;
            ps.phone_no = partyData.phone_no;
            ps.pan_no = partyData.pan_no;
            if(partyData.id){
                ps.$update({Id:partyData.id},
                function(data) {
                    self.mainData.party_id = data.id;
                    for(var i=0; i<self.parties.length; i++){
                        if(self.parties[i].id == data.id){
                            self.parties[i]= data;
                            i= self.parties.length;
                        }
                    }
                },
                function(error) {
                    console.log(error);
                });
            }else{
                ps.$save(null,
                function(data) {
                    self.mainData.party_id = data.id;
                    self.parties.splice(0, 0, data);
                },
                function(error) {
                    console.log(error);
                });

            }


            }
        });
    };


}])

.controller('SiteDetailController', ['$scope', 'Site', 'User','$modal', '$timeout', '$routeParams', '$location',
function($scope, Site, User, $modal, $timeout, $routeParams, $location) {
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    var self = $scope;
    var parent = self.$parent;
    self.site_Id =  $routeParams.siteId;
    self.users = User.query();
    self.site = {};
    if(self.site_Id !=0){
        parent.data.site_id = self.site_Id;
        var ss = new Site();
            ss.$site({pId:self.site_Id},
                    function(data) {
                    self.site = data;
                    },
                    function(error) {
                        console.log(error);
                    });
    }else{
        self.site = {start_date:today, name:'New Site', description:'', address:'', incharge:[]};
    }

    self.saveSite = function(){
    if(self.site.id){
        var ss = new Site();
        ss.id=self.site.id;
        ss.start_date=self.site.start_date;
        ss.name=self.site.name;
        ss.description=self.site.description;
        ss.address=self.site.address;
        ss.incharge = self.site.incharge;
        ss.$update({pId:self.site.id},
                function(data) {
                self.site = data;
                  alert("site "+self.site.name+" Updated ");
                },
                function(error) {
                    console.log(error);
                });

    }else{
        var ss = new Site();
        ss.start_date=self.site.start_date;
        ss.name=self.site.name;
        ss.description=self.site.description;
        ss.address=self.site.address;
        ss.incharge = self.site.incharge;
        ss.$save(null,
        function(data) {
        self.site = data;
          alert("site "+self.site.name+" Saved ");
                $location.path("/site/site-details/"+data.id);
        },
        function(error) {
            console.log(error);
        });


    }

    };
    self.addIncharge = function(){
    self.site.incharge.push({'id':self.users[0].id});

    }
    self.removeIncharge = function(index){
    self.site.incharge.splice(index,1);

    }

}])

.controller('PayrollDetailController', ['$scope', 'Voucher', 'Employee', 'SiteEmployee', 'Role', '$modal', '$timeout', '$routeParams', '$location',
function($scope, Voucher, Employee, SiteEmployee, Role, $modal, $timeout, $routeParams, $location) {
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    var self = $scope;
    var parent = self.$parent;
    self.employees = {};
    self.site_id = parent.data.site_id;
    self.$watch('data', function(data) {
        if(!angular.equals(data,{})){
        if(data.site_id){
        self.site_id = data.site_id;
            self.voucher.site_id = data.site_id;
            var se = new SiteEmployee();
            se.$query({siteID:data.site_id},
                function(data) {
                self.employees = data.employee;
                },
                function(error) {
                    console.log(error);
                });
            }
        }
    }, true);
    self.voucherId =  $routeParams.vId;
    self.initial_id = 1;
    self.voucher = {};
    if(self.voucherId !=0){
        var es = new Voucher();
            es.$get({Id:self.voucherId},
                    function(data) {
                    self.voucher = data;
                    },
                    function(error) {
                        console.log(error);
                    });
    }else{
        self.voucher = {date:today, site_id:self.site_id, voucher_no:1, rows:[]};
    }

    self.saveVoucher = function(){
    if(self.voucher.id){
        var ds = new Voucher();
        ds.id = self.voucher.id;
        ds.date = self.voucher.date;
        ds.site_id = self.voucher.site_id;
        ds.voucher_no = self.voucher.voucher_no;
        ds.rows = self.voucher.rows;
        ds.$update({Id:self.voucher.id},
                function(data) {
                self.voucher = data;
                  alert("Payroll Voucher "+self.voucher.voucher_no+" Updated ");
                },
                function(error) {
                    console.log(error);
                });

    }else{
        var ds = new Voucher();
        ds.site_id = parent.data.site_id;
        ds.date = self.voucher.date;
        ds.voucher_no = self.voucher.voucher_no;
        ds.rows = self.voucher.rows;
        ds.$save(null,
        function(data) {
        self.voucher = data;
          alert("Payroll Voucher "+self.voucher.voucher_no+" Saved ");
                $location.path("/employee/voucher-details/"+data.id);
        },
        function(error) {
            console.log(error);
        });


    }

    };

    self.newItem = function(){
    var sn = self.voucher.rows.length || 0;
    self.voucher.rows.push({'sn':sn+1,employee_id:self.employees[0].id,amount:0.0,paid_date:today,
    start_date:today,last_date:today});

    };

   self.openAddEmployee = function(index) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/employee/add_employee_modal.html'),
            controller: 'EmployeeAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            Role: function() {
                return Role;
            }
            }
        });

        modalInstance.result.then(function(employeeData) {
        if (!angular.equals({},employeeData)){
        var es = new Employee();
            var es = new Employee();
            es.name = employeeData.name;
            es.address = employeeData.address;
            es.sex = employeeData.sex;
            es.phone = employeeData.phone;
            es.marital_status = employeeData.marital_status;
            es.status = employeeData.status;
            es.site_id = parent.data.site_id;
            es.role_id = employeeData.role_id;
            es.date_of_birth = employeeData.date_of_birth;
            es.date_joined = employeeData.date_joined;

            es.$save(null,
            function(data) {
                self.employees.splice(0, 0, data);
                self.voucher.rows[index].employee_id = data.id;
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };

}])


.controller('ProgressDetailController', ['$scope', 'Tasks', '$timeout', '$routeParams', '$location',
function($scope, Tasks, $timeout, $routeParams, $location) {
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    var self = $scope;
    var parent = self.$parent;
    self.options = ['planning', 'pending', 'started', 'completed'];
    self.site_id = parent.data.site_id;
    self.$watch('data', function(data) {
        if(!angular.equals(data,{})){
        if(data.site_id){
        self.site_id = data.site_id;
            self.tasks.site_id = data.site_id;
            }
        }
    }, true);
    self.taskId =  $routeParams.pId;
    self.initial_id = 1;
    self.tasks = {};
    if(self.taskId !=0){
        var ts = new Tasks();
            ts.$get({Id:self.taskId},
                    function(data) {
                    self.tasks = data;
                    },
                    function(error) {
                        console.log(error);
                    });
    }else{
        self.tasks = {start_date:today, site_id:self.site_id, deadline:today, description:'', status_choices:self.options[0],
        status:false, rows:[]};
    }

    self.saveTask = function(){
    if(self.tasks.id){
        var ts = new Tasks();
        ts.site_id = self.site_id;
        ts.start_date = self.tasks.start_date;
        ts.deadline = self.tasks.deadline;
        ts.description = self.tasks.description;
        ts.status_choices = self.tasks.status_choices;
        ts.status = self.tasks.status;
        ts.rows = self.tasks.rows;
        ts.$update({Id:self.tasks.id},
                function(data) {
                self.tasks = data;
                  alert("Task "+self.tasks.description+" Updated ");
                },
                function(error) {
                    console.log(error);
                });

    }else{
        var ts = new Tasks();
        ts.site_id = self.site_id;
        ts.start_date = self.tasks.start_date;
        ts.deadline = self.tasks.deadline;
        ts.description = self.tasks.description;
        ts.status_choices = self.tasks.status_choices;
        ts.status = self.tasks.status;
        ts.rows = self.tasks.rows;
        ts.$save(null,
        function(data) {
        self.tasks = data;
          alert("Task "+self.tasks.description+" Saved ");
                $location.path("/progress/progress-details/"+data.id);
        },
        function(error) {
            console.log(error);
        });


    }

    };

    self.newItem = function(){
        self.tasks.rows.push({start_date:today, site_id:self.site_id, deadline:today, description:'', status_choices:self.options[0], status:false});
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

.controller('InventoryAccountController', ['$scope','Site', 'Item', 'Category', 'InventoryAccount',
'SiteInventoryAccount', '$modal', '$timeout', '$routeParams',
function($scope, Site, Item, Category, InventoryAccount, SiteInventoryAccount, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.siteID =  $routeParams.siteId;
    parent.data.site_id = self.siteID;
      var sia = new SiteInventoryAccount();
        sia.$get({Id:self.siteID},
            function(data) {
                self.accounts = data.accounts;
            },
            function(error) {
                console.log(error);
            });


}])

.controller('InventoryAccountConsumptionController', ['$scope', 'InventoryAccountConsumption', '$modal', '$timeout', '$routeParams',
function($scope,  InventoryAccountConsumption, $modal, $timeout, $routeParams){
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    var self = $scope;
    self.accountId =  $routeParams.accountId;
      var sia = new InventoryAccountConsumption();
        sia.$get({Id:self.accountId},
            function(data) {
                self.mainData = data;
            },
            function(error) {
                console.log(error);
            });
    self.newConsumption = function(){
     var sn = self.mainData.rows.length || 0;
    self.mainData.rows.push({'sn':sn+1,'purpose':'','quantity':0.0,date:today});

    };

    self.saveData = function(){
    var iac = new InventoryAccountConsumption();
        iac.id = self.mainData.id;
        iac.rows = self.mainData.rows;
        iac.$update({Id:self.accountId},
                function(data) {
                self.mainData = data;
                  alert("Consumption  "+self.mainData.name+" Updated ");
                },
                function(error) {
                    console.log(error);
                });

    };
}])

.controller('AddItemController', ['$scope','Site', 'Item', 'Category', 'InventoryAccount', 'NextAccountNo', '$modal', '$timeout',
'$routeParams', '$location',
function($scope, Site, Item, Category, InventoryAccount, NextAccountNo, $modal, $timeout, $routeParams, $location){
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
                if(!self.item.account_no){
                    self.next_account_data = NextAccountNo.query(null,
                    function(data) {
                    self.item.account_no = data.ac_no;
                    },
                    function(error) {
                        console.log(error);
                    });
                    }
                for(var i=0;i<self.categories.length;i++){
                    if(self.categories[i].id == self.item.category_id){
                        self.item.category = self.categories[i];
                    }
                }
            },
            function(error) {
                console.log(error);
            });


    }else{
        self.next_account_data = NextAccountNo.query(null,
        function(data) {
        self.item.account_no = data.ac_no;
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
            itemService.account_no = self.item.account_no;
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
        itemService.account_no = self.item.account_no;
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
          $modalInstance.dismiss('cancel');

    };
    })


.controller('ItemAddModalController', function($scope, $modalInstance, Item, Category, NextAccountNo) {
    var self = $scope;
    self.options = ['consumable', 'non-consumable'];
    self.newItem = {};
    self.items = {};
    Category.query(null,
        function(data) {
        self.categories = data;
        self.newItem.category_id = self.categories[0].id;
        self.newItem.type = self.options[1];
        },
        function(error) {
            console.log(error);
        });

      if(!self.newItem.account_no){
                    self.next_account_data = NextAccountNo.query(null,
                    function(data) {
                    self.newItem.account_no = data.ac_no;
                    },
                    function(error) {
                        console.log(error);
                    });
                    }

    self.ok = function() {

        $modalInstance.close(self.newItem);
    };

    self.cancel = function(){
         $modalInstance.dismiss('cancel');

    };
    })


.controller('UserController', ['$scope', 'User', '$modal', '$timeout',
function($scope, User, $modal, $timeout){
    var self = $scope;
    var parent = self.$parent;
    self.users = User.query();

        self.openEditUser = function(user) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/users/add_user_modal.html'),
            controller: 'UserUpdateModalController',
            windowClass: 'app-modal-window',
            resolve: {
            user: function() {
                return user;
                }
            }
        });

        modalInstance.result.then(function(userdata) {
        if (!angular.equals({},userdata)){
        var es = new User();
            es.email = userdata.email;
            es.is_site_manager = userdata.is_site_manager;
            es.is_admin = userdata.is_admin;
            es.is_active = userdata.is_active;
            es.$update({uId:userdata.id},
            function(data) {
                for( var i=0; i< self.users.length; i++){
                    if(self.users[i].id == data.id){
                        self.users[i]= data;

                    }
                }
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };

}])

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
            Role: function() {
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
            es.site_id = self.siteID;
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

.controller('PartyController', ['$scope', 'Party', 'PartyPayment', '$modal', '$timeout', '$routeParams',
function($scope, Party, PartyPayment, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.parties = Party.query();

    self.openAddParty = function(party) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/inventory/party/add_party_modal.html'),
            controller: 'PartyAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            party: function() {
                return party;
            }
            }
        });

        modalInstance.result.then(function(partyData) {
        if (!angular.equals({},partyData)){
        var ps = new Party();
            ps.name = partyData.name;
            ps.address = partyData.address;
            ps.phone_no = partyData.phone_no;
            ps.pan_no = partyData.pan_no;
            if(partyData.id){
                ps.$update({Id:partyData.id},
                function(data) {
                    for(var i=0; i<self.parties.length; i++){
                        if(self.parties[i].id == data.id){
                            self.parties[i]= data;
                            i= self.parties.length;
                        }
                    }
                },
                function(error) {
                    console.log(error);
                });
            }else{
                ps.$save(null,
                function(data) {
                    self.parties.splice(0, 0, data);
                },
                function(error) {
                    console.log(error);
                });

            }


            }
        });
    };


}])


.controller('BankWithDrawController', ['$scope', 'Bank','BankWithdraw', '$modal', '$timeout', '$routeParams',
function($scope, Bank, BankWithdraw, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.bankId = $routeParams.bankId;
    self.bank = {};
     var bs = new Bank();
       bs.$bank({Id:self.bankId},
        function(data) {
        self.bank = data;
        },
        function(error) {
            console.log(error);
        });
    self.amount = 0.00;
    self.voucher_no = 1;
    self.is_deposit = false;
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    self.date = today;
    self.withdrawAmount = function(){
       var bws = new BankWithdraw();
       bws.bank_id = self.bankId;
       bws.rows= [];
       bws.rows.push({'amount':self.amount,'date':self.date,'is_deposit':self.is_deposit,'voucher_no':self.voucher_no});
        bws.$update({Id:self.bankId},
            function(data) {
            alert("Transaction Complete")
            console.log(data);
            self.bank.current_dr = data.dr_balance;
            self.bank.current_cr = data.cr_balance;
            self.amount = 0.00;
            self.date = today;
            },
            function(error) {
                console.log(error);
            });
    };



}])

.controller('VendorPaymentController', ['$scope', 'Bank','Vendor', 'VendorPayment', '$modal', '$timeout', '$routeParams',
function($scope, Bank, Vendor, VendorPayment, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.vendorId = $routeParams.vendorId;
    self.banks = Bank.query();
    self.vendor = {};
     var bs = new Vendor();
       bs.$vendor({Id:self.vendorId},
        function(data) {
        self.vendor = data;
        },
        function(error) {
            console.log(error);
        });
    var newDate = new Date();
    var today = newDate.toISOString().substring(0, 10);
    self.rows= [];
   self.rows.push({'amount':0.00,'date':today,'bank_id':1,'voucher_no':1});
    self.withdrawAmount = function(){
       var bws = new VendorPayment();
       bws.vendor_id = self.vendorId;
       bws.rows= self.rows;
        bws.$update({Id:self.vendorId},
            function(data) {
            alert("withdraw Complete")
            self.vendor.current_dr = data.dr_balance;
            self.vendor.current_cr = data.cr_balance;
            self.rows[0].amount = 0.00;
            self.rows[0].date = today;
            },
            function(error) {
                console.log(error);
            });
    };

    self.openAddBank = function(bank) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/account/bank/add_bank_modal.html'),
            controller: 'BankAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            bank: function() {
                return bank;
            }
            }
        });

        modalInstance.result.then(function(bankData) {
        if (!angular.equals({},bankData)){
        var ps = new Bank();
            ps.name = bankData.name;
            ps.address = bankData.address;
            ps.phone_no = bankData.phone_no;
            ps.code = bankData.code;
            ps.current_dr = bankData.current_dr;
            ps.current_cr = bankData.current_cr;
            ps.$save(null,
                function(data) {
                alert("bank "+data.name+" added");
                    self.banks.splice(0, 0, data);
                    self.rows[0].bank_id = data.id;
                },
                function(error) {
                    console.log(error);
                });
            }
        });
    };

}])

.controller('BankController', ['$scope', 'Bank', '$modal', '$timeout', '$routeParams',
function($scope, Bank, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.banks = Bank.query();

    self.openAddBank = function(bank) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/account/bank/add_bank_modal.html'),
            controller: 'BankAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            bank: function() {
                return bank;
            }
            }
        });

        modalInstance.result.then(function(bankData) {
        if (!angular.equals({},bankData)){
        var ps = new Bank();
            ps.name = bankData.name;
            ps.address = bankData.address;
            ps.phone_no = bankData.phone_no;
            ps.code = bankData.code;
            ps.current_dr = bankData.current_dr;
            ps.current_cr = bankData.current_cr;
            if(bankData.id){
                ps.$update({Id:bankData.id},
                function(data) {
                alert("bank "+data.name+" updated");
                    for(var i=0; i<self.banks.length; i++){
                        if(self.banks[i].id == data.id){
                            self.banks[i]= data;
                            i= self.banks.length;
                        }
                    }
                },
                function(error) {
                    console.log(error);
                });
            }else{
                ps.$save(null,
                function(data) {
                alert("bank "+data.name+" added");
                    self.banks.splice(0, 0, data);
                },
                function(error) {
                    console.log(error);
                });

            }


            }
        });
    };


}])

.controller('VendorController', ['$scope', 'Vendor', '$modal', '$timeout', '$routeParams',
function($scope, Vendor, $modal, $timeout, $routeParams){
    var self = $scope;
    var parent = self.$parent;
    self.vendors = Vendor.query();

    self.openAddVendor = function(vendor) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/account/vendor/add_vendor_modal.html'),
            controller: 'VendorAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            vendor: function() {
                return vendor;
            }
            }
        });

        modalInstance.result.then(function(objData) {
        if (!angular.equals({},objData)){
        var ps = new Vendor();
            ps.name = objData.name;
            ps.address = objData.address;
            ps.phone_no = objData.phone_no;
            ps.code = objData.code;
            ps.current_dr = objData.current_dr;
            ps.current_cr = objData.current_cr;
            if(objData.id){
                ps.$update({Id:objData.id},
                function(data) {
                alert("Vendor "+data.name+" updated");
                    for(var i=0; i<self.vendors.length; i++){
                        if(self.vendors[i].id == data.id){
                            self.vendors[i]= data;
                            i= self.vendors.length;
                        }
                    }
                },
                function(error) {
                    console.log(error);
                });
            }else{
                ps.$save(null,
                function(data) {
                alert("vendor "+data.name+" added");
                    self.vendors.splice(0, 0, data);
                },
                function(error) {
                    console.log(error);
                });

            }


            }
        });
    };


}])

