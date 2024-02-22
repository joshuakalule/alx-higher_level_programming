#!/usr/bin/node
const SquareOld = require('./5-square');
module.exports = class Square extends SquareOld {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str;
    if (c === undefined) { c = 'X'; }
    for (let row = 0; row < this.height; row++) {
      str = '';
      for (let col = 0; col < this.width; col++) {
        str += c;
      }
      console.log(str);
    }
  }
};
