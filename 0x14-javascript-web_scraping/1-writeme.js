#!/usr/bin/node
let fs = require('fs');
let filename = process.argv[2];
let string = process.argv[3];

fs.writeFile(filename, string, 'utf8', function(error, data) {
  if (error) {
    console.log (error);
  }
});
