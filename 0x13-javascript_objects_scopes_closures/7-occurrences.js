#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    const element = list[i];
    if (element === searchElement) {
      count++;
    }
  }
  return count;
}
