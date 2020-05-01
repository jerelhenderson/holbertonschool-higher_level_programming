#!/usr/bin/node
let size = parseInt(process.argv[2]);

if (isNaN(parseInt(process.argv[2]))) {
    console.log('Missing size');
} else {
    for (let i = 0; i < size; i++) {
	let square = '';
	for (let j = 0; j < size; j++) {
	    square = square + 'X';
	}
	console.log(square);
    }
}
