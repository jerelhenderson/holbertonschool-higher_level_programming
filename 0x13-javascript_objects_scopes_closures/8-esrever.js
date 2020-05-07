#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length;
  let backwardsList = [];

  for (let i = length - 1; i >= 0; i--) {
    backwardsList.push(list[i]);
  }
  return backwardsList;
};
