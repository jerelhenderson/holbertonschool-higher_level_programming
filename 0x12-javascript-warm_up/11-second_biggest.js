#!/usr/bin/node

let arg = process.argv.slice(2).map(num => parseInt(num));
const sortedList = arg.sort((a, b) => a < b);

if (sortedList.length < 1) {
    console.log(0);
} else {
    console.log(sortedList[1]);
}
