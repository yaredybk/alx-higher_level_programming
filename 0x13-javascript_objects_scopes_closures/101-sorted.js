#!/usr/bin/node
const { dict } = require('./101-data.js');
let sorted = {};
Object.keys(dict).forEach((k) => {
  if (sorted[dict[k]] == undefined) sorted[dict[k]] = [k];
  else sorted[dict[k]].push(k);
}
console.log(sorted);
