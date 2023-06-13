#!/usr/bin/node

const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
