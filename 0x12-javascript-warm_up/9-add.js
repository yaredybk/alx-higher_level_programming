#!/usr/bin/node
const { argv } = require('node:process');

const v = Number(argv[2]);
const w = Number(argv[3]);
console.log(v + w);
