#!/usr/bin/node
// Display the status code of a GET request
const request = require('request');

const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
