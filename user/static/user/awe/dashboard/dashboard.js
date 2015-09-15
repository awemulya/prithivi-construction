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
  $routeProvider.when('/fixtures', {
    templateUrl: djstatic('user/awe/dashboard/fixture/fixtures.html'),
    controller: 'FixtureController'
  })
  $routeProvider.when('/fixtures/:fid', {
    templateUrl: djstatic('user/awe/dashboard/fixture/fixture_detail.html'),
    controller: 'FixtureDetailController',
    resolve: {
      // I will cause a 1 second delay
      delay: function($q, $timeout) {
        var delay = $q.defer();
        $timeout(delay.resolve, 1000);
        return delay.promise;
      }
    }
  })
  $routeProvider.when('/clubs', {
    templateUrl: djstatic('user/awe/dashboard/club/club.html'),
    controller: 'ClubController'
  });
}])

.controller('DashboardController', ['$scope', 'Site', '$modal', '$timeout', function($scope, Site, $modal, $timeout) {
 var self = $scope;
 self.sites = Site.query();

}])

.controller('PlayerDetailModalController', function($scope, $modalInstance, player) {
    var playerModal = $scope;
    playerModal.player = player;

     playerModal.profileImg = [{
        src: djstatic('user/vendor/dist/img/user2-160x160.jpg'),
    }];


    playerModal.ok = function() {
        $modalInstance.close();
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('FixtureModalController', function($scope, $modalInstance, player) {
    var playerModal = $scope;
    playerModal.player = player;

     playerModal.profileImg = [{
        src: djstatic('user/vendor/dist/img/user2-160x160.jpg'),
    }];


    playerModal.ok = function() {
        $modalInstance.close();
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})



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

.controller('FixtureController', ['$scope', 'Clubs', 'Player', 'Fixture', '$modal', '$timeout', '$routeParams',
function($scope, Clubs, Player, Fixture, $modal, $timeout, $routeParams) {

var self = $scope;
 self.fixtures = Fixture.query();

 self.openEditFixture = function(fixture) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/fixture/add_fixture_modal.html'),
            controller: 'EditFixtureModalController',
            windowClass: 'app-modal-window',
            resolve: {
            fixture: function() {
                    return fixture;
                },
            clubs: function() {
                    return Clubs;
                }

            }
        });

        modalInstance.result.then(function(fixture) {
        if (!angular.equals({},fixture)){
        var fixtureService = new Fixture();
            fixtureService.week = fixture.week;
            fixtureService.home = fixture.home;
            fixtureService.away = fixture.away;
            fixtureService.home_goals = fixture.home_goals;
            fixtureService.away_goals = fixture.away_goals;
            var t = fixture.time.split("-");
            fixtureService.time = new Date(t[0],t[1],t[2]);
            fixtureService.played = fixture.played;
            fixtureService.$update({pId: fixture.id},
            function(data) {
                    for (var i=0; i<self.fixtures.length; i++){
                if(self.fixtures[i].id == fixture.id){
                    self.fixtures[i] = data;
                    break;
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

.controller('FixtureDetailController', ['$scope', 'Clubs', 'Player', 'Fixture', '$modal', '$timeout', '$routeParams',
function($scope, Clubs, Player, Fixture, $modal, $timeout, $routeParams) {

var self = $scope;
self.fid =  $routeParams.fid;
self.fixture = {};
var playerService = new Fixture();
    playerService.$fixture({pId:self.fid},
            function(data) {
            self.fixture = data;
            },
            function(error) {
                console.log(error);
            });

}])

.controller('ClubController', ['$scope', 'Clubs', 'Player', 'Fixture', '$modal', '$timeout',
function($scope, Clubs, Player, Fixture, $modal, $timeout) {
 var self = $scope;
 self.clubs = Clubs.query();
 self.profileImg = [{
        src: djstatic('user/vendor/dist/img/user2-160x160.jpg'),
    }];

    self.openPlayers = function(players) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/players_modal.html'),
            controller: 'ClubPlayerModalController',
            windowClass: 'app-modal-window',
            resolve: {
                players: function() {
                    return players;
                }
            }
        });
        modalInstance.result.then(function() {
        });
    };
    self.openResults = function(game, played) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/results_modal.html'),
            controller: 'ClubResultsModalController',
            windowClass: 'app-modal-window',
            resolve: {
                game: function() {
                    return game;
                },
                played: function() {
                    return played;
                }
            }
        });
        modalInstance.result.then(function() {
        });
    };

    self.openEditClub = function(club) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/club_modify_modal.html'),
            controller: 'ClubModalController',
            windowClass: 'app-modal-window',
            resolve: {
                club: function() {
                    return club;
                }
            }
        });

        modalInstance.result.then(function(clubData) {
        var clubService = new Clubs();
        clubService.name = clubData.name;
        clubService.established = clubData.established;
         clubService.$update({clubId:clubData.id},
            function(data) {
            for (var i=0; i<self.clubs.length; i++){
                if(self.clubs[i].id == data.id){
                    self.clubs[i] = data;
                    break;
                }
            }
            },
            function(error) {
                console.log(error);
            });


        });
    };

self.openAddClub = function() {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/club_modify_modal.html'),
            controller: 'ClubAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            add: function() {
                    return true;
                }

            }
        });

        modalInstance.result.then(function(clubData) {
        if (!angular.equals({},clubData)){
        var clubService = new Clubs();
        clubService.name = clubData.name;
        clubService.established = clubData.established;
         clubService.$save(null,
            function(data) {
                    self.clubs.splice(0, 0, data);
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };

self.openAddPlayers = function(club) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/add_players_modal.html'),
            controller: 'PlayerAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            club: function() {
                    return club;
                },
            clubService: function() {
                    return "";
                },
            player: function() {
                return false;
            }

            }
        });

        modalInstance.result.then(function(playerData) {
        if (!angular.equals({},playerData)){
        var playerService = new Player();
            playerService.name = playerData.name;
            playerService.position = playerData.position;
            playerService.club = playerData.club_id;
            playerService.date_of_birth = playerData.date_of_birth;
            playerService.$save(null,
            function(data) {
                    for (var i=0; i<self.clubs.length; i++){
                if(self.clubs[i].id == data.club){
                    self.clubs[i].players.splice(0, 0, data);
                    break;
                }
            }
            },
            function(error) {
                console.log(error);
            });

            }
        });
    };


self.openAddResults = function(club, clubs) {
        var modalInstance = $modal.open({
            animation: true,
            templateUrl: djstatic('user/awe/dashboard/club/add_results_modal.html'),
            controller: 'ResultsAddModalController',
            windowClass: 'app-modal-window',
            resolve: {
            club: function() {
                    return club;
                },
            clubs: function() {
                    return clubs;
                }

            }
        });

        modalInstance.result.then(function(fixture) {
        if (!angular.equals({},fixture)){
        var fixtureService = new Fixture();
            fixtureService.week = fixture.week;
            fixtureService.home = fixture.home;
            fixtureService.away = fixture.away;
            fixtureService.home_goals = fixture.home_goals;
            fixtureService.away_goals = fixture.away_goals;
            fixtureService.time = fixture.date_of_birth;
            fixtureService.played = fixture.played;
            fixtureService.$save(null,
            function(data) {
                    for (var i=0; i<self.clubs.length; i++){
                if(self.clubs[i].id == club.id){
                    self.clubs[i].game.push(data);
                    break;
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

.controller('ClubPlayerModalController', function($scope, $modalInstance, players) {
    var playerModal = $scope;
    playerModal.players = players;

     self.profileImg.when('/Book/:bookId', {
    templateUrl: 'book.html',
    controller: 'BookController',
    resolve: {
      // I will cause a 1 second delay
      delay: function($q, $timeout) {
        var delay = $q.defer();
        $timeout(delay.resolve, 1000);
        return delay.promise;
      }
    }
  }) = [{
        src: djstatic('user/vendor/dist/img/user2-160x160.jpg'),
    }];

    playerModal.ok = function() {
        $modalInstance.close();
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('ClubResultsModalController', function($scope, $modalInstance, game, played) {
    var playerModal = $scope;
    playerModal.game = game;
    playerModal.played = played;
    playerModal.ok = function() {
        $modalInstance.close();
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('ClubModalController', function($scope, $modalInstance, club) {
    var playerModal = $scope;
    playerModal.club = angular.copy(club);

    playerModal.ok = function() {
        $modalInstance.close(playerModal.club);
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('ClubAddModalController', function($scope, $modalInstance, add) {
    var playerModal = $scope;
    playerModal.club = {};
    playerModal.operation = add;

    playerModal.ok = function() {
        $modalInstance.close(playerModal.club);
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})


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

.controller('PlayerUpdateModalController', function($scope, $modalInstance, player, clubService) {
    var playerModal = $scope;
    playerModal.options = ['goalkeeper', 'defender', 'midfielder', 'forward'];
    playerModal.$watch('clubs', function(clubs) {
    for(var i=0; i< clubs.length; i++){
        console.log(playerModal.player.club);
        if(clubs[i].id == playerModal.player.club){
            playerModal.player.club = clubs[i];
            i = clubs.length;
        }
    }
}, true);
    playerModal.player = player;
    playerModal.club = {};
    playerModal.club.established = "1990-01-01";
    playerModal.playerSenario = true;
    playerModal.clubs = clubService.query();
    playerModal.ok = function() {
        playerModal.player.date_of_birth =  playerModal.club.established;
        $modalInstance.close(playerModal.player);
    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('ResultsAddModalController', function($scope, $modalInstance, club, clubs) {
    var playerModal = $scope;
    playerModal.validateMsg = "";
    playerModal.club = angular.copy(club);
    playerModal.clubs = angular.copy(clubs);
    playerModal.fixture = {};
    playerModal.fixture.time =  playerModal.club.established;
    playerModal.fixture.played =  false;
    playerModal.ok = function() {
        if(angular.isObject(playerModal.fixture.home)){
         playerModal.fixture.home = playerModal.fixture.home.id;
        }
        if(angular.isObject(playerModal.fixture.away)){
         playerModal.fixture.away = playerModal.fixture.away.id;
        }
        playerModal.fixture.time =  playerModal.club.established;
        $modalInstance.close(playerModal.fixture);
    };

    playerModal.sameClub = function(){
        var home= "";
        var away= "";
        if(angular.isObject(playerModal.fixture.home)){
             home = playerModal.fixture.home.id;
        }else{
            home = playerModal.fixture.home;
        }
        if(angular.isObject(playerModal.fixture.away)){
         away = playerModal.fixture.away.id;
        }else{
         away = playerModal.fixture.away;
        }
        if(angular.equals(playerModal.fixture.home, playerModal.fixture.away)){
        playerModal.validateMsg = "Same Club in Home and Away.";
        return true;

        }
        playerModal.validateMsg =false;
        return false;

    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})

.controller('EmployeeController', ['$scope', 'Employee', 'SiteEmployee', 'Site', 'Role', 'SalaryRecord', 'Salary', '$modal', '$timeout', '$routeParams',
function($scope, Employee, SiteEmployee, Site, Role, SalaryRecord, Salary, $modal, $timeout, $routeParams){
    var self = $scope
    self.siteID =  $routeParams.siteId;
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
            },
            }
        });
    };


}])

.controller('EditFixtureModalController', function($scope, $modalInstance, fixture, Clubs) {
    var playerModal = $scope;
    playerModal.club = {};
    playerModal.$watch('clubs', function(clubs) {
    playerModal.fixture = fixture;
    playerModal.club.established = playerModal.fixture.time;
    for(var i=0; i< clubs.length; i++){
        if(clubs[i].id == playerModal.fixture.home){
            playerModal.fixture.home = clubs[i];
        }else if(clubs[i].id == playerModal.fixture.away){
            playerModal.fixture.away = clubs[i];
        }
    }
}, true);
    playerModal.validateMsg = "";
    playerModal.clubs = Clubs.query();
    playerModal.ok = function() {
        if(angular.isObject(playerModal.fixture.home)){
         playerModal.fixture.home = playerModal.fixture.home.id;
        }
        if(angular.isObject(playerModal.fixture.away)){
         playerModal.fixture.away = playerModal.fixture.away.id;
        }
        playerModal.fixture.time =  playerModal.club.established;
        $modalInstance.close(playerModal.fixture);
    };

    playerModal.sameClub = function(){
        var home= "";
        var away= "";
        if(angular.isObject(playerModal.fixture.home)){
             home = playerModal.fixture.home.id;
        }else{
            home = playerModal.fixture.home;
        }
        if(angular.isObject(playerModal.fixture.away)){
         away = playerModal.fixture.away.id;
        }else{
         away = playerModal.fixture.away;
        }
        if(angular.equals(playerModal.fixture.home, playerModal.fixture.away)){
        playerModal.validateMsg = "Same Club in Home and Away.";
        return true;

        }
        playerModal.validateMsg =false;
        return false;

    };

    playerModal.cancel = function() {
        $modalInstance.dismiss('cancel');
    };
})