#!/usr/bin/node
function factorial (num = 0) {
    if (num === 0) {
	return 1;
    } else {
	return num * factorial(num - 1);
    }
}

console.log(factorial(process.argv[2]));
