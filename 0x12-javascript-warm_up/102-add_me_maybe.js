#!/usr/bin/node
exports.callMeMoby = function (number, theFunction = () => null) {
  theFunction(number++);
};
