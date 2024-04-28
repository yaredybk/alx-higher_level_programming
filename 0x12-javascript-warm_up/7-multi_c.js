#!/usr/bin/node
const { argv } = require('node:process');

let v = Math.floor(Number(argv[2]));
if (isNaN(v)) console.log('Missing number of occurrences');
else while (v--) console.log('C is fun');
