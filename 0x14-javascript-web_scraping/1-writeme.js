#!/usr/bin/node
let fs = require('fs'), filename = process.argv[2], string = process.argv[3];

fs.writeFile(filename, string, 'utf8', function(err, data) {
    if (err) {
	console.log (err);
    }
    console.log(string > data);
});

