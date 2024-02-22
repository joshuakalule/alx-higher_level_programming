#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      constructor();
    }
  }

  print () {
    let str;
    for (let r = 0; r < this.height; r++) {
      str = '';
      for (let c = 0; c < this.width; c++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
