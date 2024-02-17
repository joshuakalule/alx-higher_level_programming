#!/usr/bin/node
const first = process.argv[2];
const second = process.argv[3];

function add (a, b) {
  return (parseInt(a, 10) + parseInt(b, 10));
}

console.log(add(first, second));
