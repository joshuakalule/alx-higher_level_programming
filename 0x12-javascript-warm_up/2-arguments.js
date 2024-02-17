#!/usr/bin/node
const { argv } = require('node:process');
const size = argv.length;
if (size === 2) {
  console.log('No argument');
} else if (size === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
