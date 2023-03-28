#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width =w;
      this.height = h;
    }
  }

  print () {
    for (let row = 1; row <= this.height; row++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const con = this.width;
    this.width = this.height;
    this.height = con;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
