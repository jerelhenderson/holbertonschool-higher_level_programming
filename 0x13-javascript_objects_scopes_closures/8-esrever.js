#!/usr/bin/node
exports.esrever = function (list) {
  let backwardsList = [];

  for (let i = 0; list.length !== 0; i++) {
    backwardsList.push(list.pop());
  }
  return backwardsList;
};
