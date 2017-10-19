
app.controller("MainController", function ($scope, $window){

    function constructor() {
        $scope.num = 0;
        $scope.save = function(){
            $(".data").html("Click:" + $scope.num);
            $scope.num += 1 ;
        };
    };

    constructor();
});