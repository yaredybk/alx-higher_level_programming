#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  while (j > i) {
    [list[i], list[j]] = [list[j], list[i]];
    i++;
    j--;
  }
  return list;
};
