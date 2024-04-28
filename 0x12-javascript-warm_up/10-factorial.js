#!/usr/bin/node
const { argv } = require('node:process');

function factorial (x) {
  if (x && x > 0) return (x + factorial(x - 1));
  else return (0);
}
const v = Number(argv[2]);
if (isNaN(v)) console.log(1);
else console.log(factorial(v));
