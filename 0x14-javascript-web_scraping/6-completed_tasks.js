#!/usr/bin/node
let request = require('request');
let requestURL  = process.argv[2];
let finished = {};

request.get(requestURL, function (error, response, body) {
  let code = response.statusCode;
  if (error) { 
    console.log (error); 
  }
  if (code == 200) {
    let results = JSON.parse(body);
    for (let i in results) {
      let key = results[i];
      if (results[i].completed == true) {
        let id = key['userId'];
        if (id in finished) {
          finished[id] = finished[id] + 1
        } else {
          finished[id] = 1;
        }
      }
    }
    console.log (finished);
  }
});
