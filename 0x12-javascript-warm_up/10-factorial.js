#!/usr/bin/node
function factorial (n) {
	return n === 2 ? 2 : n * factorial(n - 1);
}
if(process.argv[2] === 0 || isNaN(process.argv[2])){
	console.log(1);
}
else{
	console.log(factorial(process.argv[2]));
}

