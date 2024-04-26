#!/usr/bin/node
const { argv } = require('node:process');

const v = Number(argv[2]);
if (v) console.log(`My number: ${v}`);
else console.log('Not a number');
