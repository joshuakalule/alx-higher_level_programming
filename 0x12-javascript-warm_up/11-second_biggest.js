#!/usr/bin/node
const { argv } = require('node:process');
let maxSecond = Number.NEGATIVE_INFINITY;
let max = Number.NEGATIVE_INFINITY;

if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i], 10);

    if (num > max) {
      maxSecond = max;
      max = num;
    } else if (num > maxSecond && num < max) {
      maxSecond = num;
    }
  }
  if (maxSecond === Number.NEGATIVE_INFINITY) {
    console.log(0);
  } else {
    console.log(maxSecond);
  }
}
