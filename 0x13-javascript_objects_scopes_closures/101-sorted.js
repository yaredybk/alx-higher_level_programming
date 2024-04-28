#!/usr/bin/node
const {dict} = require('./101-data.js');
let sorted = {};
Object.keys(dict).forEach(k => sorted[dict[k]]
	? sorted[dict[k]].push(k)
	: sorted[dict[k]] = [k]);
console.log(sorted);
