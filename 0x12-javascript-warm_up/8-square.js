#!/usr/bin/node
const { argv } = require('node:process');

const v = Number(argv[2]);
console.log(v);
if (v) {
  let i = v, j = v, s = '';
  while (i--) s += 'X';
  while (j--) console.log(s);
} else console.log('Missing size');
