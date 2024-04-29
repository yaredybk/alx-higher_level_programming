#!/usr/bin/node
const { argv } = require('node:process');
let store = [0, 0];
if (argv.length < 4) console.log(0);
else {
  argv.forEach((e) => {
    e = Number(e);
    if (e && e > store[1]) {
      if (e > store[0]) store = [e, store[0]];
      else store[1] = e;
    }
  });
  console.log(store[1]);
}
