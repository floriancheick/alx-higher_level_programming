#!/usr/bin/node

const MainSquare = require('./5-square');

module.exports = class Square extends MainSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let row = 1; row <= this.height; row++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
