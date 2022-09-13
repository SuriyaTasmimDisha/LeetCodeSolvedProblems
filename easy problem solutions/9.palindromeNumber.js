var palindrome = (x) => {
	if (x < 0) return console.log(false);
	let num = x,
		rev = 0;
	while (num !== 0) {
		rev = rev * 10 + (num % 10);
		num = Math.floor(num / 10);
	}
	return console.log(x === rev);
};
palindrome(0);
