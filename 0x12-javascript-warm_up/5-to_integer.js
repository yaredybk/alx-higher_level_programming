#!/usr/bin/node
const { argv } = require('node:process');

let v = Number(argv[2]);
if (v) console.log(`My number: ${v}`);
else console.log('Not a number');
