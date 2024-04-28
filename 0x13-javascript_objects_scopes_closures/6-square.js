#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    let s = '';
    for (let i = 0; i < this.width; i++) s = s + c;
    for (let i = 0; i < this.height; i++) {
      console.log(s);
    }
  }
};
