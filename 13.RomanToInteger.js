var romanToInt = (s) => {
	var sum = 0;
	var currentValue;
	var prevValue;

	for (var i = 0; i < s.length; i++) {
			currentValue = matchLetter(s[i]);
			prevValue = matchLetter(s[i - 1]);
			if (currentValue > prevValue) {
				sum = (sum-prevValue) + (currentValue - prevValue);
			} else {
				sum = sum + currentValue;
			}
		console.log(sum);
	}
};

var matchLetter = (x) => {
	switch (x) {
		case 'I':
			return 1;
		case 'V':
			return 5;
		case 'X':
			return 10;
		case 'L':
			return 50;
		case 'C':
			return 100;
		case 'D':
			return 500;
		case 'M':
			return 1000;
	}
};
romanToInt('MCDLXXVI');
