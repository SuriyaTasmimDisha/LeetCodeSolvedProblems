var longestCommonPrefix = (s) => {
    var firstWord = s[0].split('');
	var i = 1;
	while (i < s.length) {
		var comparedWord = s[i].split('');
		for (let index = 0; index <= comparedWord.length; index++) {
			if (firstWord[index] !== comparedWord[index]) {
                 firstWord = firstWord.slice(0, index);
                break;
            } 
        }
        i++;
    }
    if (firstWord.length>0) {
        console.log(firstWord.join(''));
    } else {
        console.log('"');
    }
};

longestCommonPrefix(["ab", "a"]);
