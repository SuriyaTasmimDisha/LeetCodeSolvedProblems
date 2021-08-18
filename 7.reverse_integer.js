var reverse = function(x) {
    var ans = parseInt(x.toString(10).split('').reverse().join(''));
    if (x < 0) {
        ans = ans * -1;
    }
    if (ans >= -Math.pow(2, 31) && ans <= Math.pow(2, 31) - 1) {
        return ans;
    } else {
        return 0;
    }
};
  
console.log(reverse(Math.pow(2, 33)));
console.log(reverse(-1223));