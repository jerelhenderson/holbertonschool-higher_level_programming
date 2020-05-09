#!/usr/bin/node
let request = require('request');
let count = 0;

request.get(process.argv[2], function (error, response, body) {
  let code = response.statusCode;
  if (error) {
    console.log(error);
  } if (code === 200) {
    let results = JSON.parse(body).results;
    for (let i in results) {
      let chars = results[i].characters;
      for (let j in chars) {
        if (chars[j].search('/18/') > 0) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
