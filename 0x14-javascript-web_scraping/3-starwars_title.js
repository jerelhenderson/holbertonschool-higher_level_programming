#!/usr/bin/node
let request = require('request');
let requestURL = 'http://swapi.co/api/films/' + process.argv[2];

request.get(requestURL, function (error, response, body) {
  let code = response.statusCode;
  if (error) {
    console.log(error);
  } if (code === 200) {
    console.log(JSON.parse(body).title);
  }
});
