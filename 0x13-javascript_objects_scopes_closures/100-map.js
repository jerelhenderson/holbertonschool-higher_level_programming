#!/usr/bin/node
let list = require('./100-data').list;
console.log(list);

let listMap = list.map((value, index) => {
	return (value * index);
});
console.log(listMap);
