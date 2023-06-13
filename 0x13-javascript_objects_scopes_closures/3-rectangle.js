#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let iter = 0; iter < this.height; iter++) {
      let row = '';
      for (let iter2 = 0; iter2 < this.width; iter2++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
