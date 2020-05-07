#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let length = list.length;
  let occurrences = 0;
  for (let i = 0; i < length; i++) {
    if (list[i] === searchElement) {
      occurrences++;
    }
  }
  return occurrences;
};
