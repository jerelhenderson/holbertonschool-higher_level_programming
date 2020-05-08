#!/usr/bin/node
let requestURL = process.argv[2]
let request = require('request');

request.get(requestURL, (error, response, body) => {
    let code = response.statusCode;
    if (error) {
	console.log(error);
    } else {
	console.log("code: " + code);
    } 
});
