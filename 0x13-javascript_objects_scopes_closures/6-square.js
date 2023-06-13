#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    if (C === undefined) {
      C = 'X';
    }
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += C;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
