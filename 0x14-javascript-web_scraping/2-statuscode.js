#!/usr/bin/node
let request = require('request');
let requestURL = process.argv[2];

request.get(requestURL, function (error, response, body) {
  let code = response.statusCode;
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + code);
  }
});
