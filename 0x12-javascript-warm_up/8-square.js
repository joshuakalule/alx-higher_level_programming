#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
let row;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < size; r++) {
    row = '';
    for (let c = 0; c < size; c++) {
      row += 'x';
    }
    console.log(row);
  }
}
