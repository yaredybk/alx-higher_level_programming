#!/usr/bin/node
const { argv } = require('node:process');

let v = Number(argv[2]);
if (v) while (v--) console.log('C is fun');
else console.log('Missing number of occurrences');
