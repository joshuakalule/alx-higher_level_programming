#!/usr/bin/node
const SquareOld = require('./5-square');
module.exports = class Square extends SquareOld {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str;
    if (c === undefined) { c = 'X'; }
    for (let r = 0; r < this.height; r++) {
      str = '';
      for (let c = 0; c < this.weight; c++) {
        str += c;
      }
      console.log(str);
    }
  }
};
