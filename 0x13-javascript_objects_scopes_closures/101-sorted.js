#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const numOcurrance of Object.values(dict)) {
  const list = [];
  for (const [key, value] of Object.entries(dict)) {
    if (numOcurrance === value) { list.push(key); }
  }
  newDict[numOcurrance] = list.sort();
}
console.log(newDict);
