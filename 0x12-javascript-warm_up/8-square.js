#!/usr/bin/node
const { argv } = require('node:process');

const v = Number(argv[2]);
if (v) {
  let i = v;
  let s = '';
  while (i--) s += 'X';
  i = v;
  while (i--) console.log(s);
} else console.log('Missing size');
