#!/usr/bin/node
const { argv } = require('node:process');

let v = Integer.parseint(argv[2]);
if (v) console.log(`My number: ${v}`);
else console.log('Not a number');
