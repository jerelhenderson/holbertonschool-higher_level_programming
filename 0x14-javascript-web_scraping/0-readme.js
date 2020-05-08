#!/usr/bin/node
let fs = require('fs'), filename = process.argv[2];

fs.readFile(filename, 'utf8', function(err, data) {
    if (err) {
	console.log (err);
    }
    console.log(data);
});

