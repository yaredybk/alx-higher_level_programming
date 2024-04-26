#!/usr/bin/node
const {argv} = require('node:process');

if (argv.lenght === 2) return console.log('No argument');
if (argv.lenght === 3) return console.log('Argument found');
return console.log('Arguments found');
