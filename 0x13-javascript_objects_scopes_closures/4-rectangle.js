#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;

    console.log('X'.repeat(this.width));
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
};