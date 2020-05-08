#!/usr/bin/node
let fs = require('fs');
let request = require('request');
let requestURL = process.argv[2];
let filename = process.argv[3];

request(requestURL, function (error, response, body) {
  let code = response.statusCode;
  if (error) { 
    console.log (error);
  }
  if (code == 200) {
    fs.writeFile(filename, body, 'utf8');
  }
});
