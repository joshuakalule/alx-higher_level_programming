#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2], 10);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
