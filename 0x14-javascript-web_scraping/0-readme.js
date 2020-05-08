#!/usr/bin/node
let fs = require('fs');
let filename = process.argv[2];

fs.readFile(filename, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  }
  console.log(data);
});
