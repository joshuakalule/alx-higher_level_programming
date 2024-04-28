#!/usr/bin/node
// Prints the title of a Star Wars movie
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode !== 200) {
    console.log(`Status: ${response.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
