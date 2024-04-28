#!/usr/bin/node
exports.callMeMoby = function (x, theFunction = () => null) {
  while (x--) theFunction();
};
