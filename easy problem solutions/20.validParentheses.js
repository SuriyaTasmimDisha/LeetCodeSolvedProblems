var str = "(){}[()]";
var length = str.length;
var flag = false;
var index = 0;

if (length % 2 === 0) {
	while (index < length) {
		if (str[index] === "(") {
			if (str.charCodeAt(index) === str.charCodeAt(index + 1) - 1) {
				flag === true;
				index += 2;
			}
		} else if (str.charCodeAt(index) === str.charCodeAt(index + 1) - 2) {
			flag = true;
			index += 2;
		} else if (str[index] === "(") {
			if (str.charCodeAt(index) === str.charCodeAt(length - index - 1) - 1) {
				flag = true;
				break;
			}
		} else if (
			str.charCodeAt(index) ===
			str.charCodeAt(length - index - 1) - 2
		) {
			flag = true;
			break;
        }
        index++;
	}
    console.log("flag: " + flag);
} else {
	console.log(false);
}
