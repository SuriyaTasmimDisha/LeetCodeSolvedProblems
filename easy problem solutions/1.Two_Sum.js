var twoSum = function (nums, target) {
    var hashTable = [];
    for(var i = 0; i<nums.length; i++){
        var diff = target - nums[i];
        if (hashTable.includes(diff)){
            console.log([hashTable.indexOf(diff), i]); 
        }
        
        hashTable.push(nums[i]);
    }
};

twoSum([2, 7, 11, 15], 9);